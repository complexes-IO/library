#!/usr/bin/env python3
"""plug-pushin: blanking plug for a push-in port, a stem of one inch tube OD under a round head, closing a push-in fitting's tube
port that a circuit leaves unused ("every port connected or plugged", request pneu-1). Generic (OPERATING.md 12, EM 2026-11-07):
our own vendor-neutral design of ETIM 10.0 EC004547 "Plug stop for fitting" (synonym "Blanking plug"); the class values it is
designed to are in spec.md "## Class values". The stem is a tube end: its diameter is the tube OD of toolkit/pneu.py (request
pneu-1: D2 inch tube, push-in fittings to ISO 14743; pneu.TUBES_IN, exact conversions of the size names), so PNE-001 pairs it with
fitting-pushin's `port-tube` as it pairs a tube-pneu end. The head is as wide as fitting-pushin's release sleeve (its body less
SLEEVE_DD, read from that element), so it sits on the sleeve's face and overhangs nothing. The stem's length stands in for the
push-in port's insertion depth, which is not on file (pneu.PUSHIN depth, fitting-pushin's class B line): one class B line in
spec.md. The joint is a pivot on its axis at the head's underside. No vendor file was opened (pneu-r113)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "plug-pushin", "1.0", "connector"
TITLE = "generic blanking plug for a push-in port, tube 1/4 in"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic plug stop for fitting (ETIM 10.0 EC004547), a blanking plug for a push-in port; the stem "
            "is the tube OD of toolkit/pneu.py D2 (pneu.TUBES_IN), the head as wide as fitting-pushin's release sleeve; head "
            "length a design choice; the stem's length a stand-in for the insertion depth, a class B document wanted (pneu.PUSHIN)")
ORIGIN = ("joint plane: the head's underside y = 0 on the stem's axis (x = z = 0), where it meets fitting-pushin's release sleeve "
          "face; the stem and the fitting toward -y, the head toward +y")
COMMAND = "PLUG-PUSHIN"
PARAMS = dict(tube="1/4")

_FP = library.load("fitting-pushin")
TUBES = tuple(_FP.BODY_D)                                   # the tube ODs fitting-pushin takes: 5/32, 1/4, 3/8 (pneu.TUBES_IN)
STEM_L = 16.0                                               # stand-in (class B): the push-in port's insertion depth is not on file (pneu.PUSHIN)
HEAD_L = 8.0                                                # design choice: head length along y (envelope edges >= 8 for the AutoCAD fillet)
STEM_IN = 0.5                                               # the stem runs 0.5 into the head (one solid joint)
MAT = "M-GREY-PA"                                           # class value: polyamide, grey (fitting-pushin's release sleeve); not a
                                                            # printed material, so the Blender gate lays no decal on the thin stem


def head_d(tube):
    """the head's diameter: fitting-pushin's release sleeve for the same tube, its body less SLEEVE_DD"""
    return _FP.BODY_D[tube] - _FP.SLEEVE_DD


for _o in TUBES:
    assert _o in pneu.TUBES_IN
    assert head_d(_o) >= pneu.TUBES_IN[_o] + 4.0            # the head's rim stands at least 2 proud of the stem all round
    assert head_d(_o) >= 8.0 and HEAD_L >= 8.0              # every envelope edge at least 8 (the AutoCAD gate's fillet pre-flight)


def length():
    """overall length, stem end to head top: STEM_L + HEAD_L (24 for every tube); class value length"""
    return STEM_L + HEAD_L


def build(tube="1/4"):
    if tube not in TUBES: raise ValueError(f"tube {tube}: one of {', '.join(TUBES)} (pneu.TUBES_IN, D2)")
    P = Prims(); od = pneu.TUBES_IN[tube]; hd = head_d(tube)
    P.cyl(MAT, (0, 0, 0), (0, HEAD_L, 0), hd / 2.0)                                              # round head, underside on y = 0
    P.cyl(f"node:port-a|{MAT}", (0, -STEM_L, 0), (0, STEM_IN, 0), od / 2.0)                      # stem: a tube end, STEM_L below y = 0
    P.pivot("port-a", "port", (0, 0, 0), axis=(0, -1, 0), range=(0, 0), unit=f"tube-{tube}", gender="male")
    r = hd / 2.0
    P.collider("env", -r, -STEM_L, -r, 2 * r, STEM_L + HEAD_L, 2 * r)
    return P


PREVIEWS = [dict(name="three-quarter", az=250, el=25), dict(name="end on port-a", az=250, el=-40),
            dict(name="tube 5/32", az=250, el=25, params=dict(tube="5/32")),
            dict(name="tube 3/8", az=250, el=25, params=dict(tube="3/8"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
