"""Generic elements (EM, 2026-11-07: "yes"): a product class built as our own vendor-neutral design of an ETIM 10.0 class, so the
lanes build it unattended instead of waiting for a maker's datasheet read with EM.

An element is generic when its BASELINE starts "our own design: generic <class> (ETIM 10.0 <ECnnnnnn>)", or, for a product class
ETIM has no class for (servo drives and motors, steppers), "... (no ETIM class; <standard> values)" (NO_CLASS below). Its ETIM features
(lib/standards/etim/class-features.csv) are the class's definition: spec.md states each one under "## Class values", with the
value this element is designed to, or "not stated". They are design inputs, not Assumptions. Interfaces still come from the
standards and contracts on file (a fit not on file stays NOT ON FILE with its class); sizes no standard fixes are design choices;
no vendor names; a safety-function class still needs EM's safety sign-off (OPERATING.md 12, 13).

The work list: lib/inventory.csv rows first (own_design "generic" marks a product class built generic), then the ETIM classes
on file that no inventory row and no element covers, machine core (tier 1) first, each to the lane its domain gives.
"""
import csv, os, re

from . import library

LIB = os.path.dirname(library.ELEMENTS)
ETIM = os.path.join(LIB, "standards", "etim")
LANE = {"control": "elec", "sensing": "elec", "wiring": "elec", "enclosure-thermal": "elec", "fluid": "pneu", "mechanical": "mech",
        "handling": "mech"}
# building-trade and tool classes ETIM files in the machine groups: not elements a machine is built from
TRADE = re.compile(r"\bnail|dowel|wall plug|all-purpose plug|hammer-in plug|cavity fixing|toggle fixing|concrete|masonry|\broof|facade|"
                   r"sandwich panel|\bwood|plasterboard|insulation (?:material|board|tape)|assortment|\bset\b|\(compressed air\)|\(battery\)|"
                   r"\(electric\)|domestic|\bbell\b|door communication|antenna|photovoltai|underground|air termination|lightning|"
                   r"earth electrode|earthing rod|foundation earth|chimney|subfloor|ceiling|skirting|wall duct|installation column|furniture|"
                   r"garden|kitchen|bathroom|sanitary|curtain rail|gutter|\btile|anchor(?! bolt)|anti-theft|water softener|potable|drinking|"
                   r"radiator|boiler|tap water|heating|solar|shower|toilet|flush|documentation|software|licen[cs]e|faucet|manhole|street|"
                   r"heat pump|frost|steam|sewage|drain|fire hose|fire brigade|storz|hydrant|irrigation|hydronic|compressed air (?:tool|screwdriver)", re.I)
# fluid power is what the pneu lane builds; ETIM's fluid groups are mostly building services, so a fluid class must name it
FLUID_POWER = re.compile(r"pneumat|compressed air|hydraul|solenoid|cylinder|vacuum|air (?:filter|dryer|treatment|preparation)|"
                         r"pressure (?:regulat|reduc|switch|gauge|relief)|regulator|lubricator|manifold|distribution block|silencer|"
                         r"check valve|non-return|ball valve|needle valve|throttle|flow control|quick coupling|push-in|hose|tube|fitting|"
                         r"o-ring|seal|compressor|gripper|suction|ejector|coupling", re.I)
# the order a lane works through ETIM's groups: what a machine is mostly made of first (core chat 2026-11-07)
ORDER = {"elec": ["EG020048", "EG020090", "EG021002", "EG000019", "EG000020", "EG000024", "EG020099", "EG020088", "EG000058", "EG000012",
                  "EG000035", "EG000011", "EG020050", "EG000001", "EG000004", "EG021009", "EG000021", "EG000053"],
         "mech": ["EG020017", "EG020054", "EG019710", "EG020045", "EG021006", "EG021005", "EG010340", "EG010320"],
         "pneu": ["EG015640", "EG015410", "EG020014", "EG020069", "EG020071", "EG015910", "EG015540", "EG015510", "EG015520"]}
EC = re.compile(r"\bEC\d{6}\b")


def classes(path=None):
    """lib/standards/etim/classes.csv rows, each with `lane` (from its domain) and `trade` (a building-trade or tool class)"""
    try: rows = list(csv.DictReader(open(path or os.path.join(ETIM, "classes.csv"), encoding="utf-8")))
    except OSError: return []
    for r in rows:
        r["lane"] = LANE.get(r.get("domain", ""), "")
        r["trade"] = bool(TRADE.search(r.get("description", ""))) or (r["lane"] == "pneu" and not FLUID_POWER.search(r.get("description", "")))
    return rows


def built_classes(elements=None):
    """the ETIM classes the elements on file already are, read from each element.py's BASELINE line"""
    out = {}
    d = elements or library.ELEMENTS
    for eid in sorted(os.listdir(d)):
        p = os.path.join(d, eid, "element.py")
        try: text = open(p, encoding="utf-8", errors="replace").read()
        except OSError: continue
        for ln in text.splitlines():
            if ln.lstrip().startswith("BASELINE"):
                for m in EC.finditer(ln): out.setdefault(m.group(0), []).append(eid)
    return out


# core watch 2026-11-12 (2.d, pneu idle r87 to r89): `build.py inventory <lane>` listed the ETIM classes only when the lane had fewer
# rows left than it shows (n), so a lane whose rows all wait on a document saw no class to build and idled three rounds with 187
# fluid-power classes on file. The list always shows at least ALWAYS classes, after the rows.
ALWAYS = 3


def etim_shown(rows_left, n=6):
    """how many ETIM classes `build.py inventory <lane>` lists after a lane's next rows: the rest of n, and never fewer than ALWAYS
    (a row may wait on a document or on EM; the classes are the next work then, OPERATING.md 12)"""
    return max(n - rows_left, ALWAYS)


def next_classes(lane, n=6, rows=None, built=None):
    """the next ETIM classes for a lane to build generic: not in the inventory, not built, not a trade class; tier 1 first, then
    the lane's group order (ORDER), then by name"""
    rows = classes() if rows is None else rows
    built = built_classes() if built is None else built
    order = {g: i for i, g in enumerate(ORDER.get(lane, []))}
    todo = [r for r in rows if r["lane"] == lane and not r["trade"] and not (r.get("inventory") or "").strip() and r["class"] not in built]
    todo.sort(key=lambda r: (int(r.get("tier") or 2), order.get(r["group"], 99), r["group"], r["description"]))
    return todo[:n] if n else todo


SAY_GENERIC = re.compile(r"^[\s*_`\"'(]*(?:our\s+)?own\s+design\s*:\s*generic\b", re.I)
# ETIM 10.0 is thin on motion (servo drives and motors, steppers, encoders, linear stages): a generic element of a product class
# ETIM has no class for says so and names the standard whose rating data its Class values follow, e.g.
# "(no ETIM class; IEC 61800-2 values)" for a servo drive, "(no ETIM class; IEC 60034-1 values)" for a servo motor (EM 2026-11-08)
NO_CLASS = re.compile(r"\(\s*no\s+ETIM\s+class\s*;\s*(?:IEC|ISO|EN|IEEE|NEMA|ASME|ANSI|DIN|JIS|UL)\s*[\w.\-/ ]+?\s+values\s*\)", re.I)


def check(baseline, spec, known=None):
    """GEN-010: a generic element names an ETIM class on file and states its class values. [] when it passes or isn't generic."""
    if not SAY_GENERIC.search(baseline or ""): return []
    # on file = in classes.csv or with its features in class-features.csv (the same ETIM 10.0 release): 14 inventory rows name a class
    # the classes subset leaves out (its 66 groups) whose features are on file, and GEN-010 held them (request pneu-5, gauge-p)
    known = ({r["class"] for r in classes()} | set(features())) if known is None else known
    ids = EC.findall(baseline or "")
    out = []
    if not ids and NO_CLASS.search(baseline or ""): pass                 # ETIM has no class for it: the standard named defines its values
    elif not ids: out.append("a generic element's BASELINE names no ETIM class (ETIM 10.0 ECnnnnnn), nor 'no ETIM class; <standard> values'")
    elif not any(i in known for i in ids): out.append(f"{', '.join(ids)}: not an ETIM class on file (lib/standards/etim/classes.csv, or its features in class-features.csv)")
    if not re.search(r"^#+\s*Class values\b", spec or "", re.M | re.I):
        out.append("no '## Class values' section in spec.md: each ETIM feature of the class with the value it is designed to, or 'not stated'")
    return out


_FEAT = {}
EF = re.compile(r"\bEF\d{6}\b")


def features(path=None):
    """{class: [(EF code, description)]} from lib/standards/etim/class-features.csv (the subset on file), read once"""
    p = path or os.path.join(ETIM, "class-features.csv")
    if p not in _FEAT:
        d = {}
        try:
            for r in csv.DictReader(open(p, encoding="utf-8")): d.setdefault(r["class"], []).append((r["feature"], r.get("description", "")))
        except OSError: pass
        _FEAT[p] = d
    return _FEAT[p]


def _norm(s): return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def rating_rows(baseline, rows, feats=None, names=None):
    """GEN-010, the ratings half (escape, pneu-r52, chiller 1.0 finding 1): a ratings.csv row with status "generic design" is a class
    value only when it traces to the class on file: its source names one of the class's features (EF code, or the feature's name;
    the property's own name counts, max_tensile_force for "Max. tensile force"), or quotes the class's own name or a synonym in
    quotes ("'Pressureless storage tank'"). A rating the checks read with none of these is a class A figure (OPERATING.md 6), to
    be marked "assumption", or NOT ON FILE (A). A class whose features are not in the subset on file is not judged here (request
    pneu-4: its values stand until the features come). "(no ETIM class; <standard> values)": the source names that standard.
    `feats` {class: [(EF, name)]}, `names` {class: [the class's name and synonyms]}; [] when it passes or isn't generic."""
    if not SAY_GENERIC.search(baseline or ""): return []
    feats = features() if feats is None else feats
    if names is None:
        names = {r["class"]: [r.get("description", "")] + [x.strip() for x in (r.get("synonyms") or "").split(";")] for r in classes()}
    ids = EC.findall(baseline or "")
    std = NO_CLASS.search(baseline or "")
    std = re.sub(r"(?i)^\(\s*no\s+ETIM\s+class\s*;\s*|\s+values\s*\)$", "", std.group(0)).strip() if std and not ids else ""
    out = []
    for r in rows or []:
        if (r.get("status") or "").strip().lower() != "generic design": continue
        src, prop = r.get("source") or "", r.get("property") or ""
        if std:
            if _norm(std) not in _norm(src): out.append(f"ratings.csv {prop}: status 'generic design' but its source names no {std} value")
            continue
        known = [i for i in ids if feats.get(i)]
        if not known: continue                                               # the class's features are not on file (pneu-4)
        codes = {c for i in known for c, _ in feats[i]}
        fnames = [_norm(n) for i in known for _, n in feats[i] if len(_norm(n)) >= 6]
        quoted = [_norm(a or b) for a, b in re.findall(r"'([^']{4,})'|\"([^\"]{4,})\"", src)]
        cnames = {_norm(n) for i in ids for n in names.get(i, []) if n}
        ns, np_ = _norm(src), _norm(prop.replace("_", " "))
        if (codes & set(EF.findall(src))) or any(f in ns or f == np_ for f in fnames) or any(q in cnames for q in quoted): continue
        out.append(f"ratings.csv {prop} = {r.get('value', '')} {r.get('unit', '')}".rstrip() + f": status 'generic design' but its source names "
                   f"no feature of {', '.join(known)} on file (EF code or name) nor the class's own name: a rating with no class value behind "
                   "it is class A, mark it 'assumption' (Assumption (A) in spec.md, for EM) or NOT ON FILE (A)")
    return out
