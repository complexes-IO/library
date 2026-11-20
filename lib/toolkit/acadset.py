"""AutoCAD's settings as a gate leaves them (ESCAPE lib/reviews/pneu/r100.md finding 2; core watch 2026-11-14).

EM's round 9 rule: a script leaves AutoCAD's settings as it found them. acad-gate.py remembers TRUSTEDPATHS at its start and puts that
back, and `trustedpaths_restored_ok` compares with that start. A run stopped by a watchdog may not get its own folder out; the next run
then finds it there, records it as found and puts it back, so the folder stays trusted for good. valve-gauge-double 1.1's retry
(pneu-r100) found 55 entries, 50 of them library gate or out folders left by earlier stopped runs. "As found" cannot heal a leftover.

The rule here: what a gate puts back is what it found, less every element or assembly gate/ or out/ folder of a library worktree
(<worktree>\\lib\\elements\\<id>\\gate|out, <worktree>\\lib\\assemblies\\<id>\\gate|out, either slash, any case). A gate adds its own folder
for its run only, so no such folder is ever EM's. Everything else (EM's own folders, lib\\out) goes back untouched, in its order.
acad-gate.py (the library's file) calls restore_value() in restore_settings and compares what it reads back with it (round 38 A3).
"""
import re

_GATE_DIR = re.compile(r"[\\/]lib[\\/](elements|assemblies)[\\/][^\\/;]+[\\/](gate|out)[\\/]?$", re.I)


def is_gate_folder(path):
    """True for an element's or assembly's gate/ or out/ folder of a library worktree: a folder a gate adds for its run only."""
    return bool(_GATE_DIR.search(path.strip()))


def split(trusted):
    """TRUSTEDPATHS -> (kept, dropped), each a list in its order; empty entries dropped silently."""
    kept, dropped = [], []
    for p in (trusted or "").split(";"):
        if not p.strip():
            continue
        (dropped if is_gate_folder(p) else kept).append(p)
    return kept, dropped


def restore_value(trusted):
    """What a gate puts TRUSTEDPATHS back to: what it found, less the gate and out folders earlier runs left (split's kept)."""
    return ";".join(split(trusted)[0])


def leftovers(rep):
    """A gate result's left-over gate folders: those in its trustedpaths_before (what the run found). [] when clean or not recorded."""
    return split((rep or {}).get("trustedpaths_before") or "")[1]
