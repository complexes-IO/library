"""Derived figures (EM 2026-11-09: "all engineering is mathematics made visible ... let's make sure we are not stopping for data that is
derived from known formulas or based in standards which we can derive to by math"). A figure that a standard's formula gives from
figures on file is derived, not NOT ON FILE: the lane computes it here, writes the value with 'derived: <call> (<standard, clause>)'
as its source, and nothing waits on EM. Every function names its formula and its standard; the selftest holds each to a published
worked value. Tables a standard gives without a formula (ISO 6020-2 mounting dimensions, ISO 6149 ports, CGA V-1 outlets) are not
here: they are documents wanted (lib/standards/wanted.md, build.py wanted).
    python lib/build.py derive thread M8            -> the ISO metric thread M8 (coarse) with its 6g / 6H limits
    python lib/build.py derive thread M8x1          -> fine pitch
    python lib/build.py derive motor 7.5 460        -> a three-phase motor's full-load current from its power
    python lib/build.py derive cylinder 40 22 160 22 -> force and speed of a cylinder (bore, rod, bar, l/min)
    python lib/build.py derive resistance copper 23.4 8.84 -> R of a bar (material, length mm, area mm²)
    python lib/build.py derive torque M8 8.8 dw=13 [mu=0.12] [muk=0.12] [nu=0.7] [dh=9.0] -> a screw's preload and tightening torque
"""
import math

# ISO 261 coarse pitches (the general purpose series; public, the standard's table 1)
COARSE = {1.6: 0.35, 2: 0.4, 2.5: 0.45, 3: 0.5, 4: 0.7, 5: 0.8, 6: 1.0, 8: 1.25, 10: 1.5, 12: 1.75, 16: 2.0, 20: 2.5, 24: 3.0, 30: 3.5, 36: 4.0, 42: 4.5, 48: 5.0}
# resistivity at 20 °C, Ω·m (IEC 60028 for annealed copper: 1/58 Ω·mm²/m = 1.7241e-8; aluminium IEC 60121 2.8264e-8)
RHO = {"copper": 1.7241e-8, "aluminium": 2.8264e-8, "brass": 7.0e-8, "steel": 1.6e-7}
# IE3 efficiency, 4-pole, 60 Hz, IEC 60034-30-1 Table 3 (public): kW -> %
IE3_4P_60HZ = {0.75: 85.5, 1.1: 86.5, 1.5: 86.5, 2.2: 89.5, 3.7: 89.5, 5.5: 91.7, 7.5: 91.7, 11: 92.4, 15: 93.0, 18.5: 93.6, 22: 93.6, 30: 94.1, 37: 94.5, 45: 95.0, 55: 95.4, 75: 95.4}


def thread(d, P=None, grade_ext="6g", grade_int="6H"):
    """ISO metric thread: basic profile (ISO 68-1), limits (ISO 965-1 formulas). d, P in mm. Returns a dict of mm figures with the
    formula each came from. ISO 68-1: H = (√3/2) P; d2 = d − 0.649519 P (3/8 H × 2); d1 = d − 1.082532 P (5/8 H × 2); d3 = d − 1.226869 P
    (external minor, 17/24 H). ISO 965-1 clause 10 (tolerances, µm): Td2(6) = 90 P^0.4 d^0.1 (external pitch diameter); TD2(6) =
    1.32 Td2(6) (internal); TD1(6) = 230 P^0.7 for P ≥ 1, 433 P − 190 P^1.22 for P ≤ 0.8 (internal minor); Td(6) = 180 ∛P² − 3.15 / √P
    (external major); fundamental deviations es(g) = −(15 + 11 P), EI(H) = 0. The standard rounds its tabulated values to the R40
    series (M8: Td 212 for a computed 206), so a figure here can differ from the table by a few µm: where the table is on file it
    governs; 6g / 6H limits of M8 and M6 held in the selftest to the published values within 0.01 mm."""
    if P is None:
        if d not in COARSE: raise ValueError(f"M{d}: coarse pitch not in ISO 261's general purpose series on file; give the pitch")
        P = COARSE[d]
    H = math.sqrt(3) / 2 * P
    d2 = d - 0.649519 * P; d1 = d - 1.082532 * P; d3 = d - 1.226869 * P
    TD1 = ((230 * P ** 0.7) if P >= 1 else (433 * P - 190 * P ** 1.22)) / 1000
    Td2 = (90 * P ** 0.4 * d ** 0.1) / 1000; TD2 = 1.32 * Td2; Td = (180 * P ** (2 / 3) - 3.15 / math.sqrt(P)) / 1000
    es = -(15 + 11 * P) / 1000 if grade_ext.endswith("g") else 0.0
    out = dict(d=d, P=P, H=round(H, 4), d2=round(d2, 4), d1=round(d1, 4), d3=round(d3, 4),
               ext=dict(grade=grade_ext, d_max=round(d + es, 4), d_min=round(d + es - Td, 4), d2_max=round(d2 + es, 4), d2_min=round(d2 + es - Td2, 4), d3_max=round(d3 + es, 4)),
               int=dict(grade=grade_int, D1_min=round(d1, 4), D1_max=round(d1 + TD1, 4), D2_min=round(d2, 4), D2_max=round(d2 + TD2, 4)),
               tap_drill=round(d - P, 2),
               source=f"derived: derive.thread({d}, {P}) (ISO 68-1 basic profile; ISO 965-1 clause 10 formulas, {grade_ext} / {grade_int}; ISO 261 pitch)")
    return out


def motor_current(P_kW, V, eta=None, pf=0.85, phases=3):
    """a motor's full-load current from its rated output: I = P / (√3 · V · η · pf) (three-phase) or P / (V · η · pf). η from IEC
    60034-30-1 Table 3 (IE3, 4-pole, 60 Hz) when not given; pf 0.85 is a design value (the nameplate's when on file). NEC 430.6(A)(1)
    sizes conductors and protection from Table 430.250 instead of the nameplate; that table is a document, not a formula."""
    if eta is None:
        if P_kW not in IE3_4P_60HZ: raise ValueError(f"{P_kW} kW: no IE3 4-pole 60 Hz efficiency on file for that rating; give eta")
        eta = IE3_4P_60HZ[P_kW] / 100
    I = P_kW * 1000 / ((math.sqrt(3) if phases == 3 else 1) * V * eta * pf)
    return dict(I=round(I, 2), eta=eta, pf=pf, source=f"derived: derive.motor_current({P_kW}, {V}, eta={eta}, pf={pf}) (P = √3 V I η cosφ; η IEC 60034-30-1 Table 3 IE3 4-pole 60 Hz; pf a design value)")


def cylinder(bore, rod, p_bar, q_lpm=None):
    """force and speed of a double-acting cylinder: A = π bore² / 4, A_r = A − π rod² / 4 (mm²); F = p · A (p in Pa = bar × 1e5);
    v = Q / A (Q in m³/s). The arithmetic is the formula, by definition of pressure and flow; no standard's clause is cited (request pneu-13 4a:
    ISO 4413 is not in lib/standards/sources.csv, so its clause could not be checked)."""
    A = math.pi * bore ** 2 / 4; Ar = A - math.pi * rod ** 2 / 4
    F = p_bar * 1e5 * A * 1e-6; Fr = p_bar * 1e5 * Ar * 1e-6
    out = dict(A_mm2=round(A, 1), Ar_mm2=round(Ar, 1), F_kN=round(F / 1000, 2), F_t=round(F / 9806.65, 2), Fr_kN=round(Fr / 1000, 2),
               source=f"derived: derive.cylinder({bore}, {rod}, {p_bar}{', ' + str(q_lpm) if q_lpm else ''}) (F = p A; v = Q / A)")
    if q_lpm:
        q = q_lpm / 60 / 1000; out["v_out_m_s"] = round(q / (A * 1e-6), 3); out["v_in_m_s"] = round(q / (Ar * 1e-6), 3)
    return out


def resistance(material, L_mm, A_mm2):
    """R = ρ L / A of a conductor (IEC 60028 copper 1/58 Ω·mm²/m at 20 °C). Returns Ω."""
    rho = RHO[material]
    R = rho * (L_mm / 1000) / (A_mm2 * 1e-6)
    return dict(R=R, R_uohm=round(R * 1e6, 2), source=f"derived: derive.resistance('{material}', {L_mm}, {A_mm2}) (R = ρL/A; ρ {rho:.4e} Ω·m at 20 °C, IEC 60028)")


def proof_class(prop_class):
    """a steel property class's nominal strengths from its designation (ISO 898-1 clause 4, the designation system): "a.b" gives the
    nominal tensile strength R_m,nom = 100 a MPa and the nominal yield (lower yield or 0.2 % proof strength) R_eL,nom = R_m,nom × b / 10.
    The designation is the formula; the class's tabulated proof stress S_p and minimum values are a table (ISO 898-1 Table 3), not here."""
    m = __import__("re").fullmatch(r"(\d{1,2})\.(\d)", str(prop_class).strip())
    if not m: raise ValueError(f"property class {prop_class!r}: only the ISO 898-1 steel designations a.b read by formula (stainless ISO 3506 classes are a table)")
    Rm = 100 * int(m.group(1)); Re = Rm * int(m.group(2)) / 10
    return dict(Rm_nom=Rm, ReL_nom=Re)


def stress_area(d, P=None):
    """tensile stress area A_s = π/4 · ((d2 + d3) / 2)², d3 = d1 − H/6 (ISO 898-1, the stress area formula; d2, d3 from derive.thread)."""
    t = thread(d, P)
    return math.pi / 4 * ((t["d2"] + t["d3"]) / 2) ** 2, t


def clearance_hole(d, fit="medium"):
    """the ISO 273 clearance hole's nominal size for M<d> from lib/standards/holes.csv (fine / medium / coarse), or None."""
    import csv, os
    f = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "standards", "holes.csv")
    with open(f, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(l for l in fh if not l.startswith("#")):
            if r["kind"] == "clearance" and r["size"] == f"M{d:g}" and r["note"] in {"fine": ("H12",), "medium": ("H13",), "coarse": ("H14",)}[fit]:
                return float(r["d_min"])
    return None


def torque(d, P=None, prop_class="8.8", mu_G=0.12, mu_K=0.12, nu=0.7, d_w=None, d_h=None):
    """a metric screw's assembly preload and tightening torque (request mech-7, 2026-11-10).
    F_M = ν · R_eL,nom · A_s: the preload as the design's fraction ν of the nominal yield load (R_eL,nom from the property class's
    designation, ISO 898-1 clause 4; A_s ISO 898-1's stress area formula). M_A = F_M · (0.16 P + 0.58 μ_G d2 + μ_K D_Km / 2), the
    torque-tension relation of ISO 16047 / VDI 2230 Part 1, with D_Km = (d_w + d_h) / 2 the mean bearing diameter under the head or nut.
    Design inputs, written into the source so the lane cites them: ν, μ_G (thread friction), μ_K (bearing friction), d_w (the bearing
    face's outer diameter: the head's or nut's, from its standard when on file, else the element's own face, a design figure). d_h
    defaults to the ISO 273 medium clearance hole on file (lib/standards/holes.csv). No figure here is read from a table not on file."""
    if d_w is None: raise ValueError("give d_w, the bearing face's outer diameter under the head or nut (mm): its standard's when on file, else the element's own face (design)")
    if not 0 < nu <= 1: raise ValueError(f"nu {nu}: the preload is a fraction of the nominal yield load, 0 < nu <= 1")
    pc = proof_class(prop_class); As, t = stress_area(d, P)
    if d_h is None:
        d_h = clearance_hole(d)
        if d_h is None: raise ValueError(f"M{d:g}: no ISO 273 clearance hole on file; give d_h")
    if d_w <= d_h: raise ValueError(f"d_w {d_w} must exceed the hole d_h {d_h}")
    F = nu * pc["ReL_nom"] * As                                  # N (MPa × mm²)
    DKm = (d_w + d_h) / 2
    k_pitch, k_thread, k_head = 0.16 * t["P"], 0.58 * mu_G * t["d2"], mu_K * DKm / 2
    M = F * (k_pitch + k_thread + k_head) / 1000                 # N·m
    return dict(d=d, P=t["P"], prop_class=str(prop_class), Rm_nom=pc["Rm_nom"], ReL_nom=pc["ReL_nom"], As_mm2=round(As, 2), d2=t["d2"],
                d_w=d_w, d_h=d_h, D_Km=round(DKm, 3), F_kN=round(F / 1000, 2), M_Nm=round(M, 1),
                share=dict(pitch=round(k_pitch / (k_pitch + k_thread + k_head), 3), thread=round(k_thread / (k_pitch + k_thread + k_head), 3), head=round(k_head / (k_pitch + k_thread + k_head), 3)),
                source=(f"derived: derive.torque({d:g}, {t['P']:g}, '{prop_class}', mu_G={mu_G}, mu_K={mu_K}, nu={nu}, d_w={d_w:g}, d_h={d_h:g}) "
                        f"(M_A = F_M (0.16 P + 0.58 mu_G d2 + mu_K D_Km / 2), ISO 16047 / VDI 2230 Part 1; F_M = nu R_eL,nom A_s, ISO 898-1 clause 4 "
                        f"designation and stress area; design: nu {nu}, mu_G {mu_G}, mu_K {mu_K}, d_w {d_w:g})"))


def describe(args):
    if not args: return __doc__
    k = args[0]
    try:
        if k == "thread":
            m = args[1].upper().lstrip("M"); d, _, P = m.partition("X"); t = thread(float(d), float(P) if P else None)
            e, i = t["ext"], t["int"]
            return (f"M{t['d']:g} × {t['P']:g}: H {t['H']}  d2 {t['d2']}  d1 {t['d1']}  d3 {t['d3']}  tap drill {t['tap_drill']}\n"
                    f"  external {e['grade']}: d {e['d_min']}–{e['d_max']}  d2 {e['d2_min']}–{e['d2_max']}  d3 max {e['d3_max']}\n"
                    f"  internal {i['grade']}: D1 {i['D1_min']}–{i['D1_max']}  D2 {i['D2_min']}–{i['D2_max']}\n  {t['source']}")
        if k == "motor": r = motor_current(float(args[1]), float(args[2]), float(args[3]) if len(args) > 3 else None); return f"I = {r['I']} A (η {r['eta']}, pf {r['pf']})\n  {r['source']}"
        if k == "cylinder": r = cylinder(float(args[1]), float(args[2]), float(args[3]), float(args[4]) if len(args) > 4 else None); return "\n".join(f"  {a}: {b}" for a, b in r.items())
        if k == "torque":
            m = args[1].upper().lstrip("M"); dd, _, PP = m.partition("X"); kw = dict(a.split("=", 1) for a in args[3:] if "=" in a)
            key = {"mu": "mu_G", "muk": "mu_K", "nu": "nu", "dw": "d_w", "dh": "d_h"}
            r = torque(float(dd), float(PP) if PP else None, args[2] if len(args) > 2 else "8.8", **{key[a]: float(b) for a, b in kw.items() if a in key})
            return (f"M{r['d']:g} × {r['P']:g} class {r['prop_class']}: A_s {r['As_mm2']} mm², R_eL,nom {r['ReL_nom']:g} MPa, D_Km {r['D_Km']} mm\n"
                    f"  preload F_M {r['F_kN']} kN, tightening torque M_A {r['M_Nm']} N·m (pitch {r['share']['pitch']:.0%}, thread {r['share']['thread']:.0%}, head {r['share']['head']:.0%})\n  {r['source']}")
        if k == "resistance": r = resistance(args[1], float(args[2]), float(args[3])); return f"R = {r['R_uohm']} µΩ\n  {r['source']}"
    except (IndexError, ValueError, KeyError) as e: return f"derive {k}: {e}\n{__doc__}"
    return __doc__


STD = __import__("re").compile(r"(ISO(?:/IEC)?\s?\d{2,5}(?:-\d+)?|IEC\s?\d{4,5}(?:-\d+(?:-\d+)?)?|SAE\s?J\s?\d{3,4}|ASME\s?B\d+\.\d+(?:\.\d+)?|CGA\s?V-\d|NEC\s?(?:Table\s)?\d{3}(?:\.\d+)?|NFPA\s?\d{2,3}|UL\s?\d{3,4}[A-Z]?(?:-\d+[A-Z]?)?|DIN\s?\d{2,5}|EN\s?\d{3,5}(?:-\d+)?|ETIM\s?10\.0)")


def wanted(root=None):
    """the documents class B figures wait for, from every element's open class B lines (approvals.open_lines): {standard: [(element,
    version, file, line text)]}; lines naming no standard go under 'no standard named (the lane names one, or classes the figure)'"""
    import os, csv
    from . import approvals as AP, library, line as LN
    root = root or library.ELEMENTS; out = {}
    cat = LN._catalogue()
    for eid in library.element_ids():
        d = os.path.join(root, eid)
        try: spec = open(os.path.join(d, "spec.md"), encoding="utf-8", errors="replace").read()
        except OSError: continue
        briefs = [(n, open(os.path.join(d, "references", n), encoding="utf-8", errors="replace").read()) for n in ("measure.md", "interior.md") if os.path.isfile(os.path.join(d, "references", n))]
        rat = list(csv.DictReader(open(os.path.join(d, "ratings.csv"), encoding="utf-8"))) if os.path.isfile(os.path.join(d, "ratings.csv")) else []
        beh = open(os.path.join(d, "behaviour.csv"), encoding="utf-8").read() if os.path.isfile(os.path.join(d, "behaviour.csv")) else ""
        for L in AP.open_lines(spec, briefs, rat, beh, classes=AP.WANTED):
            stds = sorted({m.replace("  ", " ") for m in STD.findall(L["text"])}) or ["no standard named (the lane names one, or classes the figure)"]
            for st_ in stds: out.setdefault(st_, []).append((eid, cat.get(eid, {}).get("version", "?"), L["file"], L["text"][:160]))
    return out


def wanted_md(root=None):
    W = wanted(root); n = sum(len(v) for v in W.values())
    L = ["# Documents wanted · class B figures waiting for their standard (generated: python lib/build.py wanted)", "",
         "EM 2026-11-09: a figure a formula gives is derived (toolkit/derive.py), not asked for; a figure a standard tabulates waits for the",
         "document, asked for once here, not for a line of EM's per figure (DOC-005 \"source wanted\"; the board's `src`). One document",
         f"clears every line under it. {n} lines under {len(W)} headings.", ""]
    for st_, rows in sorted(W.items(), key=lambda kv: -len(kv[1])):
        L.append(f"## {st_} · {len(rows)} line(s), {len({r[0] for r in rows})} element(s)")
        for eid, ver, f, text in sorted(rows): L.append(f"- {eid} {ver} ({f}): {text}")
        L.append("")
    return "\n".join(L)
