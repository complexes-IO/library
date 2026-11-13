"""The M12 interface: what both halves of a screw-locked M12 joint share (IEC 61076-2-101 A and D coding; IEC 61076-2-111 L coding).
Elements that make up a joint (contacts, inserts, nuts, seals, receptacles, plugs) take their figures from here, so two halves built
by different elements still meet. Frames: every part is built in its MATING FRAME: the mating plane at y = 0 (where the male carrier
face meets the female insert face at the seat), the counterpart toward -y, the part's body toward +y, the key toward +z.

The thread follows the gender (1.2):
  male    pins on a carrier inside a SLEEVE that carries the external M12 x 1 thread: a cable's coupling nut, or a device's fixed sleeve.
  female  sockets in an insert that is the FOREMOST face of the half (1.3); the threaded bore round it starts behind that face, in a
          cable's coupling nut or a device's housing.
Each half comes in two KINDS with their own figures: "cordset" (a cable end: the cordset drawings and STEP files, Open CASCADE
read-back, round 4) and "device" (a receptacle in a housing: the I/O block's STEP, Open CASCADE read-back, round 4).
Both threads are modelled plain at r 5.46, so the halves touch and never overlap; the real male thread is Ø12. Where the threads
engage comes from the two halves together (thread_span), not from one figure.
1.4 (round 5 figures, Open CASCADE): the D poles and notches in this module's own sense (the I/O block manual's pole numbers, the
the D cordset drawing's), the L key block and recess outlines, the A male nut's profile.
1.6 (round 7): the cordset female L recess takes X04's outline (its own STEP's does not fit its male); M12-010 checks every pair.
1.5 (round 6 figures, Open CASCADE face wires): D keying as it is (a tooth between flat notches and a slot on the female; a channel
through a chord and a flat rib on the male), the key tolerance per coding from each keyway's own clearance, the I/O block's X03 block and X04's
recess outlines, the D and L male nuts and bodies.
Figures marked Assumption are NOT ON FILE; every other figure names its source."""
import math

THREAD, PITCH = "M12x1", 1.0           # M12 x 1 (ISO 261; drawings 'M12X1')
THREAD_R = 5.46                        # both threads, modelled plain at the internal thread's minor radius (Ø10.917 device; Ø11.0 cordset)
TORQUE = (0.5, 0.6)                    # N m: 0.5 maker's datasheet: the I/O block's technical data p. 2; 'max. 0.6 Nm' cordset catalogues p. 2
KEY_TOL = None                         # deg: set below from the key and keyway (1.3: was 5.0, an Assumption the pins contradicted)
KINDS = ("cordset", "device")

# male half (OCC read-back: the A and D cordsets' males; the L cordset's male; the I/O block's X03 L male)
MALE = {
    "cordset": dict(reach={"A": 8.9, "D": 8.9, "L": 8.8},              # sleeve front ahead of the carrier face
                    bore={"A": 4.15, "D": 4.15, "L": 4.4},             # sleeve bore r: Ø8.3, Ø8.8
                    thread={"A": (0.9, 5.95), "D": (0.9, 5.95), "L": (1.2, 6.439)},   # (behind, ahead of) the carrier face
                    face={"A": 1.4, "D": 1.4, "L": 1.2}),              # where the knurl starts behind the carrier face (OCC: the A cordset,
                                                                       # the D and L cordsets)
    "device": dict(reach={"A": 8.9, "D": 8.9, "L": 8.9},               # X03: front 8.9 ahead of the carrier face
                   bore={"A": 4.15, "D": 4.15, "L": 4.45},             # X03: Ø8.9
                   thread={"A": (0.9, 5.95), "D": (0.9, 5.95), "L": (3.7, 7.94)},     # X03: from the housing face (0.5 out) to 12.14 out
                   face={"A": 1.4, "D": 1.4, "L": 4.2})}               # the housing face behind the carrier face: X03 4.2; A / D Assumption
KNURL = {"A": 7.5, "D": 7.5, "L": 8.95}          # coupling nut knurl: Ø15 (A / D), Ø17.9 (L)
KNURL_L = 4.8                                    # a male nut's body behind the knurl's front, where MALE_NUT has no figures: Assumption
MALE_NUT = {"A": dict(collar=(0.9, 1.4, 7.0), knurl=(1.4, 3.9, 7.5), hex=(3.9, 6.4, 6.5, 7.2)),
            "D": dict(collar=(0.9, 1.4, 7.0), knurl=(1.4, 3.9, 7.5), hex=(3.9, 6.4, 6.5, 7.2)),
            "L": dict(collar=None, knurl=(1.2, 5.2, 8.95), hex=(5.2, 8.7, 8.45, 8.95))}
                                                 # D: the A nut to 0.01 (the D cordset, OCC, round 6). L (the L cordset, round 6): the nut's front
                                                 # face at 1.2 out to Ø17.9, Ø17.9 to 5.2, a 16.9 hex with its corners turned to Ø17.9 to
                                                 # 8.15, a 60° chamfer to the back face at 8.7 (the chamfer modelled square)
                                                 # the A male nut behind the carrier face (the A cordset, OCC, round 5): front face 0.9 with
                                                 # its 45° chamfer Ø14 -> Ø15 to 1.4 (modelled as a Ø14 collar), knurl Ø15 1.4 to 3.7 with
                                                 # an r 0.2 round to 3.9, hex 13.0 across flats with its corners turned to Ø14.4 from 3.9
                                                 # to 6.2, back face 6.4 (the 6.2-6.4 chamfer modelled square)
KEY = dict(d=1.2, r=3.55, reach=8.4)             # A key peg Ø1.2 on r 3.55, its front 8.4 ahead (the A cordset, OCC); D ribs run as far
KEYS = {"A": (0.0,), "D": (0.0, 106.5)}         # female-face angles, clockwise from +z: A the keyway (its peg's) centreline; D the tooth's
                                                 # and the slot's (D_KEY)
D_KEY = dict(tooth=0.9, floor=3.127, slot=(106.5, 0.5, 3.292), deep=8.7, chord=3.25, channel=1.0, rib=(0.45, 3.40))
                                                 # D (OCC face wires, round 6; round 5's ±25.76° / 106.09° were face mid-points):
                                                 #  female (the I/O block's X01): a tooth 1.80 wide on the 0° line standing to the insert's edge,
                                                 #  flat notches either side with their floors on one chord 3.127 from the axis; a slot 1.00
                                                 #  wide on the 106.5° line, its floor 3.292 from the axis; both 8.7 deep.
                                                 #  male (the D cordset): a chord 3.250 from the axis across the 0° line, cut by a 2.00 channel
                                                 #  (two blocks out to the sleeve bore; round 5's "V ribs" are their inner corners at r 3.40);
                                                 #  a flat rib 0.90 wide on the 106.5° line, its top 3.400 from the axis.
                                                 #  Clearances 0.10 / 0.12 / 0.05 / 0.11
KEY_GAP = KEY["reach"]                           # a key that does not fit meets the female insert face this far off the seat
KEY_TOL = round(math.degrees(math.asin((1.3 - KEY["d"]) / 2 / KEY["r"])), 3)   # A, 0.807°: the Ø1.2 peg turns no further in the Ø1.3
                                                 # keyway on r 3.55 (OCC). At 5° the pins on r 2.5 sit 0.22 off their sockets and stop
                                                 # on the face, so a key "within tolerance" could not seat (found writing the Kani proof).
                                                 # D and L: key_tol()
L_KEY = dict(back=0.8, recess={"cordset": 8.2, "device": 8.5}, flank=20.0,
             block={"cordset": dict(chord=1.5, feet=(-1.036, 1.036), tops=((-1.6, 3.05), (1.6, 3.05))),
                    "device": dict(chord=1.448, feet=(-1.084, 1.087), tops=((-1.648, 2.999), (1.651, 2.998)))},
             pocket={"cordset": dict(chord=1.369, feet=(-1.167, 1.205), tops=((-1.731, 2.919), (1.770, 2.922))),
                     "device": dict(chord=1.369, feet=(-1.167, 1.205), tops=((-1.731, 2.919), (1.770, 2.922)))})
                                                 # L (the L cordset, OCC, round 5), in a half's own face view with FE up (+z):
                                                 #  male key block: a flat chord 1.5 from the axis (X03: 1.448), flanks leaning 20° out to
                                                 #  (±1.6, 3.05); on the +x side a ledge at z 3.05 out to the bore, on the -x side a wall
                                                 #  x -1.6 up to the bore: 67.4° of the bore, not symmetric about FE. Its face 0.8 behind
                                                 #  the sleeve front, the FE socket in it.
                                                 #  female recess: the same outline 0.1 larger (chord 1.4, flanks to (±1.7, 3.352)), the
                                                 #  ledge on the female's -x side (the male's +x side meets it), 8.2 deep (X04: 8.5).
                                                 #  X03 (round 6): chord 1.448, flanks and wall 0.05 further out, ledge 2.998. X04 (round 6):
                                                 #  chord 1.369 with its feet at -1.167 / +1.205, ledge 2.919, wall 1.770, 8.5 deep (no
                                                 #  radial grooves). The cordset female's radial grooves 4.0 deep are not modelled.
                                                 #  Outlines are (feet u at the chord, flank tops (u, v)), u across the key, + clockwise.
                                                 #  1.6 (round 7): the cordset female's keyway as read (chord 1.4, tops ±1.7 at 3.352) does
                                                 #  not fit its own male: an exact boolean of the L cordset's halves as they mate leaves
                                                 #  3.375 mm³ in common (the male's foot 0.302 inside the female's ledge), and the drawing
                                                 #  dimensions neither. It takes X04's measured outline instead (Assumption), which clears
                                                 #  the cordset male by 0.131 and X03 by 0.079

# female half (OCC read-back: the A cordset's female; the L cordset's female; the I/O block's X1-X8, X01 / X02, X04)
FEMALE = {
    "cordset": dict(face={"A": 1.5, "D": 1.5, "L": 1.3},               # the nut's front face behind the insert face
                    thread={"A": (2.1, 9.0), "D": (2.1, 9.0), "L": (1.589, 10.3)},    # internal thread (from, to) behind the insert face
                    depth={"A": 9.0, "D": 9.0, "L": 10.5}),            # insert front: from the bore floor to the insert face
    "device": dict(face={"A": 3.4, "D": 3.4, "L": 3.4},                # the housing face behind the insert face (the insert stands 3.4 proud)
                   thread={"A": (4.5, 9.4), "D": (4.5, 9.4), "L": (4.5, 9.4)},       # the Ø10.917 cylinder, 1.1 to 6.0 behind the housing face
                   depth={"A": 9.5, "D": 9.5, "L": 9.5},
                   counterbore=(6.15, 1.1))}                           # Ø12.3 entry (with its 60° cone) to 1.1 behind the housing face
INSERT_R = {"A": 4.1, "D": 4.1, "L": 4.35}       # female insert front: Ø8.2 (A), Ø8.7 (L); D as A
KEYWAY = dict(d=1.3)                             # keyway / notch Ø1.3 on r 3.55 along the insert front's edge (A: the A cordset and the I/O block)

# contacts
GUIDE = {"A": 1.05, "D": 1.05, "L": 1.6}         # contact entry Ø at the female face (the I/O block's read-back)
CAVITY = {"A": 1.65, "D": 1.65, "L": 2.1}        # counterbore behind the entry: the socket contact's seat (read-back)
CHAMFER = {"A": 2.0, "D": 2.0, "L": 2.4}         # entry chamfer Ø at the face (A / D read-back; L Assumption)
PCD = {"A": 5.0, "D": 5.0, "L": 5.88}            # pitch circle of the outer poles (read-back and OCC)
LAYOUT = {                                       # pole: degrees from the key, clockwise looking at the female face; None = centre
    "A": {"1": 315, "2": 45, "3": 135, "4": 225, "5": None},   # the A cordset drawing, Detail A: clockwise from the key 2, 3, 4, 1; 5 centre
    "D": {"1": 315, "2": 45, "3": 135, "4": 225},              # maker's datasheet: the I/O block's manual p. 32 Fig. 5 and the D cordset drawing (round 5):
                                                               # the notch pair between 1 and 2, the single notch between 2 and 3
    "L": {"5": 0, "1": 72, "2": 144, "3": 216, "4": 288}}     # 72° apart on Ø5.88, FE at the key (X03 / X04, cordset L pair)
REVERSED = {"L": ("5",)}                         # poles whose gender is the other half's: L-coded FE is a pin in the female, a socket in the male
COLOUR = {"A": "M-BLACK-PC", "D": "M-GREEN", "L": "M-GREY-PA"}    # coding colour (maker's datasheet: the I/O block's manual p. 32-34 colour coding)
CONTACT_D = {"A": 1.0, "D": 1.0, "L": 1.5}       # pin Ø (drawings, OCC)
PIN = {"A": (6.9, 0.45), "D": (6.9, 0.45), "L": (5.4, 0.6)}       # (protrusion ahead of the carrier face, rounded tip): A / D 6.45 + 0.45;
                                                                   # L 4.8 + 0.6 (OCC)
FE_L = dict(pin=(8.0, 0.7), below=0.2, bore=1.85, deep=8.0)       # L FE: the female's pin 7.3 + a 0.7 tip, its tip 0.2 below the insert
                                                                   # face; the male's socket a Ø1.85 bore 8.0 deep in the key block (OCC)
SOCKET = dict(mouth=1.0, spring=0.5, bottom={"A": 6.0, "D": 6.0, "L": 7.0})   # mouth 1.0 below the face (read-back); bore bottom 7.0
                                                                   # below the face (A holes 7.0 deep, OCC); L Assumption; springs Assumption
SEAL = dict(squeeze=0.2)                         # NOT ON FILE (no seal in any file on hand): modelled as a flat ring on the female's bore
                                                 # floor round the insert, pressed by the male sleeve's front: Assumption
INSERT_L = {"female": {"A": 1.0, "D": 1.0, "L": 2.5}, "male": {"A": 8.0, "D": 8.0, "L": 10.0}}   # female: the base behind the bore floor
                                                 # (L: room for the FE pin's collar); male: the carrier. Assumption
WIPE, R_CONTACT = 0.5, 5.0                       # mm of overlap for a reliable contact; mΩ per contact: Assumption

def insert_l(gender, coding, kind="cordset"):
    """the insert's length behind the mating plane: a female's front and base, a male's carrier (a cordset A carrier fills its
    sleeve to the nut's back face, 6.4: the plug body's Ø8.4 neck starts there, the A cordset)"""
    if gender == "female": return FEMALE[kind]["depth"][coding] + INSERT_L["female"][coding]
    if kind == "cordset" and coding in MALE_NUT: return MALE_NUT[coding]["hex"][1]
    return INSERT_L["male"][coding]

def male(kind, coding, what):
    return MALE[kind][what][coding]

def female(kind, coding, what):
    return FEMALE[kind][what][coding]

def front(gender, coding, kind="cordset"):
    """how far a half's foremost point stands ahead of its mating plane (toward -y): the male sleeve; 0 for a female (its insert face)"""
    return MALE[kind]["reach"][coding] if gender == "male" else 0.0

def face(gender, coding, kind="cordset"):
    """how far a half's nut or housing face sits BEHIND its mating plane (toward +y)"""
    return (MALE if gender == "male" else FEMALE)[kind]["face"][coding]

def thread_span(gender, coding, kind="cordset"):
    """the thread along the mating axis as (lo, hi) measured AHEAD of the mating plane (toward the counterpart)"""
    if gender == "male": b, a = MALE[kind]["thread"][coding]; return (-b, a)
    s, e = FEMALE[kind]["thread"][coding]; return (-e, -s)

def engagement(male_span, female_span):
    """(the gap off the seat at which the threads first catch, the length engaged at the seat), from the two halves' spans. At the
    seat a point `a` ahead in the male sits at -a ahead in the female; backing the male off by g moves it to -a + g."""
    m_lo, m_hi = male_span; f_lo, f_hi = female_span
    return round(f_hi + m_hi, 3), round(min(-m_lo, f_hi) - max(-m_hi, f_lo), 3)

def seal_thick(coding, kind="cordset", male_kind="cordset"):
    """the floor seal fills the female's bore floor to the male sleeve's front, plus its squeeze"""
    return round(FEMALE[kind]["depth"][coding] - MALE[male_kind]["reach"][coding] + SEAL["squeeze"], 3)

def nut_back(coding):
    """where a male cordset nut's back face sits behind the carrier face: the A nut's measured hex end, else the Assumption"""
    if coding in MALE_NUT: return MALE_NUT[coding]["hex"][1]
    return MALE["cordset"]["face"][coding] + KNURL_L

def key_outline(coding, gender, kind="cordset"):
    """the L key block (male) or recess (female) outline in the half's own frame (x across, z out along the key): (chord z, feet
    (x-, x+) on the chord, flank tops ((x, z) on the -x side, (x, z) on the +x side), ledge side +1 / -1 along x). The male's ledge is
    on its +x side, its wall on -x; the female's ledge on its -x side, its wall on +x, so the two meet. u in the figures runs
    clockwise looking at the face, which is +x in the frame."""
    d = L_KEY["block" if gender == "male" else "pocket"][kind]
    return d["chord"], d["feet"], d["tops"], (1 if gender == "male" else -1)

def key_tol(coding, gender="female", kind="device"):
    """the angle a half's key turns before it meets its counterpart's keyway (deg), with the counterpart of the other kind (a device's
    port meets a cordset's plug, a cordset half another cordset's): A the peg (KEY_TOL); D the rib in the slot, the tighter of D's two
    fits; L the block's wall against the recess's wall, the tighter of L's fits. Each is the side clearance over the outermost radius
    the two share."""
    if coding == "A": return KEY_TOL
    if coding == "D":
        a, w, floor = D_KEY["slot"]; r_ = math.sqrt(INSERT_R["D"] ** 2 - w ** 2)
        return round(math.degrees(math.asin((w - D_KEY["rib"][0]) / r_)), 3)
    other = "cordset" if kind == "device" else ("device" if gender == "male" else "cordset")
    mk, fk = (kind, other) if gender == "male" else (other, kind)
    wall_m = -L_KEY["block"][mk]["tops"][0][0]; wall_f = L_KEY["pocket"][fk]["tops"][1][0]; r_ = math.sqrt(INSERT_R["L"] ** 2 - wall_f ** 2)
    return round(math.degrees(math.asin((wall_f - wall_m) / r_)), 3)

def key_r(coding):
    """the key's radius from the axis: on the sleeve wall (A / D 3.55)"""
    return MALE["cordset"]["bore"][coding] - KEY["d"] / 2

def gender_of(coding, pole, half):
    """'pin' or 'socket' for a pole of a male or female half (L-coded FE is reversed)"""
    pin = half == "male"
    if str(pole) in REVERSED.get(coding, ()): pin = not pin
    return "pin" if pin else "socket"

def pole_xz(coding, pole, gender):
    """(x, z) of a pole in a part's mating frame. Looking at the female face from the front (from -y), clockwise from the key (+z);
    a male face is its mirror image, so pin n lands on socket n when the halves meet (the plug turns 180° about z to face the port)."""
    a = LAYOUT[coding][str(pole)]
    if a is None: return (0.0, 0.0)
    return ang_xz(a, PCD[coding] / 2, gender)

def ang_xz(a, r, gender):
    """(x, z) of a point at angle a (female-face degrees, clockwise from +z) and radius r, in a female or (mirrored) male frame"""
    th = math.radians(a); x = r * math.sin(th); z = r * math.cos(th)
    return (x if gender == "female" else -x, z)

def port_data(coding, gender, kind="cordset"):
    """the extras a mating face carries (pivot kind port): what toolkit/contact.py and the twin's binder need. thread_span is this
    half's thread ahead of its mating plane; thread_gap is where it catches against the other kind's standard half (the binder's
    default; contact.mate() works it out from both halves)"""
    mine = thread_span(gender, coding, kind); other = thread_span("female" if gender == "male" else "male", coding, "cordset")
    ms, fs = (mine, other) if gender == "male" else (other, mine)
    return dict(gender=gender, coding=coding, half=kind, keyref=(0.0, 0.0, 1.0), key_tol=key_tol(coding, gender, kind), key_gap=KEY_GAP, thread=THREAD, pitch=PITCH,
                thread_span=mine, thread_gap=engagement(ms, fs)[0], seal=SEAL["squeeze"], torque=TORQUE)

def parse_conditions(s):
    """'2:bent/4:pushed-back' -> {'2': 'bent', '4': 'pushed-back'} (a BOM params cell separates its keys with ';', so poles take '/')"""
    out = {}
    for part in str(s or "").replace(",", "/").replace(";", "/").split("/"):
        if ":" in part: k, v = part.split(":", 1); out[k.strip()] = v.strip()
    return out
