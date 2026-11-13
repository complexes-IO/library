# Complexes Institute of Technology · Element Library

Industrial automation components (contactors, relays, sensors, valves, cylinders), each modelled from its standards with its
behaviour specified. Machines, panels and lab rooms are built from them, and a digital twin runs them.

## An element

`lib/elements/<id>/`: `element.py` (geometry), `spec.md` (every figure and its source), `ratings.csv`, `behaviour.csv`,
`out/` (the built model). Ids name the class, never a product: `contactor-9a-1no1nc`.

## Try it

```
pip install numpy matplotlib
python lib/build.py contactor-9a-1no1nc
```

Open `out/*.glb` in any glTF viewer.

## Help

Pick an element from the [wanted list](../../issues?q=is%3Aissue+is%3Aopen+label%3Awanted) and comment `/claim`.
See CONTRIBUTING.md.

## Licence

MIT, © 2026 CIT. Teaching material: verify every figure before you build from it (NOTICE.md).
