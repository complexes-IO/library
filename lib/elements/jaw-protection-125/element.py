#!/usr/bin/env python3
"""jaw-protection-125: generic protection jaw for a bench vice (the soft angle a fitter hangs over a vice's hard jaw plate so the
plate's face doesn't mark finished work), our own vendor-neutral design of the ETIM 10.0 class EC002202 (Vice plate for bench-vice;
its synonyms name protection jaws and vice protection jaws), built unattended (OPERATING.md 12, generic elements; `python lib/build.py
inventory mech` lists the class once no inventory row builds unattended: group EG020054 Clamping tools, lib/needs-em/mech.md). An
aluminium angle 3 thick: a front leg that covers vise-bench 1.0's jaw plate's clamping face (125 x 50, read from vise-bench with
library.load: one home for the plate's size) and a top leg that rests on the plate's top edge, so it hangs there by its own weight. Not
magnetic, no screw, no hole. One fixed body, no moving node, no terminal. The class values (spec.md, "Class values") are design
inputs; every other size is a design choice. No clamping force or protection claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "jaw-protection-125", "1.1", "device"
TITLE = "protection jaw, generic, aluminium angle 3 thick for vise-bench's jaw plate 125 x 50 x 12, hangs on the plate's top edge"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic vice plate for bench-vice (ETIM 10.0 EC002202), a protection jaw; class values are design inputs "
            "(spec.md); the jaw plate it covers, 125 x 50 x 12, read from vise-bench 1.0 (library.load); every other size a design "
            "choice; no clamping force or protection claimed; no vendor file opened")
ORIGIN = ("the protection face x = 0 (the front leg's +x face, toward the work); the front leg's underside z = 0 (level with the vice "
          "plate's underside); the jaw's centre y = 0; the front leg's back face (on the vice plate's clamping face) at x = -3; the "
          "top leg's underside (on the plate's top edge) at z = 50")
COMMAND = "JAWPROT"
PARAMS = dict()

VB = library.load("vise-bench")       # vise-bench 1.0: the vice whose jaw plate this angle covers (one home for the plate's size)
W, H, T = VB.JAW_W, VB.JAW_H, VB.JAW_T  # 125 wide (y) x 50 high (z) x 12 thick (x): vise-bench's jaw plate
S = 3.0                               # the angle's legs 3 thick: design choice (at or under the gate's 3.0 short-edge rule)
AL = "M-ALU-ANOD"

assert (W, H, T) == (125.0, 50.0, 12.0)    # the plate as vise-bench 1.0 gives it
assert S <= 3.0 and min(W, H, T) >= 8.0    # every free-corner edge 3 or shorter, or 8 or longer (device r 0.5)


def build():
    P = Prims()
    P.box(AL, -S, -W / 2, 0, S, W, H + S)          # front leg: x -3..0, z 0..53, over the plate's clamping face and up past its top
    P.box(AL, -S - T, -W / 2, H, T, W, S)          # top leg: x -15..-3, z 50..53, resting on the plate's top edge
    P.collider("front-leg", -S, -W / 2, 0, S, W, H + S)    # two boxes, so the vice plate's seat under the top leg stays free
    P.collider("top-leg", -S - T, -W / 2, H, T, W, S)
    return P


PREVIEWS = [dict(name="three-quarter", az=60, el=25), dict(name="back", az=230, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
