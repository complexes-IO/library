#!/usr/bin/env python3
"""shock-buffer: generic cylindrical rubber buffer (end stop), our own vendor-neutral design of the ETIM 10.0 class EC011714 (Shock
buffer), built unattended (OPERATING.md 12, generic elements). An elastomer pad Ø40 x 30 (node `pad`, compresses 7.5 under a blow)
bonded to a steel base plate Ø40 x 4, with an M10 male stud (port `stud`) to fix it. The class values (spec.md, "Class values")
are design inputs. The M10 thread's limits are derived (spec.md, What it meets: derive.thread, ISO 68-1 / ISO 965-1); the thread
form is not drawn: the stud is a plain cylinder at the nominal Ø10. Every size below is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "shock-buffer", "1.2", "device"
TITLE = "shock buffer, generic, rubber, Ø40 x 34, M10 male stud"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic shock buffer (ETIM 10.0 EC011714); class values are design inputs (spec.md); the M10 thread "
            "derived (ISO 68-1, ISO 965-1), modelled plain; every size a design choice; no vendor file opened")
ORIGIN = ("the mounting face (the base plate's underside, which seats on the host) on the buffer's axis; the buffer toward +z, its "
          "impact face up, the stud toward -z")
COMMAND = "SHOCKBUF"
PARAMS = dict()
D = 40.0                         # class value: diameter (pad and base plate)
PLATE_T = 4.0                    # steel base plate, bonded to the pad: design choice
PAD_H = 30.0                     # elastomer pad: design choice (height 34 over both: the class value)
STUD_D, STUD_L = 10.0, 20.0      # class value M10; stud length 20: design choice. The thread's limits are derived (spec.md, What it meets);
                                 # the form is not drawn: modelled plain at the nominal Ø10
DEFLECT = 7.5                    # the pad's travel under a blow, 25 % of its height: design choice

def build():
    P = Prims(); Z, R = "M-ZINC", "M-GASKET"
    P.cyl(Z, (0, 0, 0), (0, 0, PLATE_T), D / 2)                                              # base plate
    P.cyl(f"node:pad|{R}", (0, 0, PLATE_T), (0, 0, PLATE_T + PAD_H), D / 2)                  # elastomer pad, impact face on top
    P.pivot("pad", "compress", (0, 0, PLATE_T), axis=(0, 0, 1), range=(0, DEFLECT))           # squeezed toward its bonded face
    P.cyl(f"node:stud|{Z}", (0, 0, -STUD_L), (0, 0, 0), STUD_D / 2)                          # stud M10 x 20 (plain at Ø10)
    P.pivot("stud", "port", (0, 0, 0), axis=(0, 0, -1), unit="M10", gender="male", thread="M10", length=STUD_L)
    P.collider("body", -D / 2, -D / 2, 0, D, D, PLATE_T)
    P.collider("pad", -D / 2, -D / 2, PLATE_T, D, D, PAD_H)
    P.collider("stud", -STUD_D / 2, -STUD_D / 2, -STUD_L, STUD_D, STUD_D, STUD_L)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
