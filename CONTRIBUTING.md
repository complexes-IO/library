# Contributing

Thank you for helping. Everything here is checked by machines first and by people second, so a contribution is welcome even if
it is small.

## Pick something

- **An element:** the [wanted issues](../../issues?q=is%3Aissue+is%3Aopen+label%3Awanted). Comment `/claim` to take one; nobody
  else, person or AI lane, starts it while it is yours. `/unclaim` gives it back. Fourteen days with no activity releases it.
- **A figure:** an element's `spec.md` marks what is `NOT ON FILE` or an `Assumption`. If you hold the datasheet or the standard,
  open an issue with the figure, the document, its clause or page.
- **A review:** read an element against its datasheet and its behaviour and open an issue with what you find.

## The rules an element follows

1. **Every figure has a source.** A standard's clause, a datasheet's page, a calculation from a standard's formula, or "our own
   design" with the reason. A figure with no source is written `NOT ON FILE`, never guessed.
2. **No maker's material.** No maker's name, part number, logo or CAD file goes in an element. You may measure from a maker's
   drawing; the figures you take are cited by page in `references/measure.md`, and the file itself stays with you.
3. **Code builds geometry and nothing else.** `element.py` imports the toolkit, `math`, `numpy`, `csv`, `json`, and `os.path`
   only. No file writes, no network, no `eval`. The `guard` check refuses anything else.
4. **Source only.** Send `.py .md .csv .json` files. The build makes the models (`out/`); the library's own machines run the
   AutoCAD, Blender and Godot checks.
5. **The id names the class:** `class[-form][-size][-function]`, e.g. `relay-safety-2ch-2no1nc`.

## Send it

```
python lib/build.py <your-element-id>     # builds it and runs its checks: ALL PASS
python lib/build.py guard main            # what your branch brings in: 0 refused
git commit -s -m "<id> 1.0: <what it is>"  # -s signs the Developer Certificate of Origin
```

Open a pull request that says `Closes #<the wanted issue>`. The `guard` check runs on it; a first-time contributor's checks start
when a maintainer approves the run. A reviewer and CIT's engineer audit the element before it is released.

By signing off (`-s`) you certify the [Developer Certificate of Origin](https://developercertificate.org): you wrote the change,
or have the right to submit it, under the MIT License.
