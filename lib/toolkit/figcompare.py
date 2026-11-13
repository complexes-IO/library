"""Brief figures against the gate's measured build (core watch 2026-11-06; escape group 6, lib/requests/core/escapes.md: the reviewer's
bench-1800-1.0:1, disc-3p-30a-1.3:4, overload-9a-1.1:2; the library's round-11 return, section 4).

acad-gate.py's measure_compare matched each figure of references/measure*.md to the nearest overall extent on any axis, or to any
side of any solid, within 2 mm, whatever the figure was: 83.7 deep passed against 84.9, a 30.2 shaft passed against a 32.0 hub, a
trip current of 7.0 A passed against a 7.0 mm solid, and a 69.1 x 69.1 plate passed twice on the x extent alone. A figure is now
matched only to the feature it names:

  kind(feature)        "not a length"   the feature names a current, voltage, torque, pressure, temperature, power, count ...
                       "envelope"       the feature starts with width / height / depth / thickness, or overall / envelope
                                        (then the next axis word, if any): compared with the build's overall extent. "length" alone
                                        is not (a duct's "length as supplied" is a parameter), "overall length" is
                       "local"          also any feature measured from or to a part of the element (above, below, from, behind,
                                        across, between, to the, a datum, a centre, "as supplied", "per"): a part, not the envelope
                       "local"          anything else (a hole, a thread, a body, a foot, a pattern): its solid is not named in the
                                        gate's data, so it is reported "not located", never "found"
  axis(feature)        0 (x: width), 1 (y: depth, thickness), 2 (z: height), or None (length, overall: any axis)
  tol(v)               ISO 2768-1 class m for the figure's size (lib/standards/general-tolerances.csv), the library's default
                       when a figure carries no tolerance
  compare(figs, ext)   figs: the gate JSON's measure_compare rows (feature, values, not_on_file); ext: the STEP's [x, y, z].
                       One result per row: status "found" | "miss" | "not located" | "not a length" | "not on file" |
                       "not built" (the row's feature or source says "not built": a configuration the default build is not,
                       as contactor-9a-1no1nc's "depth alone" beside its fitted front block; the lane writes it in measure.md's row).
                       An envelope row with several values on one axis (two readings, 59.6 / 60.0) is found when any of them is;
                       a row with no named axis takes the nearest extent.
  misses(rep)          the "miss" rows of a gate JSON: what holds the element at station 6 (toolkit/line.py tools_check).
"""
import csv, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
TOL_CSV = os.path.join(HERE, "..", "standards", "general-tolerances.csv")

NOT_LENGTH = re.compile(r"\b(current|curr|amp\w*|voltage|volt\w*|torque|pressure|temperature|temp|power|watt\w*|kw|hz|frequency|"
                        r"rating|count|qty|quantity|number of|mass|weight|speed|rpm|time|angle|ip\d\d|awg|ga|gauge)\b", re.I)
AXES = {"width": 0, "wide": 0, "depth": 1, "deep": 1, "thickness": 1, "thick": 1, "height": 2, "high": 2, "tall": 2, "length": None}
NOT_BUILT = re.compile(r"\bnot built\b", re.I)
PART_OF = re.compile(r"\b(above|below|from|behind|across|between|to the|datum|centre|center|centreline|centerline|as supplied|per)\b", re.I)
LEAD = re.compile(r"^\s*(overall|envelope)?\s*,?\s*(width|wide|depth|deep|thickness|thick|height|high|tall|length)?\b", re.I)


def _tol_rows():
    rows = []
    try:
        for r in csv.reader(open(TOL_CSV, encoding="utf-8")):
            if not r or r[0].startswith("#") or r[0] == "class": continue
            if r[0] == "m": rows.append((float(r[1]), float(r[2]), float(r[3])))
    except OSError: pass
    return rows


_TOL = _tol_rows()


def tol(v):
    """ISO 2768-1 m for a figure of size v (below 0.5 mm: 0.1; above the table: its last row)"""
    v = abs(v)
    for lo, hi, t in _TOL:
        if lo < v <= hi: return t
    return _TOL[-1][2] if _TOL and v > _TOL[-1][1] else 0.1


def kind(feature):
    f = re.sub(r"\([^)]*\)", "", feature or "")
    if NOT_LENGTH.search(f): return "not a length"
    if PART_OF.search(f): return "local"
    m = LEAD.match(f)
    if m and m.group(1): return "envelope"
    if m and m.group(2) and m.group(2).lower() != "length": return "envelope"
    return "local"


def axis(feature):
    m = LEAD.match(re.sub(r"\([^)]*\)", "", feature or ""))
    return AXES.get(m.group(2).lower()) if m and m.group(2) else None


def compare(figs, ext):
    out = []
    for fg in figs:
        feat, vals = fg.get("feature", ""), [float(v) for v in fg.get("values", [])]
        r = {"feature": feat, "values": vals, "source": str(fg.get("source", ""))}
        if fg.get("not_on_file"): r["status"] = "not on file"
        elif NOT_BUILT.search(feat + " " + str(fg.get("source", ""))): r["status"] = "not built"
        else:
            k = kind(feat)
            if k != "envelope" or not ext: r["status"] = "not located" if k == "local" or not ext else k
            else:
                a = axis(feat); best = None
                for v in vals:
                    cand = [(abs(ext[a] - v), a)] if a is not None else [(abs(e - v), i) for i, e in enumerate(ext)]
                    d, i = min(cand)
                    if best is None or d - tol(v) < best[0] - best[3]: best = (d, i, v, tol(v))
                d, i, v, t = best
                r.update(status="found" if d <= t else "miss", axis="xyz"[i], extent=round(ext[i], 3), figure=v, diff=round(d, 3), tol=t)
        out.append(r)
    return out


def misses(rep):
    """the rows of a gate JSON that hold the element: an envelope figure the build misses on its own axis beyond ISO 2768-1 m"""
    if not rep: return []
    ext = (rep.get("step") or {}).get("extents") or (rep.get("acad_extents") or {}).get("size")
    figs = [dict(c, not_on_file=c.get("not_on_file", False)) for c in rep.get("measure_compare") or []]
    return [r for r in compare(figs, ext) if r["status"] == "miss"]


def say(r):
    return (f"brief figure '{r['feature']}' {r['figure']:g} not on the build's {r['axis']} extent {r['extent']:g} "
            f"(diff {r['diff']:g} > {r['tol']:g}, ISO 2768-1 m)")
