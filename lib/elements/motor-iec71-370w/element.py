#!/usr/bin/env python3
"""motor-iec71-370w: 0.37 kW 3-phase TEFC motor, IEC 71 frame, B3 feet. Brief: references/measure.md (250.5 overall, shaft
height 71.0, fan cover Ø138, feet 136 x 90 with 112 x 90 holes, slots 7.0 along the shaft x 10.5 across (K = 7), shaft Ø14 x 30
key 5 x 5 x 25, terminal box 81 x 110, M20 entry). Every figure not from the brief is marked below with its class (spec.md, "Open
figures")."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din, sweep as SW
from toolkit.prims import Prims

ID, VERSION, CLASS = "motor-iec71-370w", "1.5", "machine"
TITLE = "3-phase induction motor 0.37 kW, IEC 71 B3, TEFC, terminal box with M20 entry"
TOOLKIT = "1.3"
BASELINE = "maker's 2-D dimension drawing p. 1 and cutsheet p. 1 (the brief, references/measure.md); IEC 60072-1 frame 71 (K = 7)"
ORIGIN = "bench machine: foot plane z = 0, front-left foot hole x = 0, y = 0; shaft axis at z = 71 pointing toward -y (drive end)"
COMMAND = "MOTOR"
PARAMS = {}
SH, FC_R = 71.0, 69.0                           # shaft height (drawing p. 1), fan cover radius (Ø138, drawing p. 1)
R = 62.0                                        # frame radius inside the cover radius: Assumption (C), housing wall (open figures)
HX, HY = 112.0, 90.0                            # foot hole pattern across (x) and along (y): drawing p. 1
XC = HX / 2                                     # shaft axis x
FOOT_END = 10.0                                 # foot length past each hole centre: Assumption (B), the foot's outline (open figures)
Y_DE, Y_NDE = -80.0, 140.5                      # drive-end shield face, fan cover end (220.5 body + 30 shaft = 250.5); the shield face
                                                # 80 from the first hole row: Assumption (B), the drawing's 45.0 / 75.0 not assigned (open figures)

def build():
    P = Prims()
    P.cyl("M-CAST-BLUE", (XC, Y_DE + 12, SH), (XC, Y_NDE - 72, SH), R)                                     # frame, between the shield and the fan cover
    for k in range(10):                                                                                     # cooling fins on the upper half: count, angles, 6 x 2.5 on R + 3: Assumption (C), appearance
        a = math.radians(20 + k * 14); fy0, fy1 = Y_DE + 16, Y_NDE - 76
        cx, cz = XC + (R + 3) * math.cos(a), SH + (R + 3) * math.sin(a)
        P.obox("M-CAST-BLUE", (cx - 1.5 * math.sin(a) * 0, fy0, cz), (math.cos(a), 0, math.sin(a)), (0, 1, 0), (-math.sin(a), 0, math.cos(a)), 6, fy1 - fy0, 2.5)
    P.cyl("M-CAST-BLUE", (XC, Y_DE, SH), (XC, Y_DE + 12, SH), R - 4)                                        # drive-end shield 12 long at R - 4: Assumption (C), housing wall
    fc = P.cyl("M-STEEL-7035", (XC, Y_NDE - 72, SH), (XC, Y_NDE, SH), FC_R)                                 # fan cover 72 long (STEP read-back, measure.md) (louvres: decal)
    P.hole("M-GASKET", (XC, Y_NDE - 73, SH), (XC, Y_NDE - 1.5, SH), FC_R - 1.5, fc)                        # a 1.5 shell with its end face, so the fan inside is real (1.1)
    P.cyl("node:fan|M-BLACK-PA", (XC, Y_NDE - 60, SH), (XC, Y_NDE - 58, SH), FC_R - 7); P.pivot("fan", "rotate", (XC, Y_NDE - 59, SH), axis=(0, -1, 0), range=(0, 360))  # fan Ø124 x 2: Assumption (C), internal
    P.cyl("node:shaft|M-ZINC", (XC, Y_DE + 2, SH), (XC, Y_DE - 30, SH), 7.0)                                 # shaft Ø14 x 30 (drawing p. 1)
    P.box("node:shaft|M-STEEL-7035", XC - 2.5, Y_DE - 28, SH + 4.5, 5, 25, 2.5)                              # key 5 x 5 x 25 (drawing p. 1), built 5 x 25 x 2.5 with its top at the shaft's top line z SH + 7, inside the shaft's envelope (its top edges 0.46 outside the round surface, 1.5): the 2.5 height Assumption (B) (1.4); GA / keyway depth NOT ON FILE (B)
    P.pivot("shaft", "rotate", (XC, Y_DE, SH), axis=(0, -1, 0), range=(0, 360))                              # (the M5 tapped centre hole of detail A is left out: spec.md)
    for x0 in (-12.0, HX - 12.0):                                                                           # feet, 136 across overall (drawing p. 1), 8 thick (drawing p. 1)
        ft = P.box("M-CAST-BLUE", x0, -FOOT_END, 0, 24, HY + 2 * FOOT_END, 8.0)                          # foot runs FOOT_END past each hole (1.2: the holes sat on its ends)
        P.box("M-CAST-BLUE", x0 + 4, 10, 8, 16, HY - 20, SH - R + 20)                                    # web from the foot into the frame, 16 x 70 x 29: Assumption (C), housing
        for y in (0.0, HY):                                                                             # 7.0 along the shaft x 10.5 across slot (drawing p. 1), as three Ø7 holes
            for dx in (-1.75, 0.0, 1.75): P.hole("M-GASKET", (x0 + 12 + dx, y, -1), (x0 + 12 + dx, y, 9), 3.5, ft)
    tb_z = SH + R                                                                                           # terminal box on top (F3, cutsheet p. 1)
    P.box("M-CAST-BLUE", XC - 40.5, -10, tb_z, 81.0, 110.0, 175.5 - tb_z - 3)                              # box 81 x 110 (brief :25; finding 2 open), top at 175.5 (drawing p. 1)
    P.box("M-CAST-BLUE", XC - 42, -12, 175.5 - 3, 84.0, 114.0, 3.0)                                         # lid 84 x 114 x 3: Assumption (C), appearance
    P.cyl("node:pwr|M-ZINC", (XC + 40.5, 45, tb_z + 16), (XC + 52, 45, tb_z + 16), 10.0)                     # M20 entry on the right (drawing p. 1); its place y 45, z + 16: Assumption (B)
    P.pivot("pwr", "port", (XC + 52, 45, tb_z + 16), axis=(1, 0, 0), range=(0, 0), unit="480V-3P+E", gender="none")  # a cable entry to ring-lug screw terminals (PIN-002)
    P.box("M-ALU-ANOD", XC + R - 2, 20, SH - 15, 0.6, 50, 30)                                                # nameplate field on the frame side (decal): size and place Assumption (C)
    P.collider("env", XC - FC_R, Y_DE - 30, 0, 2 * FC_R, Y_NDE - Y_DE + 30, 175.5)
    return P

PREVIEWS = [dict(name="drive end three-quarter", az=250, el=20), dict(name="fan end and terminal box", az=60, el=25), dict(name="side feet and shaft height", az=180, el=0)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
