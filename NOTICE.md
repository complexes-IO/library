# Notice

This library — its code (lib/toolkit, lib/build.py and the rest), its elements (lib/elements/*: specifications, behaviour,
parts, geometry), its assemblies and its documents — is released by Complexes Institute of Technology Inc. under the MIT
License (LICENSE; EM, 2026-11-09). "Software" in that licence means all of these files.

## Teaching material, not an engineering deliverable

Everything here is simulation and teaching material. Every figure is to be verified against the maker's documents and the
applicable codes and standards before anything is built, wired or energised from it. Nothing here is a safety device or a
safety design: the twin's safety functions are models of how such functions behave, not certified implementations. The
training pendant is marked "SIMULATION ONLY. NOT A SAFETY DEVICE" and so is everything the library produces.

## What is not part of the library

- Manufacturers' documents (datasheets, drawings, manuals, CAD files) referenced in the elements' briefs (references/) are
  not part of the library and remain their owners'. The elements are built from the figures those documents state, cited by
  page; no vendor file is copied into the repository (CONTRIBUTING.md). Manufacturers' names and part numbers appear only
  in references/ as the record of what was read.
- The text and tables of standards (ISO, IEC, ASME, NFPA, NEC, UL and others) are not part of the library. The library cites
  clauses and derives figures from the formulas they publish (lib/toolkit/derive.py); it reproduces no standard's text.
- The names "Complexes Institute of Technology", "complexes.org", "RobotPad" and the institute's marks are not licensed by
  the MIT License; they are the institute's (see its trademark filing).

## Third-party content in the library and its terms

What the library ships that is not ours, and the obligation each carries (lib/standards/sources.csv is the full register):

- **ETIM International classification, ETIM 10.0** (lib/standards/etim/: a subset of the classes and features): Open Data Commons
  Attribution Licence, ODC-BY 1.0. Attribution to ETIM International stays with the data wherever it goes; the MIT License does
  not re-license it. ETIM's own notice is lib/standards/etim/README.md.
- **FED-STD-H28/2B and /7A** (lib/standards/un-threads.csv and the toolkit's NPT values): United States federal standards, public
  domain. Cited by table.
- **US federal regulations** cited (OSHA 29 CFR 1910, NEC values where quoted as facts): public domain; the NEC's text is not
  reproduced (NFPA's).
- **Nothing else of a third party ships**: no vendor file, no standard's text, no KiCad symbol or 3D model, no BOLTS table (should
  one be taken in, its own licence travels with the file and is recorded in sources.csv).

Tools the library runs on but does not ship, each under its own licence: Python and numpy (PSF, BSD), pywin32 (PSF-style),
Godot (MIT), Blender (GPL: our scripts that import bpy are MIT, a GPL-compatible licence), KiCad (GPL), AutoCAD (Autodesk's
commercial licence; our LISP and DWG files are ours), draw.io (Apache 2.0). The Rust core (lib/core) is ours, MIT.
