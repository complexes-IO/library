"""Unified inch screw threads on file (lib/standards/un-threads.csv): UNC and UNF, No. 0 to 1 inch, from FED-STD-H28/2B
Table II.A.3 (a public US federal standard; EM, 2026-11-07: inch parts beside metric ones, one library, each element naming its
series). load() gives the rows; check() holds every row to the thread form's own arithmetic, so a misread figure fails:
  basic minor diameter D1 = D - 1.082532 P (P = 1/tpi): the class 1B/2B minimum minor diameter, to the table's rounding
  percent of thread = 100 (D - d) / (2 x 0.649519 P), 0.649519 P being 0.75H (H = 0.866025 P), its 20.2.3: both limits, to 0.1
  the recommended hole before threading lies within the minor limits, its maximum being the maximum minor diameter (its 30.1)
"""
import csv, os

from . import library

PATH = os.path.join(library.ROOT, "standards", "un-threads.csv")
NUM = ("D_in", "tpi", "minor_min_in", "pct_min", "minor_max_in", "pct_max", "hole_min_in", "hole_max_in")


def load(path=None):
    """{size: row} with the numbers as floats and the figures' text kept under '<field>_text'"""
    out = {}
    with open(path or PATH, encoding="utf-8") as f:
        for r in csv.DictReader(ln for ln in f if not ln.startswith("#")):
            for k in NUM: r[k + "_text"] = r[k]; r[k] = float(r[k])
            out[r["size"]] = r
    return out


def _half_unit(text):
    """half a unit of the last decimal place the table printed: its rounding"""
    return 0.5 * 10 ** -len(text.split(".")[1]) if "." in text else 0.5


def check(rows=None):
    """[(size, problem)] for every figure the thread form's arithmetic refutes; [] when the table holds"""
    rows = load() if rows is None else rows
    out = []
    for size, r in rows.items():
        D, P = r["D_in"], 1.0 / r["tpi"]
        basic = D - 1.082532 * P
        if abs(r["minor_min_in"] - basic) > _half_unit(r["minor_min_in_text"]) + 1e-6:
            out.append((size, f"minor_min {r['minor_min_in_text']} is not the basic minor diameter D - 1.082532P = {basic:.4f}"))
        for d, p in (("minor_min_in", "pct_min"), ("minor_max_in", "pct_max")):
            pct = 100 * (D - r[d]) / (1.299038 * P)
            if abs(pct - r[p]) > 0.1 + 1e-9:
                out.append((size, f"{p} {r[p + '_text']} disagrees with {d} {r[d + '_text']} ({pct:.1f} % of 0.75H)"))
        if r["hole_max_in"] != r["minor_max_in"]: out.append((size, "hole_max is not the maximum minor diameter (30.1)"))
        if not r["minor_min_in"] <= r["hole_min_in"] < r["hole_max_in"]: out.append((size, "hole_min is not within the minor limits"))
        if not r["minor_min_in"] < r["minor_max_in"]: out.append((size, "minor_min is not below minor_max"))
    return out
