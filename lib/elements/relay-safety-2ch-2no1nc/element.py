#!/usr/bin/env python3
"""relay-safety-2ch-2no1nc: safety relay, one dual-channel input, 2 NO safety outputs, 22.5 mm housing with four removable terminal blocks.
Brief: references/measure.md (the maker's installation manual on file, p. 9 / 11 / 14 / 31 / 73: 22.5 x 119.14 x 113.6; RESTRICTED licence,
baseline only; the maker and part numbers in references/ only).
1.2: DOC-006 (OPERATING.md 6): no vendor name or part number in BASELINE, the spec or ratings.csv's sources."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "relay-safety-2ch-2no1nc", "1.2", "device"
TITLE = "safety relay, dual-channel input, 2 NO safety outputs, 1 NC aux, 22.5 mm, 35 mm rail"
TOOLKIT = "1.3"
BASELINE = "maker's datasheet: the installation manual on file (references/measure.md), p. 11 / p. 73: 22.5 x 119.14 x 113.6; terminal blocks 4.3 proud from the STEP. Vendor file RESTRICTED, nothing shipped"
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "SR"
PARAMS = {}
W, H, D0 = 22.5, 119.14, 113.6
D = D0 - 7.5                                       # manual depth includes the 7.5 clip region behind the crown
TB_PROUD, TB_H = 4.3, 14.0                         # removable terminal blocks: two top, two bottom
LEDS = ["led-pwr", "led-in1", "led-in2", "led-logic", "led-out"]      # ruling 2026-11-03: names from the manual's LED legend (PWR/Fault, IN1, IN2, LOGIC IN, OUT)
LED_COL = {"led-pwr": "M-LENS-GREEN", "led-in1": "M-LENS-GREEN", "led-in2": "M-LENS-GREEN", "led-logic": "M-LENS-GREEN", "led-out": "M-LENS-GREEN"}

def build():
    P = Prims(); yb = -(D - TB_PROUD)                                                               # housing front; blocks stand 4.3 proud
    P.box("M-GREY-PA", 0, yb, -H / 2, W, D - TB_PROUD, H)
    din.rail_clip(P, 0, W)
    for sz in (1, -1):                                                                              # four pluggable blocks, 4 terminals each
        for k in range(2):
            z0 = sz * (H / 2 - TB_H * (k + 1)) + (0 if sz > 0 else 0)
            z0 = (H / 2 - TB_H * (k + 1)) if sz > 0 else (-H / 2 + TB_H * k + 1.0)                  # mirrored: 1.0 short of the end face (1.1: flush, it flickered)
            P.box("M-BLACK-PA", 1.0, yb - TB_PROUD, z0, W - 2.0, TB_PROUD + 12.0, TB_H - 1.0)
            for i in range(4):
                cx = 3.0 + i * 5.5; P.cyl("M-ZINC", (cx, yb - TB_PROUD, z0 + TB_H / 2), (cx, yb - TB_PROUD - 1.0, z0 + TB_H / 2), 1.6)
                P.box("M-GASKET", cx - 1.3, yb - TB_PROUD + 3, (z0 + TB_H - 1.0) if sz > 0 else (z0 - 0.5), 2.6, 7, 0.5)
    for i, n in enumerate(LEDS): din.led(P, n, LED_COL[n], 6.0, yb, 24.0 - i * 7.0, r=1.5)
    P.cyl("node:sw-mode|M-BLACK-PA", (15.0, yb + 0.5, 8.0), (15.0, yb - 1.0, 8.0), 4.0); P.pivot("sw-mode", "rotate", (15.0, yb, 8.0), axis=(0, -1, 0), range=(0, 300))
    P.box("M-WHITE-PA", 1.5, yb - 0.2, -34, W - 3, 0.2, 60)                                           # face legend field (decal: terminal ids, LED legend)
    P.collider("env", 0, -D, -H / 2, W, D0, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="face LEDs, mode switch, terminal blocks", az=262, el=8, center=(11, -112, 0), height=130), dict(name="rear rail clip", az=60, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
