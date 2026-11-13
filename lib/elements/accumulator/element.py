#!/usr/bin/env python3
"""accumulator: a hydraulic bladder accumulator, 1 l nominal gas volume: an upright steel shell with stepped ends, the fluid port
block under it and the gas charging valve under a cap on top. A gas-filled bladder inside (not modelled) takes oil in against the
gas and gives it back when the circuit's pressure falls. lib/inventory.csv row `accumulator` (own_design generic, "hydraulic
accumulator (bladder)"; hpu-assembly-station). Generic (OPERATING.md 12, EM 2026-11-07 and 2026-11-08): the ETIM subset on file has
no class for it (its "Accumulator" synonyms are batteries), so it is generic by the standard whose rating quantities its Class
values follow, ISO 4413 (as hpu-7.5kw, valve-counterbalance, hyd-filter-return and hyd-cooler); no vendor file was opened. The shell, the
ends, the port block, the gas valve and its cap are design choices. The fluid port is a plain spot face, unit "hyd-port"
(toolkit/hyd.py H1: the dash size open), its thread a figure of SAE J1926-1 table 1 (class B, spec.md Open figures, not drawn). The
gas valve is no port of the circuit: it is charged with a charging set at commissioning, and no node is given to it. The bladder
and the fluid port's poppet inside are not modelled; nothing moves. No pressure-vessel code is on file and none is claimed."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import hyd, library
from toolkit.prims import Prims

ID, VERSION, CLASS = "accumulator", "1.0", "device"
TITLE = "hydraulic accumulator, generic, bladder type, 1 l nominal gas volume, 160 bar, upright, fluid port down"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic hydraulic bladder accumulator (no ETIM class; ISO 4413 values), 1 l nominal gas volume, "
            "160 bar by design (the relief pressure of the circuits on file); class values in spec.md; fluid port thread not on "
            "file (class B, not drawn); shell, ends, port block, gas valve and cap are design choices; no vendor file opened")
ORIGIN = ("the centre of the fluid port's face (the joint plane z = 0), the shell's axis along +z: upright, the fluid port down, "
          "the gas valve on top")
COMMAND = "ACCUMULATOR"
PARAMS = dict()

P_MAX_BAR = 160.0                          # class value 1 "max. operating pressure" (ratings.csv p_max): design, the circuits' relief pressure
V_NOMINAL_L = 1.0                          # class value 2 "nominal gas volume": design choice
SHELL_D, SHELL_L = 114.0, 150.0            # design choices: the shell, its axis along z
SHELL_WALL = 8.0                           # design choice: the shell's wall, for the volume only (the shell is modelled solid)
END_D, END_L = 90.0, 15.0                  # design choice: each rounded end, shown as a short Ø90 step
BLOCK_D, BLOCK_L = 50.0, 30.0              # design choice: the fluid port block under the lower end (the poppet inside, not modelled)
SPOT_D, SPOT_T = 32.0, 1.0                 # design choice: the fluid port's spot face, 1 proud of its block (hyd-filter-return's)
STEM_D, STEM_L = 16.0, 12.0                # design choice: the gas valve's stem on the upper end
CAP_D, CAP_L = 28.0, 28.0                  # design choice: the gas valve's protective cap, over the stem's end
IN = 0.5                                   # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_SHELL, MAT_BLOCK, MAT_SPOT, MAT_STEM, MAT_CAP = "M-STEEL-7035", "M-ZINC", "M-SILVER", "M-BRASS", "M-BLACK-PA"

Z_BLOCK = (SPOT_T, SPOT_T + BLOCK_L)                    # 1 to 31
Z_END_LO = (Z_BLOCK[1], Z_BLOCK[1] + END_L)             # 31 to 46
Z_SHELL = (Z_END_LO[1], Z_END_LO[1] + SHELL_L)          # 46 to 196
Z_END_HI = (Z_SHELL[1], Z_SHELL[1] + END_L)             # 196 to 211
Z_STEM = (Z_END_HI[1], Z_END_HI[1] + STEM_L)            # 211 to 223
Z_TOP = Z_STEM[1] + CAP_L                               # 251: the cap's top


def volume_l():
    """class value 2 "nominal gas volume": the shell's inside, Ø(114 - 2 x 8) over (150 - 2 x 8), in litres (the ends not counted)"""
    d, l = SHELL_D - 2 * SHELL_WALL, SHELL_L - 2 * SHELL_WALL
    return math.pi / 4 * d * d * l / 1e6


assert abs(volume_l() - V_NOMINAL_L) <= 0.05                         # 1.011 l: the nominal volume within 5 %
assert SPOT_D <= BLOCK_D - 2 * 6.0                                   # the spot face keeps 9 of block face round it
assert BLOCK_D < END_D < SHELL_D and STEM_D < CAP_D < END_D          # each part steps in from the one it sits on
assert P_MAX_BAR >= hyd.P_TANK                                       # H5: never rated under the tank line


def build():
    P = Prims()
    P.cyl(MAT_SHELL, (0, 0, Z_SHELL[0]), (0, 0, Z_SHELL[1]), SHELL_D / 2.0)                             # shell
    P.cyl(MAT_SHELL, (0, 0, Z_END_LO[0]), (0, 0, Z_END_LO[1] + IN), END_D / 2.0)                        # lower end, 0.5 into the shell
    P.cyl(MAT_SHELL, (0, 0, Z_END_HI[0] - IN), (0, 0, Z_END_HI[1]), END_D / 2.0)                        # upper end
    P.cyl(MAT_BLOCK, (0, 0, Z_BLOCK[0]), (0, 0, Z_BLOCK[1] + IN), BLOCK_D / 2.0)                        # fluid port block, 0.5 into the lower end
    P.cyl(f"node:port-oil|{MAT_SPOT}", (0, 0, 0.0), (0, 0, Z_BLOCK[0] + IN), SPOT_D / 2.0)              # spot face, 0.5 into the block
    P.pivot("port-oil", "port", (0, 0, 0.0), axis=(0, 0, -1), range=(0, 0), unit="hyd-port", gender="female")
    P.cyl(MAT_STEM, (0, 0, Z_STEM[0] - IN), (0, 0, Z_STEM[1]), STEM_D / 2.0)                            # gas valve stem, 0.5 into the upper end
    P.cyl(MAT_CAP, (0, 0, Z_STEM[1] - IN), (0, 0, Z_TOP), CAP_D / 2.0)                                  # its protective cap
    P.collider("body", -SHELL_D / 2.0, -SHELL_D / 2.0, 0.0, SHELL_D, SHELL_D, Z_TOP)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=20), dict(name="port end", az=225, el=-35), dict(name="gas valve", az=225, el=55)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
