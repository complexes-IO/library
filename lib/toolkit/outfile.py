"""Generated outputs are written only when their content changes (round 10 h, the DOWNTIME review): a rebuild that changes nothing
touches nothing, so `git status` and the file times show only what really changed, on the PC and in a Linux clone alike."""
import io, os


def write(path, data, newline=None, encoding="utf-8"):
    """write data (bytes, or str) to path unless the file already holds exactly those bytes; True when it wrote. A str is written as
    open(path, "w") would write it: newline=None turns "\\n" into os.linesep, newline="\\n" keeps it."""
    if isinstance(data, str):
        if newline is None and os.linesep != "\n": data = data.replace("\n", os.linesep)
        elif newline not in (None, "", "\n"): data = data.replace("\n", newline)
        data = data.encode(encoding)
    try:
        with open(path, "rb") as f:
            if f.read() == data: return False
    except OSError: pass
    with open(path, "wb") as f: f.write(data)
    return True


def savefig(fig, path, **kw):
    """matplotlib's savefig, written only when the image's bytes change"""
    b = io.BytesIO(); fig.savefig(b, format="png", **kw); return write(path, b.getvalue())
