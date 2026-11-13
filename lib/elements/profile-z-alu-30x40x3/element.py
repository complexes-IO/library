#!/usr/bin/env python3
"""profile-z-alu-30x40x3: generic aluminium Z-profile, our own vendor-neutral design of the ETIM 10.0 class EC012295 (Z-profile,
aluminium), built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name, after
profile-u-pvc-25x25 and the classes skipped in mech-r142). An extruded aluminium Z-section: a bottom flange 30 wide to one side of an
upright web, a top flange 30 wide to the other side, total height 40, flanges and web 3, sharp corners, anodised. Plain stock, cut to
length (the `length` parameter; a parameter stays out of the id, OPERATING.md 6); no holes: a host that bolts it drills its own and
declares them in its own features.csv. An extruded aluminium Z-section's sizes are fixed by no dimensional standard on file (EN 755-9
gives an extrusion's tolerances only, not on file and not claimed), so every size is a design choice. The class values (spec.md,
"Class values") are design inputs; the class has no load feature, so none is claimed, and nothing moves. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "profile-z-alu-30x40x3", "1.0", "rail"
TITLE = "Z-profile, aluminium, generic, extruded Z-section, flanges 30 and 30, height 40, thickness 3, sharp corners, anodised, plain (no holes), cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Z-profile, aluminium (ETIM 10.0 EC012295), an extruded Z-section, top and low flanges 30 wide, "
            "height 40, thickness 3, sharp corners, anodised, plain stock; class values are design inputs (spec.md); every size a design "
            "choice; no load claim; no vendor file opened")
ORIGIN = ("run start x = 0, the web's centre plane y = 0, the low flange's underside z = 0; the run along +x, the low flange to -y "
          "(z 0 to 3), the web upright, the top flange to +y (z 37 to 40)")
COMMAND = "ZPROFALU"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

WT, WL, H = 30.0, 30.0, 40.0                 # width top base, width low base (y, outside, each over the web), height (z): design choices
T = 3.0                                      # thickness of flanges and web: design choice (class feature Thickness)
YL = -WL + T / 2                             # -28.5: the low flange's free edge
YT = WT - T / 2                              # 28.5: the top flange's free edge
CW = WT - T                                  # 27: each flange's outstand past the web
CH = H - T                                   # 37: the web's height from either flange's outer face to the other's inner face
MAT = "M-ALU-ANOD"                           # anodised aluminium (lib/materials.csv al-6063; no temper claimed)

assert T <= 3.0                                                              # the flanges' free edges: "short" edges, skipped by the gate
assert WL - T >= 8.0 and CW >= 8.0 and H - 2 * T >= 8.0                      # every other end-face edge clears the 3 to 7 mm free-corner trap (mech-r69)
AREA = WL * T + WT * T + (H - 2 * T) * T
assert abs(AREA - 282.0) < 1e-9                                              # by hand: 30 x 3 + 30 x 3 + 34 x 3 = 282 mm²
assert abs(AREA - ((YT - YL) * H - (WT - T) * CH - (WL - T) * CH)) < 1e-9    # = 57 x 40 − 27 x 37 − 27 x 37


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, YL, 0, L, YT - YL, H)                                               # the section's bounding box: one box ...
    P.cutbox(MAT, -1.0, T / 2, -1.0, L + 2.0, CW + 1.0, CH + 1.0, body)                     # ... less the space under the top flange (+y, z up to 37)
    P.cutbox(MAT, -1.0, YL - 1.0, T, L + 2.0, WL - T + 1.0, CH + 1.0, body)                 # ... and over the low flange (-y, z from 3): one Z solid
    P.collider("flange-low", 0, YL, 0, L, WL, T)
    P.collider("web", 0, -T / 2, T, L, T, H - 2 * T)
    P.collider("flange-top", 0, -T / 2, H - T, L, WT, T)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 20), height=80)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
