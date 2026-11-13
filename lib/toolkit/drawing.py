"""Print-style dimension drawings (SVG): the same line weights, arrows and paper as the ladder prints. Coordinates in px; callers scale mm."""
STYLE = (".o{fill:none;stroke:#1a1a1a;stroke-width:1.1}.o2{fill:none;stroke:#1a1a1a;stroke-width:0.7}.h{fill:none;stroke:#1a1a1a;stroke-width:0.6;stroke-dasharray:4 3}"
         ".d{fill:none;stroke:#1a1a1a;stroke-width:0.5}.a{fill:#1a1a1a}.t{font-size:9px;fill:#1a1a1a;text-anchor:middle}.k{font-size:8px;fill:#555}")
def R(x, y, w, h, cls="o"): return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" class="{cls}"/>'
def C(x, y, r, cls="o2"): return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" class="{cls}"/>'
def Ln(x1, y1, x2, y2, cls="d"): return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}"/>'
def T(x, y, txt, cls="t", extra=""): return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" {extra}>{txt}</text>'
def dim_h(x1, x2, y, txt, ext=None):
    e = "" if ext is None else Ln(x1, ext, x1, y + 6) + Ln(x2, ext, x2, y + 6)
    return (e + Ln(x1, y, x2, y) + T((x1 + x2) / 2, y - 4, txt) + f'<polygon points="{x1:.1f},{y:.1f} {x1 + 7:.1f},{y - 2.5:.1f} {x1 + 7:.1f},{y + 2.5:.1f}" class="a"/>'
            + f'<polygon points="{x2:.1f},{y:.1f} {x2 - 7:.1f},{y - 2.5:.1f} {x2 - 7:.1f},{y + 2.5:.1f}" class="a"/>')
def dim_v(y1, y2, x, txt, ext=None):
    e = "" if ext is None else Ln(ext, y1, x - 6, y1) + Ln(ext, y2, x - 6, y2)
    return (e + Ln(x, y1, x, y2) + f'<text x="{x + 4:.1f}" y="{(y1 + y2) / 2:.1f}" class="t" transform="rotate(-90 {x + 4:.1f} {(y1 + y2) / 2:.1f})" dy="-2">{txt}</text>'
            + f'<polygon points="{x:.1f},{y1:.1f} {x - 2.5:.1f},{y1 + 7:.1f} {x + 2.5:.1f},{y1 + 7:.1f}" class="a"/>' + f'<polygon points="{x:.1f},{y2:.1f} {x - 2.5:.1f},{y2 - 7:.1f} {x + 2.5:.1f},{y2 - 7:.1f}" class="a"/>')
def page(path, w, h, title, lines, body):
    """write the sheet: title (bold), subtitle lines, then the drawing elements"""
    head = T(60, 22, title, "k", 'style="text-anchor:start;font-size:9px;font-weight:700"') + "".join(T(60, 34 + 10 * i, ln, "k", 'style="text-anchor:start;font-size:7px"') for i, ln in enumerate(lines))
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" font-family="Arial, Helvetica, sans-serif"><style>{STYLE}</style>'
           f'<rect width="100%" height="100%" fill="#f4f3ef"/>{head}{"".join(body)}</svg>')
    open(path, "w", encoding="utf-8").write(svg)
