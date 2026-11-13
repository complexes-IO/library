"""complexes component library · toolkit. The only thing an element may import.
Conventions: millimetres, Z up, right-handed. Layer "M-<material>" or "node:<name>|M-<material>" (on disk: node-<name>_M-<material>).
Elements record the toolkit version they were last built with; bump VERSION when a change alters what an element builds."""
VERSION = "1.3"
VALIDATION = "1.0"   # the validation suite (validate.py and the v_*.py checkers); it reads what elements build and never changes it
