#!/usr/bin/env python3
"""cap-strut-41: generic end cap for the 41 x 41 strut channel, our own vendor-neutral design of the ETIM 10.0 class EC000475
(Protective cap/cover for mounting rail/- profile; synonyms end cap, end cap/cover for support/profile rail, profile rail cover cap),
built unattended (OPERATING.md 12, generic elements; group EG021005 Mounting systems, a tier-2 class, after EG021006 by name,
lib/rounds/mech/r149.md). A grey polyamide cap that closes the cut end of strut 1.0: a plate 41 x 41 x 2 over the end face, flush
with the channel's outline, and a plug 12 deep that enters the channel's lower chamber (between the walls, over the back, under the
lips' returns) 0.2 clear all round. Every channel figure is read from strut with library.load, so the cap and the channel cannot
drift apart. The class's features are not on file (lib/standards/etim/class-features.csv has no EC000475 rows): spec.md gives the
design values under plain names, as compensator-ring-qt-6 and spring-plate-qt-6 do. Every size is a design choice. No retention
force, impact or fire claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "cap-strut-41", "1.0", "connector-part"
TITLE = ("end cap for a 41 x 41 strut channel, generic, grey polyamide, plate 41 x 41 x 2 flush with the channel's outline, plug "
         "35.6 x 25.6 x 12 into the lower chamber 0.2 clear")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic protective cap/cover for mounting rail/-profile (ETIM 10.0 EC000475), an end cap for strut 1.0 "
            "(41 x 41 x 2.5): a plate over the end face and a plug into the channel's lower chamber, the channel's figures read from "
            "strut (library.load); class features not on file, design values under plain names (spec.md); every size a design "
            "choice; no retention force, impact or fire claim; no vendor file opened")
ORIGIN = ("strut's own frame at its run start: the channel's end face x = 0 (the cap's seat), the centre line y = 0, the back's outer "
          "face z = 0; the plug goes +x into the channel, the plate lies at -x, the open side (the lips) up")
COMMAND = "CAPST41"
PARAMS = dict()

ST = library.load("strut")                   # strut 1.0: the channel the cap closes (one home for each figure)
W, H, T = ST.W, ST.H, ST.T                   # 41 x 41, wall 2.5
RET_LOW = ST.H - ST.T - ST.RET               # 28.5: the underside of the lips' returns, the lower chamber's top
PLATE_T = 2.0                                # design: the plate's thickness (<= 3, so the gate skips its edges)
PLUG_L = 12.0                                # design: the plug's depth into the channel
C = 0.2                                      # design: the plug's clearance to the walls, the back and the returns
IN = 0.5                                     # the plug runs 0.5 into the plate (one solid joint, strut's way)
PLUG_Y = W / 2 - T - C                       # 17.8: half the plug's width, 0.2 inside each wall's inner face (y +-18)
PLUG_Z0, PLUG_Z1 = T + C, RET_LOW - C        # 2.7 .. 28.3: over the back (z 2.5), under the returns (z 28.5)
MAT = "M-GREY-PA"                            # grey polyamide (render layer M-GREY-PA, not a printed layer)

assert abs(RET_LOW - 28.5) < 1e-9 and abs(PLUG_Y - 17.8) < 1e-9                                  # by hand: 41 - 2.5 - 10 = 28.5; 20.5 - 2.5 - 0.2
assert abs((PLUG_Z1 - PLUG_Z0) - 25.6) < 1e-9 and abs(2 * PLUG_Y - 35.6) < 1e-9                  # the plug 35.6 x 25.6
assert PLUG_Y < W / 2 - T and PLUG_Z0 > T and PLUG_Z1 < RET_LOW                                 # clear of the walls, the back and the returns
assert PLUG_Y > W / 2 - ST.LIP + T                                                              # the returns (|y| 11 .. 13.5) stand over the plug: it stays under 28.5
assert PLATE_T <= 3.0 and PLUG_L >= 8.0 and 2 * PLUG_Y >= 8.0 and PLUG_Z1 - PLUG_Z0 >= 8.0       # no free edge in the gate's 3 to 7 mm trap


def build():
    P = Prims()
    P.box(MAT, -PLATE_T, -W / 2, 0, PLATE_T, W, H)                                                # the plate, flush with the outline
    P.box(MAT, -IN, -PLUG_Y, PLUG_Z0, PLUG_L + IN, 2 * PLUG_Y, PLUG_Z1 - PLUG_Z0)                  # the plug, 0.5 into the plate
    P.collider("plate", -PLATE_T, -W / 2, 0, PLATE_T, W, H)
    P.collider("plug", 0, -PLUG_Y, PLUG_Z0, PLUG_L, 2 * PLUG_Y, PLUG_Z1 - PLUG_Z0)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
