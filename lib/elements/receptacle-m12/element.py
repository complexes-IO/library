#!/usr/bin/env python3
"""receptacle-m12: the device side of an M12 joint, built to the I/O block's ports (toolkit/m12.py 1.3, kind device). Female: the coded
insert stands 3.4 proud of the housing face, the foremost face of the port; behind the face a Ø12.3 entry, then the threaded bore round
the insert to its floor, where the face seal (seal-m12) sits. Male: the fixed threaded sleeve round the pin carrier, standing out of the
housing face. Hosts (a bulkhead port, an I/O block, a station) place it at each port with front() and face(); its node `self` (the
body) is the port the cable lands on, with the mating data in its extras (port_data). 1.4: insert-m12 1.4 (D poles and notches, the L
key outlines, round 5). A host clocks a port by its placement's roll (toolkit/prims.py: clockwise looking along +y, as m12.py measures
angles). 1.5: insert-m12 1.5 (D keyed as it is; X03 / X04 key outlines; the key tolerance per coding). Built in the M12 mating frame: mating plane y = 0, the plug toward -y, the body toward +y. Brief: references/measure.md."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, m12
from toolkit.prims import Prims

ID, VERSION, CLASS = "receptacle-m12", "1.6", "connector"
TITLE = "M12 receptacle (device side), female (sockets, insert 3.4 proud, threaded bore) or male (pins, threaded sleeve), A / D / L coded, M12 x 1"
TOOLKIT = "1.3"
BASELINE = "the I/O block's ports read with Open CASCADE (round 4): female insert 3.4 proud, Ø12.3 entry to 1.1 deep, Ø10.917 bore 4.9 long, floor 9.5 below the insert face; male X03 (L) sleeve 13.1 out, carrier face 4.2 out; the male A / D device sleeve and the body behind the face an Assumption"
ORIGIN = "the mating plane on the axis (female: the insert face, the housing face 3.4 behind it; male: the carrier face, the sleeve ahead of it toward -y); body toward +y"
COMMAND = "M12RCP"
PARAMS = dict(gender="female", coding="A", conditions="", length=13.0)
BODY_R = 6.75                     # Ø13.5 body inside the housing (port-m12-a drawing p. 1 front Ø13.5): Assumption for a housing

def front(gender="female", coding="A"):
    """how far the receptacle stands ahead of its mating plane"""
    return m12.front(gender, coding, "device")

def face(gender="female", coding="A"):
    """where the housing face sits behind the mating plane: a host puts its face there"""
    return m12.face(gender, coding, "device")

def build(gender="female", coding="A", conditions="", length=13.0):
    """length: the body's back behind the mating plane (a host that bridges to its own parts passes its own)"""
    P = Prims(); f = face(gender, coding); length = float(length)
    if gender == "female":
        D = m12.female("device", coding, "depth"); cb_r, cb_d = m12.FEMALE["device"]["counterbore"]
        body = P.cyl("node:self|M-ZINC", (0, f, 0), (0, length, 0), BODY_R)
        P.hole("M-GASKET", (0, f - 1.0, 0), (0, f + cb_d, 0), cb_r, body)                           # the Ø12.3 entry
        P.hole("M-GASKET", (0, f + cb_d, 0), (0, m12.insert_l("female", coding, "device"), 0), m12.THREAD_R, body)   # the threaded bore and the base's seat
        t = m12.seal_thick(coding, "device", "cordset")
        library.place(P, dict(element="seal-m12", version="1.2", tag="seal", parent="", x=0, y=D - t, z=0, yaw=0.0,
                              params=dict(r_in=m12.INSERT_R[coding] + 0.05, r_out=m12.THREAD_R - 0.01, thick=t)))   # on the bore floor
    else:
        ri, reach = m12.male("device", coding, "bore"), m12.male("device", coding, "reach")
        sl = P.cyl("M-ZINC", (0, -reach, 0), (0, f, 0), m12.THREAD_R)                              # the fixed threaded sleeve, out of the housing face
        P.hole("M-GASKET", (0, -reach - 1.0, 0), (0, f + 1.0, 0), ri, sl)
        body = P.cyl("node:self|M-ZINC", (0, f, 0), (0, length, 0), BODY_R)
        P.hole("M-GASKET", (0, f - 1.0, 0), (0, m12.insert_l("male", coding, "device"), 0), ri, body)        # the carrier's seat
    library.place(P, dict(element="insert-m12", version="1.6", tag="insert", parent="", x=0, y=0, z=0, yaw=0.0,
                          params=dict(gender=gender, coding=coding, kind="device", conditions=conditions)))
    P.pivot("self", "port", (0, 0, 0), axis=(0, -1, 0), range=(0, 0), unit=coding, **m12.port_data(coding, gender, "device"))
    ahead = front(gender, coding)
    P.collider("env", -BODY_R, -ahead, -BODY_R, 2 * BODY_R, length + ahead, 2 * BODY_R)
    return P

PREVIEWS = [dict(name="female A-coded", az=250, el=25), dict(name="male A-coded", az=250, el=25, params=dict(gender="male")),
            dict(name="female L-coded", az=250, el=25, params=dict(coding="L")), dict(name="male L-coded (power in)", az=250, el=25, params=dict(gender="male", coding="L"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
