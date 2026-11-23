import os, sys; sys.path.insert(0, os.path.expanduser("~/reel"))
from cartoon import *
from cartoon_wide import svg_wide
B = os.path.dirname(os.path.abspath(__file__))
def put(part, name, body, bg):
    os.makedirs(f"{B}/{part}/scenes", exist_ok=True)
    open(f"{B}/{part}/scenes/{name}.svg", "w").write(svg_wide(body, bg))

RAINBOW = ["#E8483B", "#FF8A2B", "#FFD23F", "#5CBF6A", "#3A8DDE", "#4B4FC9", "#9B4FD6"]

def qmark(x, y, s=1, c="#FF4FA3"):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-70 -120 q0 -90 90 -90 q90 0 90 85 q0 60 -70 85 q-25 10 -25 50 v20" fill="none" stroke="{INK}" stroke-width="70" stroke-linecap="round"/>'
            f'<path d="M-70 -120 q0 -90 90 -90 q90 0 90 85 q0 60 -70 85 q-25 10 -25 50 v20" fill="none" stroke="{c}" stroke-width="46" stroke-linecap="round"/>'
            f'<circle cx="-5" cy="130" r="40" fill="{c}" stroke="{INK}" stroke-width="10"/></g>')

def cloud(x, y, s=1, c="#FFFFFF"):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-150 40 q-60 0 -60 -50 q0 -55 65 -55 q15 -70 95 -70 q70 0 95 60 q75 -10 90 55 q10 60 -55 60 z" fill="{c}" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/></g>')

def prism(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 -230 L200 120 L-200 120 Z" fill="#CFEFFF" fill-opacity=".85" stroke="{INK}" stroke-width="10" stroke-linejoin="round"/>'
            f'<path d="M0 -170 L40 -90" stroke="#FFFFFF" stroke-width="18" stroke-linecap="round" opacity=".8"/></g>')

def beam(x1, y1, x2, y2, c="#FFFFFF", w=34):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="{w+14}" stroke-linecap="round"/>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>')

def fan(x, y, x2, y0, y1, w=26):
    out = ""; n = len(RAINBOW)
    for i, c in enumerate(RAINBOW):
        yy = y0 + (y1 - y0) * i / (n - 1)
        out += f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{yy:.0f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'
    return out

def wave(x0, y, length, wl, amp, c, w=16):
    pts = []
    for i in range(0, int(length) + 1, 6):
        pts.append(f"{x0+i:.0f},{y + amp*math.sin(2*math.pi*i/wl):.1f}")
    d = "M" + " L".join(pts)
    return (f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w+10}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')

def molecule(x, y, s=1, c="#8FD3FF", c2=None):
    c2 = c2 or c
    return (f'<g transform="translate({x} {y}) scale({s})"><circle cx="-55" cy="0" r="75" fill="{c}" stroke="{INK}" stroke-width="9"/>'
            f'<circle cx="55" cy="0" r="75" fill="{c2}" stroke="{INK}" stroke-width="9"/>'
            f'<circle cx="-75" cy="-25" r="18" fill="#FFFFFF" opacity=".7"/><circle cx="35" cy="-25" r="18" fill="#FFFFFF" opacity=".7"/></g>')

def burst(x, y, r0, r1, c="#4FA3FF", n=10, w=16):
    out = ""
    for k in range(n):
        a = 2*math.pi*k/n + 0.2
        out += beam(x + r0*math.cos(a), y + r0*math.sin(a), x + r1*math.cos(a), y + r1*math.sin(a), c, w)
    return out

def eye(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-200 0 q200 -170 400 0 q-200 170 -400 0 z" fill="#FFFFFF" stroke="{INK}" stroke-width="10"/>'
            f'<circle r="85" fill="#3A8DDE" stroke="{INK}" stroke-width="8"/><circle r="38" fill="{INK}"/><circle cx="-25" cy="-25" r="16" fill="#FFFFFF"/></g>')

def ground(y, c1, c2):
    return (f'<path d="M0 {y} q270 -60 540 -10 q270 50 540 -20 V1920 H0 z" fill="{c1}" stroke="{INK}" stroke-width="8"/>'
            f'<path d="M0 {y+180} q300 -50 620 10 q250 40 460 -10 V1920 H0 z" fill="{c2}" stroke="{INK}" stroke-width="8"/>')

def rocks(y, seed=4, c="#8E3B22"):
    r = random.Random(seed); out = ""
    for _ in range(9):
        x = r.randint(30, 1050); yy = y + r.randint(0, 300); w = r.randint(40, 110)
        out += f'<ellipse cx="{x}" cy="{yy}" rx="{w}" ry="{w*.45:.0f}" fill="{c}" stroke="{INK}" stroke-width="6"/>'
    return out

def rover(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-150" y="-80" width="300" height="90" rx="18" fill="#E9E4D8" stroke="{INK}" stroke-width="8"/>'
            f'<rect x="-10" y="-230" width="22" height="150" fill="#B9B3A6" stroke="{INK}" stroke-width="6"/>'
            f'<rect x="-50" y="-280" width="100" height="60" rx="12" fill="#E9E4D8" stroke="{INK}" stroke-width="7"/>'
            f'<circle cx="-20" cy="-250" r="14" fill="#3A8DDE" stroke="{INK}" stroke-width="5"/><circle cx="22" cy="-250" r="14" fill="#3A8DDE" stroke="{INK}" stroke-width="5"/>'
            + "".join(f'<circle cx="{wx}" cy="40" r="40" fill="#4A4A55" stroke="{INK}" stroke-width="8"/><circle cx="{wx}" cy="40" r="12" fill="#B9B3A6"/>' for wx in (-110, 0, 110))
            + '</g>')

def bluesun(x, y, r=110):
    return (f'<circle cx="{x}" cy="{y}" r="{r*4}" fill="url(#bglow)"/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="#CFE8FF" stroke="{INK}" stroke-width="8"/>')

BGLOW = '<defs><radialGradient id="bglow"><stop offset="0" stop-color="#6FB8FF" stop-opacity="1"/><stop offset=".5" stop-color="#3F7FE0" stop-opacity=".6"/><stop offset="1" stop-color="#4F8FE0" stop-opacity="0"/></radialGradient></defs>'
OGLOW = '<defs><radialGradient id="oglow"><stop offset="0" stop-color="#FFB347" stop-opacity=".95"/><stop offset="1" stop-color="#FF6B3D" stop-opacity="0"/></radialGradient></defs>'

