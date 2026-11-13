"""What a contribution may bring in (EM 2026-11-12, before the library goes public: "how do we prevent files with virus etc..?").

Two checks on the files a branch or a pull request changes against its base (`python lib/build.py guard [base] [--external]`):

GRD-010  files: every changed file in an element's or an assembly's folder (in a pull request from outside: every changed file)
         is a type the library holds, and is what its name says.
         - text: .py .md .csv .json .txt .svg .gitkeep, utf-8, no NUL byte; an .svg carries no script, event handler, external
           reference or foreignObject (a browser runs those)
         - built: .png .glb .lsp only under an element's or assembly's out/, gate/, qa/ or thumbs/ (the build and the gates write
           them), each with its format's signature (PNG, glTF); a .lsp is AutoCAD code and is only ever written by the toolkit
         - nothing else (no .exe .dll .bat .ps1 .zip .docx .pdf .dwg ...), no source file over 2 MB (a built one 25 MB), no symbolic link
         - --external (a pull request from outside the lanes): no built file at all (the library builds them), and only
           element and assembly folders; the toolkit, the rules, the workflows and the line's files are the core's
GRD-020  code: every changed .py under lib/elements/ or lib/assemblies/ builds geometry and nothing else. Its imports are the
         toolkit, math, numpy, csv, json, and os / sys for their path helpers only; no call to eval, exec, compile, __import__,
         getattr / setattr / delattr, globals, locals, vars, input or breakpoint; no dunder attribute but __file__ and __name__;
         open() only to read (no mode, or 'r' / 'rb'); sys.modules only as sys.modules[__name__] (the element handing itself to
         the toolkit). An assembly may also use importlib (it loads its sub-assemblies), os.makedirs, and open() to write inside its
         `if __name__ == "__main__":` block or into os.path.join(OUT, ...), its own out/ folder (its outputs).
A static check is not a sandbox: Python can be bent past one. The sandbox is the pull-request workflow (GitHub's machine, no
secrets, read-only token, approval for first-time contributors); this check makes a bad file fail loudly there and on every lane
merge, and keeps anything but geometry out of the code the PC runs.
"""
import ast, os, re, subprocess

TEXT = {".py", ".md", ".csv", ".json", ".txt", ".svg", ".gitkeep"}
BUILT = {".png": b"\x89PNG\r\n\x1a\n", ".glb": b"glTF", ".lsp": None}
BUILT_DIRS = {"out", "gate", "qa", "thumbs"}
MAX = 2 * 1024 * 1024; MAX_BUILT = 25 * 1024 * 1024        # a source file; a built one (a machine's glb runs past 2 MB)
IMPORTS = {"toolkit", "math", "numpy", "csv", "json", "os", "sys"}
OS_OK = {"path"}; SYS_OK = {"path", "argv", "exit"}
CALLS = {"eval", "exec", "compile", "__import__", "getattr", "setattr", "delattr", "globals", "locals", "vars", "input", "breakpoint"}
DUNDER_OK = {"__file__", "__name__"}
SVG_BAD = re.compile(r"<\s*script|\bon[a-z]+\s*=|<\s*foreignObject|javascript:|(?:xlink:)?href\s*=\s*[\"'](?!#)", re.I)


def _ext(p):
    b = os.path.basename(p)
    return ".gitkeep" if b == ".gitkeep" else os.path.splitext(b)[1].lower()


def file_findings(path, data, external=False, is_link=False):
    """[(status, rule, where, message)] for one changed file (repo-relative path, its bytes)"""
    out = []; ext = _ext(path); parts = path.replace("\\", "/").split("/")
    if is_link: return [("FAIL", "GRD-010", path, "a symbolic link: the library holds files only")]
    library = len(parts) > 2 and parts[0] == "lib" and parts[1] in ("elements", "assemblies")
    if not external and not library: return []                                 # the toolkit, the gates, the workflows: their owners' (OWNERS.csv)
    in_built = len(parts) > 3 and parts[0] == "lib" and parts[1] in ("elements", "assemblies") and parts[3] in BUILT_DIRS
    cap = MAX_BUILT if in_built else MAX
    if len(data) > cap: out.append(("FAIL", "GRD-010", path, f"{len(data) // 1024} kB: over the {cap // 1048576} MB a {'built' if in_built else 'source'} file may be"))
    if ext in TEXT:
        if b"\x00" in data: out.append(("FAIL", "GRD-010", path, "a NUL byte in a text file: binary content under a text name"))
        else:
            try: txt = data.decode("utf-8")
            except UnicodeDecodeError: out.append(("FAIL", "GRD-010", path, "not utf-8 text")); txt = ""
            if ext == ".svg" and SVG_BAD.search(txt): out.append(("FAIL", "GRD-010", path, f"the drawing carries something a browser runs or fetches ({SVG_BAD.search(txt).group(0)[:30]})"))
        if external and in_built: out.append(("FAIL", "GRD-010", path, "a built file: the library builds out/, gate/, qa/ and thumbs/ itself; leave them out of the pull request"))
    elif ext in BUILT:
        if not in_built: out.append(("FAIL", "GRD-010", path, f"a {ext} outside an element's or assembly's out/, gate/, qa/ or thumbs/: only the build writes these"))
        elif external: out.append(("FAIL", "GRD-010", path, f"a built {ext}: the library builds it itself (and a .lsp is AutoCAD code); leave it out of the pull request"))
        sig = BUILT[ext]
        if sig and not data.startswith(sig): out.append(("FAIL", "GRD-010", path, f"named {ext} but not one (its first bytes are not the format's signature)"))
    else:
        out.append(("FAIL", "GRD-010", path, f"a {ext or 'file with no extension'}: not a type the library holds (text: {' '.join(sorted(TEXT))}; built by the library: .png .glb .lsp)"))
    if external and not (len(parts) > 2 and parts[0] == "lib" and parts[1] in ("elements", "assemblies")):
        out.append(("FAIL", "GRD-010", path, "outside lib/elements/ and lib/assemblies/: the toolkit, the rules, the workflows and the line's files are the core's (a request, lib/requests/)"))
    return out


def code_findings(path, text):
    """GRD-020 for one .py under lib/elements/ or lib/assemblies/"""
    out = []; asm = "/assemblies/" in path.replace("\\", "/")
    try: tree = ast.parse(text)
    except SyntaxError as e: return [("FAIL", "GRD-020", path, f"does not parse: {e.msg} (line {e.lineno})")]
    mods = {}
    parent = {c: p for p in ast.walk(tree) for c in ast.iter_child_nodes(p)}
    def in_main(n):                                                            # inside `if __name__ == "__main__":` (writes the outputs)
        while n in parent:
            n = parent[n]
            if isinstance(n, ast.If) and isinstance(n.test, ast.Compare) and isinstance(n.test.left, ast.Name) and n.test.left.id == "__name__": return True
        return False
    def self_ref(n):                                                           # sys.modules[__name__]: the element passing itself to the toolkit
        p = parent.get(n)
        return isinstance(p, ast.Subscript) and isinstance(p.slice, ast.Name) and p.slice.id == "__name__"
    def to_out(n):                                                             # open(os.path.join(OUT, ...)): an assembly's own out/ folder
        f = n.args[0] if n.args else None
        return (isinstance(f, ast.Call) and isinstance(f.func, ast.Attribute) and f.func.attr == "join" and f.args
                and isinstance(f.args[0], ast.Name) and f.args[0].id == "OUT")
    def bad(n, msg): out.append(("FAIL", "GRD-020", f"{path}:{getattr(n, 'lineno', 0)}", msg))
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                top = a.name.split(".")[0]
                if top == "importlib" and asm: mods[a.asname or a.name.split(".")[0]] = "importlib"; continue
                if top not in IMPORTS: bad(n, f"imports {a.name}: element code imports the toolkit, math, numpy, csv, json, os and sys only")
                mods[a.asname or top] = top
        elif isinstance(n, ast.ImportFrom):
            top = (n.module or "").split(".")[0]
            if n.level: bad(n, "a relative import: element code imports from toolkit")
            elif top == "importlib" and asm: pass
            elif top not in IMPORTS or top in ("os", "sys"): bad(n, f"from {n.module} import ...: element code imports the toolkit, math, numpy, csv and json by name")
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
            f = n.func.id
            if f in CALLS: bad(n, f"calls {f}(): code that builds geometry never needs it")
            elif f == "open":
                mode = n.args[1] if len(n.args) > 1 else next((k.value for k in n.keywords if k.arg == "mode"), None)
                if mode is not None and not (isinstance(mode, ast.Constant) and mode.value in ("r", "rb")) and not (asm and (in_main(n) or to_out(n))):
                    bad(n, "opens a file to write: element code reads its own tables only (the build writes the outputs)")
        elif isinstance(n, ast.Attribute):
            if n.attr.startswith("__") and n.attr.endswith("__") and n.attr not in DUNDER_OK: bad(n, f"reaches {n.attr}: a way out of the toolkit")
            base = n.value.id if isinstance(n.value, ast.Name) else None
            m = mods.get(base)
            if m == "os" and n.attr not in OS_OK and not (asm and n.attr == "makedirs"): bad(n, f"os.{n.attr}: element code uses os.path only")
            if m == "sys" and n.attr not in SYS_OK and not (n.attr == "modules" and self_ref(n)): bad(n, f"sys.{n.attr}: element code uses sys.path, sys.argv, sys.exit and sys.modules[__name__] only")
            if m == "importlib" and n.attr not in ("util", "spec_from_file_location", "module_from_spec"): bad(n, f"importlib.{n.attr}: an assembly loads its sub-assemblies' files only")
        elif isinstance(n, ast.Name) and n.id.startswith("__") and n.id.endswith("__") and n.id not in DUNDER_OK and isinstance(n.ctx, ast.Load) and n.id not in ("__name__",):
            bad(n, f"uses {n.id}: a way out of the toolkit")
    return out


def check(base="HEAD", external=False, root=None):
    """GRD findings for every file changed against base (added or modified; a deletion brings nothing in)"""
    root = root or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    g = lambda *a: subprocess.run(["git", *a], cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
    paths = sorted({p for p in g("diff", "--name-only", "--diff-filter=AMRT", base).splitlines() + g("ls-files", "--others", "--exclude-standard").splitlines() if p.strip()})
    out = []
    for p in paths:
        full = os.path.join(root, p)
        if not os.path.lexists(full): continue
        if os.path.islink(full): out += file_findings(p, b"", external, is_link=True); continue
        data = open(full, "rb").read()
        out += file_findings(p, data, external)
        if p.endswith(".py") and p.startswith(("lib/elements/", "lib/assemblies/")):
            out += code_findings(p, data.decode("utf-8", "replace"))
    return paths, out
