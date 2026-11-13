#!/usr/bin/env python3
"""damper-vibration: generic cylindrical rubber-metal vibration damper (a machine mount), our own vendor-neutral design of the ETIM
10.0 class EC011696 (Vibration damper), built unattended (OPERATING.md 12, generic elements). A rubber body Ø50 x 32 (node `rubber`,
compresses 5 at its rated load) bonded between two steel plates Ø40 x 4, an M10 male stud on each: the lower one (port `stud`) into
the base, the upper one with its plate (node `top`, sinks 5 at the rated load) through the machine's foot. The class values
(spec.md, "Class values") are design inputs. The M10 thread's limits are derived (spec.md, What it meets: derive.thread, ISO 68-1 /
ISO 965-1); the thread form is not drawn: both studs are plain cylinders at the nominal Ø10. Every size below is a design choice.
No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "damper-vibration", "1.3", "device"
TITLE = "vibration damper, generic, rubber-metal, Ø50 x 40, M10 male studs both ends, 1000 N"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic vibration damper (ETIM 10.0 EC011696); class values are design inputs (spec.md); the M10 thread "
            "derived (ISO 68-1, ISO 965-1), modelled plain; every size a design choice; no vendor file opened")
ORIGIN = ("the mounting face (the lower plate's underside, which seats on the base) on the damper's axis; the damper toward +z, the "
          "machine-side stud up, the base-side stud toward -z")
COMMAND = "VIBDAMPER"
PARAMS = dict()
D = 50.0                         # class value: diameter, the rubber body
H = 40.0                         # class value: height, the lower plate's underside to the upper plate's top face (studs not included)
PLATE_D, PLATE_T = 40.0, 4.0     # bonded steel plates Ø40 x 4, top and bottom: design choice
RUBBER_H = H - 2 * PLATE_T       # 32: the rubber between the plates
STUD_D, STUD_L = 10.0, 25.0      # class value M10; stud length 25 each end: design choice. The thread's limits are derived (spec.md,
                                 # What it meets); the form is not drawn: modelled plain at the nominal Ø10
DEFLECT = 5.0                    # the rubber's compression at the rated load: max. load capacity 1000 N / stiffness 200 N/mm (class values)

def build():
    P = Prims(); Z, R = "M-ZINC", "M-GASKET"
    P.cyl(Z, (0, 0, 0), (0, 0, PLATE_T), PLATE_D / 2)                                        # lower plate, mounting face at z = 0
    P.cyl(f"node:rubber|{R}", (0, 0, PLATE_T), (0, 0, PLATE_T + RUBBER_H), D / 2)             # rubber body, bonded to both plates
    P.pivot("rubber", "compress", (0, 0, PLATE_T), axis=(0, 0, 1), range=(0, DEFLECT))        # squeezed toward the lower plate
    P.cyl(f"node:top|{Z}", (0, 0, H - PLATE_T), (0, 0, H), PLATE_D / 2)                      # upper plate, the machine's foot seats on it
    P.cyl(f"node:top|{Z}", (0, 0, H), (0, 0, H + STUD_L), STUD_D / 2)                        # machine-side stud M10 x 25 (plain at Ø10)
    P.pivot("top", "translate", (0, 0, H), axis=(0, 0, -1), range=(0, DEFLECT),               # sinks with the rubber under load
            end="machine", gender="male", thread="M10", length=STUD_L)
    P.cyl(f"node:stud|{Z}", (0, 0, -STUD_L), (0, 0, 0), STUD_D / 2)                          # base-side stud M10 x 25 (plain at Ø10)
    P.pivot("stud", "port", (0, 0, 0), axis=(0, 0, -1), unit="M10", gender="male", thread="M10", length=STUD_L)
    P.collider("body", -PLATE_D / 2, -PLATE_D / 2, 0, PLATE_D, PLATE_D, PLATE_T)
    P.collider("rubber", -D / 2, -D / 2, PLATE_T, D, D, RUBBER_H)
    P.collider("top", -PLATE_D / 2, -PLATE_D / 2, H - PLATE_T, PLATE_D, PLATE_D, PLATE_T)
    P.collider("stud", -STUD_D / 2, -STUD_D / 2, -STUD_L, STUD_D, STUD_D, STUD_L)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
