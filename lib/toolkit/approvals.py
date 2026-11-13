"""EM's approvals at station 7, kept in one file: lib/approvals.csv (EM, 2026-11-06: "approved" for the 25 elements waiting on him;
he chose a sign-off page with a yes or no per figure over a blanket approval).

The page (claude.ai artifact "Station 7 Sign-off") lists every figure that holds an element for EM: open_lines() below, the same
rule DOC-005 counts by. EM accepts or refuses each line there; the core chat reads his decisions and merges them into
lib/approvals.csv (merge(), `python lib/build.py approvals merge <decisions.json>`), and pushes core. Every row carries EM's mark
("· EM <date>") in `signed`, so the PC's pre-push hook refuses any unattended push that adds one (autopilot.em_lines), as it does
for a "REVIEW accepted:" line in a spec.

A row counts only while its figure's line still reads exactly as EM saw it: a lane that changes the figure (a source found, a
new class, a redesign) puts it back in front of EM. An accepted row clears that line's figures in DOC-005; a refused row is the
lane's to change (DOC-005 says so first, and the line board no longer counts the element as waiting on EM). A safety row signs
off a safety-function element at one version only.
"""
import csv, datetime as dt, os, re

from . import library

PATH = os.path.join(library.ROOT, "approvals.csv")
FIELDS = ["element", "version", "kind", "file", "line", "class", "figures", "decision", "figure", "note", "signed", "record"]
SIGNED = re.compile(r"·\s*EM\s+\d{4}-\d{2}-\d{2}")
NEED = ("A", None)                                              # class C is the reviewer's (OPERATING.md 6); class B a document wanted (EM 2026-11-09)
WANTED = ("B",)


def read(path=None):
    """every row of lib/approvals.csv that carries EM's mark"""
    try: rows = list(csv.DictReader(open(path or PATH, encoding="utf-8")))
    except OSError: return []
    return [r for r in rows if SIGNED.search(r.get("signed") or "")]


def rating_text(row):
    """how a ratings.csv row reads on the page and in approvals.csv"""
    return ", ".join(f"{k}={v}" for k, v in row.items())


def counts(eid, spec, brief="", ratings=(), rows=None, behaviour=""):
    """(figures EM accepted, figures EM refused) for an element, counting only rows whose line still reads as it did"""
    rows = read() if rows is None else [r for r in rows if SIGNED.search(r.get("signed") or "")]
    here = {ln.strip() for ln in (spec + "\n" + (brief or "") + "\n" + (behaviour or "")).splitlines()} | {rating_text(r) for r in ratings or ()}
    yes = no = 0
    for r in rows:
        if r.get("element") != eid or r.get("kind", "figure") != "figure" or (r.get("figure") or "").strip() not in here: continue
        try: n = max(1, int(r.get("figures") or 1))
        except ValueError: n = 1
        if r.get("decision") == "yes": yes += n
        elif r.get("decision") == "no": no += n
    return yes, no


def safety_signed(eid, version, rows=None):
    """EM signed off this safety-function element at this version on the page"""
    rows = read() if rows is None else [r for r in rows if SIGNED.search(r.get("signed") or "")]
    return any(r.get("element") == eid and r.get("kind") == "safety" and r.get("version") == version and r.get("decision") == "yes"
               for r in rows)


def open_lines(spec, brief_files=(), ratings=(), behaviour="", classes=NEED):
    """every line holding a figure that needs EM, as DOC-005 counts them (validate.open_figures, _extra_figures, behaviour_open):
    [{file, line, text, hits: [(kind, class)]}], class None for an unclassed one (counted as A). brief_files: [(name, text)].
    classes=WANTED lists the class B lines instead: the figures that wait for a standard's document (derive.wanted; EM 2026-11-09)."""
    body = re.sub(r"(Figures|Every figure) marked \*\*Assumption\*\*[^.]*\.", lambda m: "\n" * m.group(0).count("\n"), spec)
    lines, raw = body.splitlines(), spec.splitlines()
    hist = next((i for i, ln in enumerate(lines) if ln.startswith("## History")), len(lines))
    any_, cap = re.compile(r"assumption(?:\W{0,3}\(\s*([ABC])\s*\))?", re.I), re.compile(r"Assumption(?:\W{0,3}\(\s*([ABC])\s*\))?")
    out = []
    for i, ln in enumerate(lines):
        if "REVIEW accepted:" in ln: continue
        pat = cap if (i >= hist or ln.lstrip().startswith("#")) else any_
        hits = [("Assumption", h.upper() if h else None) for h in pat.findall(ln)]
        hits += [("NOT ON FILE", h or None) for h in re.findall(r"NOT ON FILE(?:\W{0,3}\(\s*([ABC])\s*\))?", ln)]
        hits = [h for h in hits if h[1] in classes]
        if hits: out.append(dict(file="spec.md", line=i + 1, text=raw[i].strip(), hits=hits))
    for r in ratings or ():
        m = re.match(r"\s*assumption(?:\W{0,3}\(\s*([ABC])\s*\))?", r.get("status") or "", re.I)
        if m and (m.group(1) or "A").upper() in classes:
            out.append(dict(file="ratings.csv", line=0, text=rating_text(r), hits=[("Assumption", (m.group(1) or "A").upper())]))
    for name, text in brief_files:
        for i, ln in enumerate(text.splitlines()):
            if ln.lstrip().startswith("|") and "NOT ON FILE" in ln:
                k = re.search(r"NOT ON FILE(?:\W{0,3}\(\s*([ABC])\s*\))?", ln).group(1)
                if k in classes: out.append(dict(file=f"references/{name}", line=i + 1, text=ln.strip(), hits=[("NOT ON FILE", k)]))
    from .validate import behaviour_open                                      # escape mech-r68:4
    for i, text, kind, k in behaviour_open(behaviour):
        if k in classes: out.append(dict(file="behaviour.csv", line=i, text=text, hits=[(kind, k)]))
    return out


# A PC without time-zone data (Windows Python with no tzdata package: ZoneInfo raises) must not date EM's decisions in UTC:
# every approval after 18:00 Chicago would be signed with the next day's date (library run 2026-11-06 13:52, refused core
# 3496d48). The fallback carries the zone's own rules; a zone it doesn't know is refused, never dated in UTC.
FALLBACK = {"America/Chicago": -6}                              # US Central: standard offset, US daylight rules (since 2007)


def _zone(tz, zoneinfo=True):
    """the zone EM's decisions are dated in: ZoneInfo when the PC has its data, else the fixed rules below (zoneinfo=False
    forces the fallback, as on a PC without tzdata)"""
    if zoneinfo:
        try:
            from zoneinfo import ZoneInfo; return ZoneInfo(tz)
        except Exception: pass
    if tz not in FALLBACK: raise ValueError(f"no time-zone data for {tz} on this PC and no fallback rule: install tzdata")
    return ("us", FALLBACK[tz])


def _us_offset(at, std):
    """hours from UTC at the aware time `at` in a US zone of standard offset `std`: daylight time (std + 1) from 02:00 local
    standard time on the second Sunday of March to 02:00 local daylight time on the first Sunday of November (the US rule since 2007; core watch
    checked it against Python's zoneinfo every 30 minutes from 2019 to 2030: no day differed)"""
    u = at.astimezone(dt.timezone.utc); y = u.year
    def sunday(month, n):
        d = dt.date(y, month, 1); d += dt.timedelta(days=(6 - d.weekday()) % 7)
        return d + dt.timedelta(weeks=n - 1)
    start = dt.datetime.combine(sunday(3, 2), dt.time(2), dt.timezone.utc) - dt.timedelta(hours=std)
    end = dt.datetime.combine(sunday(11, 1), dt.time(2), dt.timezone.utc) - dt.timedelta(hours=std + 1)
    return std + 1 if start <= u < end else std


def _local_day(at, zone):
    if isinstance(zone, tuple): return (at.astimezone(dt.timezone.utc) + dt.timedelta(hours=_us_offset(at, zone[1]))).strftime("%Y-%m-%d")
    return at.astimezone(zone).strftime("%Y-%m-%d")


def merge(decisions, path=None, tz="America/Chicago", zoneinfo=True):
    """EM's decisions from the page (its db documents: {id, kind, decision, note, element, version, file, line, figure, figures,
    cls, at}) into lib/approvals.csv: one row per page record, the newest decision kept; a record EM undid (absent here) is left
    as it is, so an undo after a merge needs a new decision. Returns (added, changed)."""
    path = path or PATH
    try: have = list(csv.DictReader(open(path, encoding="utf-8")))
    except OSError: have = []
    by = {r.get("record"): r for r in have}
    added = changed = 0
    zone = _zone(tz, zoneinfo)
    for d in decisions:
        if d.get("decision") not in ("yes", "no") or not d.get("element") or not d.get("figure"): continue
        at = dt.datetime.fromisoformat(str(d.get("at", "")).replace("Z", "+00:00")) if d.get("at") else dt.datetime.now(dt.timezone.utc)
        day = _local_day(at, zone)
        row = {"element": d["element"], "version": d.get("version", ""), "kind": d.get("kind", "figure"), "file": d.get("file", ""),
               "line": str(d.get("line", "")), "class": d.get("cls", ""), "figures": str(d.get("figures", 1)), "decision": d["decision"],
               "figure": d["figure"].strip(), "note": (d.get("note") or "").replace("\n", " ").strip(), "signed": f"· EM {day}",
               "record": d.get("id", "")}
        old = by.get(row["record"])
        if old is None: have.append(row); by[row["record"]] = row; added += 1
        elif any((old.get(k) or "") != row[k] for k in ("decision", "note", "figure", "version")): old.update(row); changed += 1
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n"); w.writeheader()
        for r in have: w.writerow({k: r.get(k, "") for k in FIELDS})
    return added, changed
