#!/usr/bin/env python3
"""conveyor-incline: cleated belt incline conveyor, one straight sloped section, our own design, built unattended (OPERATING.md 12,
own designs; inventory row own_design "yes": "cleated belt incline conveyor section (our own build)"). Goods ride up a belt with
cross cleats that rises along +y at 30 degrees. The belt is drawn as its top run at rest, one sloped plate with six cleats
standing on it: it lies on a slider bed plate, which two cross members carry between the two sloped side frames. The belt's wrap
round the pulleys, its return run and the drive are not drawn. The head pulley and the tail pulley (a drum with a shaft through
it) are nodes `pulley-head` and `pulley-tail`, each turning about its own axis (along x): they are what the twin turns when the
conveyor runs. The frames stand on two supports (two vertical posts cut to the frames' sloped undersides and a tie each) on two
floor rails that run the section's full 1500 length, each rail with two M12 clearance holes (ISO 273 medium) for floor anchors
in the pattern of conveyor-roller's, conveyor-slat's and conveyor-mattop's foot plates. At its tail end the belt's top is at
z 750, the track height of the horizontal sections, so one of them can feed it. Every size below is a design choice. No load
rating, no speed, no safety claim. No vendor file was opened.
Gate note: the bounding box's extremes lie on axis-aligned solids (the floor rails' ends and outer edges) except the top, the belt
plate's upper corner: the gate's r 1.0 fillet on a corner of a tilted box draws its extreme in by 0.37 (the gate allows 0.5),
so no axis may have two such corners at its ends (mech-r92: the frames' sloped ends at both ends of y failed it, 0.74)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "conveyor-incline", "1.1", "furniture"
TITLE = "cleated belt incline conveyor section, 500 between frames, 1500 long, 30 degrees, belt 490 wide with 6 cleats, belt top 750 at the tail rising to 1558 at the head, head and tail pulleys, floor rails with 4 x M12 anchor holes"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; anchor holes ISO 273 medium for M12; every size a "
            "design choice; no load rating, no speed, no safety claim; no vendor file opened")
ORIGIN = ("floor plane z = 0 at the centre of the section's plan, x = 0 midway between the side frames, y = 0 midway along the "
          "floor rails (y -750..750); goods travel up the slope toward +y (the head end); the belt's top line passes z 750 over "
          "the tail end (y -750) and rises at 30 degrees; the frames run 1630 along the slope inside the rails' plan")
COMMAND = "CONVINCL"
PARAMS = dict()
W = 500.0                                        # between the side frames' inner faces (x +-250): design choice, conveyor-roller's
RUN = 1500.0                                     # the section's plan length, the floor rails y -750..750: design choice, conveyor-roller's length
ANG = 30.0                                       # the slope, degrees from the horizontal: design choice (a cleated belt carries loose goods up it)
CA, SA = math.cos(math.radians(ANG)), math.sin(math.radians(ANG))
SLF = 1630.0                                     # the frames' length along the slope: their sloped ends stay inside the rails' plan (tail top corner y -745, head underside corner y 746.6)
TAIL_TOP = 750.0                                 # the belt's top line over the tail end (y -750): the horizontal sections' track height
D = (0.0, CA, SA)                                # up the slope
N = (0.0, -SA, CA)                               # the slope's normal, up out of the belt
EX = (1.0, 0.0, 0.0)
BELT_T, BELT_END = 10.0, 13.4                    # the belt 10 thick, drawn as one plate by its outside; its ends 13.4 short of the frames' ends along the slope: conveyor-mattop's
BELT_GAP = 5.0                                   # the belt's edges 5 clear of the side frames (x +-245)
CLEAT_H, CLEAT_T, CLEAT_IN = 50.0, 2.5, 10.0     # cleats 50 high, 2.5 thick, 10 in from each belt edge (470 wide): design choice
CLEAT_PITCH, CLEATS = 250.0, 6                   # six cleats 250 apart along the slope, centred on the frames' midpoint
BED_T, BED_END = 10.0, 250.0                     # slider bed plate 10 thick under the belt, from 250 to SLF - 250 along the slope (40 clear of the pulleys' drums)
FR_W, FR_H = 50.0, 160.0                         # side frames 50 (x) by 160 (normal to the slope), drawn by their outside: design choice
FR_N = -10.0                                     # the frames' tops 10 below the belt's top (level with its underside): goods wider than the track pass over
XM_L, XM_H = 50.0, 40.0                          # cross members between the side frames under the bed plate: 50 along the slope, 40 deep (-60..-20)
PUL_S, PUL_N = 150.0, -90.0                      # the pulleys' axes 150 from the frames' ends along the slope, 90 below the belt's top
PUL_R, SH_R = 60.0, 20.0                         # drums Ø120 (tops 10 below the bed plate), shafts Ø40, drawn round: design choice
DRUM_X = 210.0                                   # the drums' end faces x +-210; the shafts run on to x +-245
SUP_Y = (-400.0, 500.0)                          # the two supports' centres (the posts' y): 900 apart
POST = 50.0                                      # posts 50 x 50 under each side frame, drawn by their outside
RL_W, RL_T = 150.0, 20.0                         # floor rails 150 (x) wide, 20 thick, 1500 long (y +-750), one under each side's posts, running outward
RL_X0 = W / 2 - 25.0                             # 225: a rail's inner edge, 25 inside the posts' inner faces; outer edge x 375
HOLE_X = W / 2 + POST + 40.0                     # 340: anchor hole centres x +-340, 40 outside the posts, 35 from the rail's outer edge
M12_D = 13.5                                     # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
TIE_LO = (150.0, 50.0)                           # lower tie between the posts: underside z 150, 50 deep
SEG = 6                                          # collider boxes per sloped part (axis-aligned steps along the slope)

def pt(s, n, x=0.0):
    """the point s along the slope from the frames' tail end and n along the normal from the belt's top line, at x"""
    return (x, -RUN / 2 + s * CA - n * SA, TAIL_TOP + s * SA + n * CA)

def s_at(y, n):
    """the slope coordinate s of the point at y on the line n from the belt's top line"""
    return (y + RUN / 2 + n * SA) / CA

def z_under(y):
    """z of the frames' underside (n = FR_N - FR_H) over y"""
    return TAIL_TOP + (FR_N - FR_H) * CA + s_at(y, FR_N - FR_H) * SA

def steps(P, name, s0, s1, n0, n1, x, dx):
    """axis-aligned collider boxes stepping along a sloped slab (s0..s1 along the slope, n0..n1 across it)"""
    for i in range(SEG):
        a, b = s0 + (s1 - s0) * i / SEG, s0 + (s1 - s0) * (i + 1) / SEG
        ys = [pt(s, n)[1] for s in (a, b) for n in (n0, n1)]; zs = [pt(s, n)[2] for s in (a, b) for n in (n0, n1)]
        P.collider(f"{name}-{i + 1}", x, min(ys), min(zs), dx, max(ys) - min(ys), max(zs) - min(zs))

def build():
    P = Prims(); S = "M-STEEL-7035"; Z = "M-ZINC"; K = "M-BLACK-PA"; C = "M-SILVER"   # belt and cleats black, drums bright steel
    x0 = W / 2                                                          # the frames' and posts' inner faces: x +-250
    n_fr = FR_N - FR_H                                                  # -170: the frames' undersides
    for sx, k in ((-1, "l"), (1, "r")):
        fx = x0 if sx > 0 else -x0 - FR_W
        P.obox(S, pt(0, n_fr, fx), EX, D, N, FR_W, SLF, FR_H)                                        # side frame, along the slope
        steps(P, f"frame-{k}", 0, SLF, n_fr, FR_N, fx, FR_W)
        rx = RL_X0 if sx > 0 else -RL_X0 - RL_W
        rl = P.box(S, rx, -RUN / 2, 0, RL_W, RUN, RL_T)                                              # floor rail, the section's full length
        P.collider(f"rail-{k}", rx, -RUN / 2, 0, RL_W, RUN, RL_T)
        for y, j in zip(SUP_Y, ("a", "b")):
            sp = s_at(y, n_fr)                                                                       # where the frame's underside passes the post's centre
            zt = z_under(y + POST / 2) + 20.0                                                        # the post drawn up past the frame, then cut to it
            po = P.box(S, fx, y - POST / 2, RL_T, POST, POST, zt - RL_T)                             # post, on the floor rail
            P.cut(S, pt(sp - 150, n_fr, fx - 1), EX, D, N, POST + 2, 300, 300, po)                   # its top cut to the frame's sloped underside
            P.hole(S, (sx * HOLE_X, y, -1), (sx * HOLE_X, y, RL_T + 1), M12_D / 2, rl)               # M12 anchor hole in the rail, beside the post
            P.collider(f"post-{k}{j}", fx, y - POST / 2, RL_T, POST, POST, z_under(y) - RL_T)
    for y, j in zip(SUP_Y, ("a", "b")):
        sp = s_at(y, n_fr)
        P.obox(S, pt(sp - XM_L / 2, -BED_T - BELT_T - XM_H, -x0), EX, D, N, W, XM_L, XM_H)           # cross member, frame to frame, under the bed
        ys = [pt(s, n)[1] for s in (sp - XM_L / 2, sp + XM_L / 2) for n in (-BED_T - BELT_T - XM_H, -BED_T - BELT_T)]
        zs = [pt(s, n)[2] for s in (sp - XM_L / 2, sp + XM_L / 2) for n in (-BED_T - BELT_T - XM_H, -BED_T - BELT_T)]
        P.collider(f"cross-{j}", -x0, min(ys), min(zs), W, max(ys) - min(ys), max(zs) - min(zs))
        P.box(S, -x0, y - POST / 2, TIE_LO[0], W, POST, TIE_LO[1])                                   # lower tie, post to post
        P.collider(f"tie-lo-{j}", -x0, y - POST / 2, TIE_LO[0], W, POST, TIE_LO[1])
    xs = x0 - BELT_GAP                                                  # the belt's and the bed's edges, the shafts' end faces: x +-245
    P.obox(S, pt(BED_END, -BELT_T - BED_T, -xs), EX, D, N, 2 * xs, SLF - 2 * BED_END, BED_T)         # slider bed plate, on the cross members
    P.obox(K, pt(BELT_END, -BELT_T, -xs), EX, D, N, 2 * xs, SLF - 2 * BELT_END, BELT_T)              # the belt's top run, one plate, on the bed
    steps(P, "belt-deck", BELT_END, SLF - BELT_END, -BELT_T, 0, -xs, 2 * xs)                         # what goods ride on
    xc = xs - CLEAT_IN
    for i in range(CLEATS):
        sc = SLF / 2 + (i - (CLEATS - 1) / 2) * CLEAT_PITCH
        P.obox(K, pt(sc - CLEAT_T / 2, 0, -xc), EX, D, N, 2 * xc, CLEAT_T, CLEAT_H)                  # cleat, standing on the belt
    for n, s in (("pulley-head", SLF - PUL_S), ("pulley-tail", PUL_S)):
        a = lambda x: pt(s, PUL_N, x)                                   # a point on the pulley's axis
        P.cyl(f"node:{n}|{Z}", a(-xs), a(-DRUM_X), SH_R)                                             # shaft, up to the drum's face
        P.cyl(f"node:{n}|{C}", a(-DRUM_X), a(DRUM_X), PUL_R)                                         # drum, a plain cylinder
        P.cyl(f"node:{n}|{Z}", a(DRUM_X), a(xs), SH_R)                                               # shaft, to its end face
        P.pivot(n, "rotate", a(-xs), axis=(1, 0, 0), range=(0, 360), unit="deg")                     # turns in its bearings (not drawn)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
