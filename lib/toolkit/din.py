"""Shared parts of DIN-rail devices (origin: back face on the rail crown y = 0, rail centreline z = 0, left edge x = 0, body toward -y).
Terminal rows, screw heads, LED windows, rail clips, toggles. Dimensions are the common ones a product manual shows; each element
sets its own sizes from its brief."""
from . import std22

def rail_clip(P, x0, w, depth=7.5):
    """the latch that sits over the rail: two lips behind the back face, the rail (35 high) between them, and a release tab below"""
    P.box("M-GREY-PA", x0 + 1, 0, 17.5, w - 2, depth, 2.0)            # upper lip over the rail flange
    P.box("M-GREY-PA", x0 + 1, 0, -19.5, w - 2, depth, 2.0)           # lower lip
    P.box("M-GREY-PA", x0 + w / 2 - 3, 0, -27, 6, 3.0, 8.0)           # release tab (screwdriver slot)

SLOT = 0.5                                                             # the wire entry's depth into the end face (design choice)

def terminal_row(P, x0, y_face, z_edge, n, pitch, up=True, screw_r=2.2, opening=(3.6, 5.0), depth=9.0, mat="M-ZINC", target=None):
    """n screw terminals along x on a shoulder: screw heads on the front face, wire openings on the end face.
    y_face: the shoulder's front face (y < 0); z_edge: the device's end face (top if up).
    target: the housing's primitive index. Given, each wire entry is a slot SLOT deep cut into the end face (P.cutbox through the
    housing, the dark slot filling it), inside the housing's envelope. Without it the slot stands SLOT proud of the end face, the
    toolkit-1.3 shape the elements gated with it keep until their next version (request elec-2: thermostat-enc 1.0 measured 60.5
    for its 60 housing). A new caller passes the housing."""
    s = 1 if up else -1
    for i in range(n):
        cx = x0 + pitch * (i + 0.5)
        P.cyl(mat, (cx, y_face, z_edge - s * 6.0), (cx, y_face - 1.2, z_edge - s * 6.0), screw_r)          # screw head
        if target is None:
            P.box("M-GASKET", cx - opening[0] / 2, y_face + 2.0, z_edge - (0.0 if up else SLOT), opening[0], depth, SLOT)   # proud (toolkit 1.3)
            continue
        z0 = z_edge - (SLOT if up else 0.0)                                                                   # recessed into the end face
        P.cutbox("M-GASKET", cx - opening[0] / 2, y_face + 2.0, z0 - (0.0 if up else 1.0), opening[0], depth, SLOT + 1.0, target)   # out past the face
        P.box("M-GASKET", cx - opening[0] / 2, y_face + 2.0, z0, opening[0], depth, SLOT)                    # wire entry: the dark slot in its cut

def led(P, node, colour, cx, y_face, cz, r=1.6, proud=0.3):
    """a lens window on the front face; the node is emissive"""
    P.cyl(f"node:{node}|{colour}", (cx, y_face + 0.5, cz), (cx, y_face - proud, cz), r)
    P.pivot(node, "emissive", (cx, y_face, cz), axis=(0, -1, 0), range=(0, 1))

def toggle(P, node, x0, w, y_face, cz, length=16.6, proud=3.7, swing=25.0, mat="M-BLACK-PA"):
    """a breaker handle: a bar on the front face pivoting about x at its root; ON is up (+z)"""
    P.box(f"node:{node}|{mat}", x0 + 1.5, y_face - proud, cz - length / 2, w - 3, proud, length)
    P.pivot(node, "rotate", (x0 + w / 2, y_face, cz), axis=(1, 0, 0), range=(-swing, swing))

def indicator(P, node, x0, w, y_face, cz, mat="M-RED-PA"):
    """contact-position window: material swap red / green in the twin; declared as a lamp without emission"""
    P.box(f"node:{node}|{mat}", x0 + w / 2 - 3, y_face - 0.4, cz - 2, 6, 0.6, 4)
    P.pivot(node, "emissive", (x0 + w / 2, y_face, cz), axis=(0, -1, 0), range=(0, 1))
