exec(open(__file__.replace("long_scenes.py","example_long_helpers_2026-11-23.py")).read())
L = "long"
NAVY = [(0, "#0B1033"), (1, "#22285E")]
SKYB = [(0, "#2D8CFF"), (1, "#A9DBFF")]
INDIGO = [(0, "#120B3A"), (.6, "#2A1B6B"), (1, "#4A2E8F")]
LAB = [(0, "#2B2340"), (1, "#4A3B66")]
SUNSET = [(0, "#3B2A80"), (.5, "#E0607A"), (1, "#FFB347")]
MARS = [(0, "#2B1B3A"), (.5, "#7A4A5A"), (1, "#D9A066")]
MARSDAY = [(0, "#C98A4E"), (1, "#E8B97A")]
def gnd(y, c1="#5CBF6A", c2="#3E9E50"):
    return (f'<path d="M0 {y} q480 -70 960 -10 q480 60 960 -20 V1080 H0 z" fill="{c1}" stroke="{INK}" stroke-width="8"/>'
            f'<path d="M0 {y+110} q520 -50 1100 10 q450 40 820 -10 V1080 H0 z" fill="{c2}" stroke="{INK}" stroke-width="8"/>')
def chap(n, en):
    return tag(330, 90, f"{n}. {en}", bg="#FFFFFF", size=46)
def wstars(n, seed=1, ymax=1080):
    r = random.Random(seed)
    return "".join(f'<circle cx="{r.randint(0,1920)}" cy="{r.randint(0,ymax)}" r="{r.choice([2,3,4])}" fill="#FFFFFF" opacity="{r.uniform(.5,1):.2f}"/>' for _ in range(n))
def wfan(x, y, x2, y0, y1, w=22):
    return fan(x, y, x2, y0, y1, w)
def tube(x, y, w, h, smoke=0):
    sm = "".join(f'<circle cx="{x+30+i*((w-60)/11):.0f}" cy="{y+h/2+((i*37)%40-20)}" r="{18+(i%3)*6}" fill="#C8C8D8" opacity=".35"/>' for i in range(12)) if smoke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="#DDF3FF" fill-opacity=".35" stroke="{INK}" stroke-width="9"/>' + sm
def drop(x, y, s=1):
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M0 -170 C 90 -40 140 20 140 80 A140 140 0 0 1 -140 80 C -140 20 -90 -40 0 -170 Z" fill="#9ED8FF" fill-opacity=".75" stroke="{INK}" stroke-width="10"/></g>'
def bigcloud(x, y, s=1, c="#FFFFFF"):
    return cloud(x, y, s, c)
MOLS = [(300,250),(560,420),(820,230),(1100,380),(1380,250),(1640,430),(420,640),(760,700),(1080,620),(1420,690),(1760,640)]

# 01 cover
put(L,"s01", '<circle cx="1300" cy="760" r="420" fill="url(#glow)" opacity=".55"/>' + sun(1300, 760, 190) +
    bigcloud(300, 820, 1.0) + qmark(1700, 820, .9) + kid(560, 760, .5, "surprised", look=(14,-12)) + gnd(990), SKYB)
put(L,"s02", sun(1550, 250, 120) + bigcloud(350, 260, .9) + kid(960, 520, .62, "happy", arms="up") + gnd(950), SKYB)
# ch1 light travel
put(L,"s03", wstars(120, 3) + sun(260, 540, 170) + earth(1640, 540, 150) + beam(480, 540, 1460, 540, "#FFF6C8", 24) +
    tag(960, 360, "150 million km") + tag(960, 760, "8 min 20 s", bg="#FF4FA3", fg="#FFFFFF") + chap(1, "Light"), [(0,"#03040F"),(1,"#151A3A")])
put(L,"s04", wstars(80, 5) + earth(960, 560, 220) + arrow_curve(960, 560, 330, 200, 520, "#FFD23F", 18) +
    tag(960, 140, "300 000 km/s") + tag(1600, 960, "x7 / second", bg="#FF4FA3", fg="#FFFFFF"), [(0,"#03040F"),(1,"#151A3A")])
put(L,"s05", sun(960, 470, 200) + '<circle cx="960" cy="470" r="420" fill="url(#glow)" opacity=".5"/>' + qmark(1500, 520, .8) +
    kid(400, 600, .5, "surprised", look=(16,-12)) + gnd(990), SKYB)
# ch2 Newton
put(L,"s06", '<rect x="0" y="0" width="1920" height="1080" fill="#2B2340"/><rect x="60" y="200" width="160" height="380" fill="#FFF6C8" stroke="#1B1B2F" stroke-width="8"/>' +
    beam(140, 390, 900, 520, "#FFFFFF", 26) + '<rect x="0" y="860" width="1920" height="220" fill="#6B4A2F" stroke="#1B1B2F" stroke-width="8"/>' +
    kid(1400, 520, .55, "happy", look=(-14, 0)) + tag(1400, 130, "~1666") + chap(2, "Newton"), LAB)
put(L,"s07", beam(0, 420, 720, 520, "#FFFFFF", 30) + prism(880, 560, 1.1) + wfan(960, 540, 1920, 300, 900, 30) +
    '<rect x="1840" y="200" width="80" height="780" fill="#EFE6D6" stroke="#1B1B2F" stroke-width="8"/>', LAB)
put(L,"s08", beam(0, 480, 480, 520, "#FFFFFF", 28) + prism(600, 560, .85) + wfan(660, 540, 1180, 420, 720, 18) +
    f'<g transform="rotate(180 1300 560)">{prism(1300, 560, .85)}</g>' + beam(1380, 560, 1920, 600, "#FFFFFF", 28) + tag(960, 150, "= WHITE", bg="#FFFFFF"), [(0,"#14223D"),(1,"#33507A")])
put(L,"s09", '<rect x="660" y="160" width="600" height="760" rx="20" fill="#F5ECD7" stroke="#1B1B2F" stroke-width="10"/>' +
    "".join(f'<rect x="720" y="{260+i*70}" width="{480-(i%3)*90}" height="22" rx="11" fill="#C9B994"/>' for i in range(8)) +
    wfan(760, 820, 1160, 760, 880, 10) + tag(960, 120, "Feb 1672") + kid(1550, 560, .45, "happy") + kid(380, 560, .45, "surprised", look=(14,-8)), [(0,"#3A2A1E"),(1,"#6B4A2F")])
put(L,"s10", prism(760, 560, 1.5) + beam(0, 380, 520, 480, "#FFFFFF", 32) + wfan(880, 520, 1920, 300, 1000, 28) +
    tag(400, 900, "Dispersion", bg="#FFFFFF") + tag(1500, 120, "200 000 km/s"), [(0,"#0F2A4F"),(1,"#1F5A8F")])
put(L,"s11", drop(760, 520, 1.6) + beam(0, 330, 640, 380, "#FFFFFF", 22) + wfan(760, 640, 1300, 760, 960, 14) +
    sun(150, 160, 80) + tag(1450, 300, "42°", size=90) + bigcloud(1600, 650, .8, "#DDE3EE"), [(0,"#5C7DA8"),(1,"#A9C4E6")])
# ch3 waves
put(L,"s12", wave(160, 540, 1600, 520, 160, "#5CBF6A", 22) +
    f'<line x1="550" y1="300" x2="1070" y2="300" stroke="{INK}" stroke-width="10"/><line x1="550" y1="270" x2="550" y2="330" stroke="{INK}" stroke-width="10"/><line x1="1070" y1="270" x2="1070" y2="330" stroke="{INK}" stroke-width="10"/>' +
    tag(810, 200, "wavelength λ") + chap(3, "Waves"), [(0,"#1B1B2F"),(1,"#2E2E55")])
put(L,"s13", wave(120, 330, 1680, 500, 110, "#E8483B", 20) + tag(960, 160, "700-750 nm", bg="#E8483B", fg="#FFFFFF") +
    wave(120, 720, 1680, 260, 110, "#4B4FC9", 20) + tag(960, 560, "~400 nm", bg="#4B4FC9", fg="#FFFFFF") + tag(1500, 960, "1 nm = 0.000000001 m", bg="#FFD23F", size=48), [(0,"#1B1B2F"),(1,"#2E2E55")])
put(L,"s14", wave(120, 360, 800, 500, 90, "#E8483B", 18) + wave(1000, 360, 800, 260, 90, "#4B4FC9", 18) +
    '<circle cx="960" cy="360" r="60" fill="#FFD23F" stroke="#1B1B2F" stroke-width="8"/><rect x="945" y="400" width="30" height="120" fill="#FFD23F" stroke="#1B1B2F" stroke-width="8"/>' +
    kid(960, 640, .45, "happy", look=(0,-14)), [(0,"#1B1B2F"),(1,"#2E2E55")])
# ch4 air
put(L,"s15", "".join(molecule(x, y, .55, "#8FD3FF" if k % 5 else "#FF8C8C") for k, (x, y) in enumerate(MOLS)) +
    tag(560, 940, "N2 78%", bg="#8FD3FF") + tag(1360, 940, "O2 21%", bg="#FF8C8C") + chap(4, "Air"), [(0,"#0B1A3A"),(1,"#23407A")])
put(L,"s16", molecule(520, 520, 1.3) + wave(820, 520, 1000, 560, 200, "#4FA3FF", 22) + tag(520, 220, "tiny") + tag(1320, 200, "light wave", bg="#4FA3FF", fg="#FFFFFF"), [(0,"#0B1A3A"),(1,"#23407A")])
# ch5 Rayleigh
put(L,"s17", '<circle cx="960" cy="520" r="420" fill="url(#bglow)" opacity=".7"/>' + BGLOW + beam(0, 520, 760, 520, "#FFFFFF", 26) +
    burst(960, 520, 200, 460, "#4FA3FF", 12, 14) + molecule(960, 520, 1.2) + beam(1160, 520, 1920, 520, "#E8483B", 20) + tag(1500, 120, "Scattering", bg="#FFFFFF") + chap(5, "Rayleigh"), INDIGO)
put(L,"s18", tube(260, 380, 1400, 240, smoke=1) + '<circle cx="230" cy="500" r="80" fill="#FFF6C8" stroke="#1B1B2F" stroke-width="8"/>' +
    '<rect x="320" y="440" width="1300" height="120" fill="#6FA8FF" opacity=".35"/>' + '<circle cx="1720" cy="500" r="60" fill="#FF6B3D" stroke="#1B1B2F" stroke-width="8"/>' +
    kid(960, 840, .35, "surprised", look=(0,-14)) + tag(960, 160, "Tyndall 1860s") + tag(1720, 330, "red", bg="#FF6B3D", fg="#FFFFFF") + tag(960, 300, "blue", bg="#4FA3FF", fg="#FFFFFF", size=50), LAB)
put(L,"s19", '<rect x="560" y="180" width="800" height="560" rx="24" fill="#1F3B2D" stroke="#1B1B2F" stroke-width="14"/>' +
    label(960, 500, "I ∝ 1/λ⁴", 150, "#FFFFFF") + tag(960, 120, "Rayleigh 1871"), [(0,"#3A2A1E"),(1,"#5A4430")])
put(L,"s20", wave(120, 330, 820, 400, 90, "#E8483B", 18) + tag(1300, 330, "x1", bg="#E8483B", fg="#FFFFFF") +
    wave(120, 700, 820, 200, 90, "#4FA3FF", 18) + tag(1300, 700, "x16", bg="#4FA3FF", fg="#FFFFFF") +
    tag(960, 130, "x12 blue vs red", bg="#FFD23F", size=50), [(0,"#1A1033"),(1,"#3A2466")])
put(L,"s21", sun(1650, 170, 100) + "".join(beam(1650, 170, x, y, "#4FA3FF", 9) for x, y in [(300,300),(560,520),(880,260),(1150,560),(1380,380)]) +
    "".join(molecule(x, y, .3) for x, y in [(300,300),(560,520),(880,260),(1150,560),(1380,380)]) +
    kid(700, 640, .45, "happy", look=(0,-16), arms="up") + gnd(980, "#3E9E50", "#2F7A3E"), [(0,"#1F6FE0"),(1,"#7FC0FF")])
# ch6 violet
put(L,"s22", wave(160, 360, 1600, 220, 100, "#9B4FD6", 20) + qmark(960, 700, .8, "#9B4FD6") + chap(6, "Violet?"), [(0,"#20124D"),(1,"#45277F")])
put(L,"s23", sun(380, 480, 150) + tag(380, 780, "1. less violet", bg="#FFD23F", size=48) +
    '<path d="M760 300 h400 v360 h-400 z" fill="#3A2466" stroke="#1B1B2F" stroke-width="8"/>' + wave(780, 480, 360, 120, 40, "#9B4FD6", 12) + tag(960, 780, "2. absorbed", bg="#FFFFFF", size=48) +
    eye(1560, 480, .9) + tag(1560, 780, "3. our eyes", bg="#4FA3FF", fg="#FFFFFF", size=48), [(0,"#20124D"),(1,"#45277F")])
# ch7 clouds
put(L,"s24", bigcloud(700, 480, 1.8) + "".join(f'<circle cx="{x}" cy="{y}" r="20" fill="#9ED8FF" stroke="#1B1B2F" stroke-width="5"/>' for x, y in [(560,470),(700,430),(820,480),(640,520)]) +
    wfan(200, 480, 520, 420, 540, 12) + burst(700, 470, 260, 420, "#FFFFFF", 10, 12) + chap(7, "Clouds"), SKYB)
put(L,"s25", bigcloud(960, 380, 2.2, "#8A90A0") + "".join(f'<line x1="{x}" y1="560" x2="{x-30}" y2="680" stroke="#6FA8FF" stroke-width="10" stroke-linecap="round"/>' for x in range(620, 1340, 70)) +
    kid(1600, 650, .45, "worried", look=(-14,-14)) + gnd(990, "#4E8F5A", "#3B7046"), [(0,"#5A6478"),(1,"#9AA3B5")])
# ch8 sunset
put(L,"s26", earth(960, 1500, 900) + '<path d="M-200 1500 A1160 1160 0 0 1 2120 1500" fill="none" stroke="#8FD3FF" stroke-width="150" opacity=".45"/>' +
    beam(960, 60, 960, 560, "#FFF6C8", 22) + tag(1250, 200, "noon: x1", bg="#FFFFFF") + chap(8, "Sunset"), NAVY)
put(L,"s27", earth(960, 1500, 900) + '<path d="M-200 1500 A1160 1160 0 0 1 2120 1500" fill="none" stroke="#8FD3FF" stroke-width="150" opacity=".45"/>' +
    beam(0, 520, 1920, 640, "#FF8A2B", 22) + tag(960, 300, "horizon: x38", bg="#FF8A2B"), NAVY)
put(L,"s28", OGLOW + '<circle cx="960" cy="760" r="560" fill="url(#oglow)" opacity=".9"/>' + sun(960, 760, 170).replace("#FFE14D", "#FF8A2B") +
    city(1000, 5) + tag(960, 170, "red + orange + yellow", bg="#FF8A2B"), SUNSET)
# ch9 Moon
put(L,"s29", wstars(150, 11) + earth(1550, 260, 130) + sun(330, 230, 80) +
    '<path d="M0 760 q480 -60 960 -10 q480 50 960 -20 V1080 H0 z" fill="#BDBDC8" stroke="#1B1B2F" stroke-width="8"/>' + chap(9, "Moon"), [(0,"#000000"),(1,"#0A0A14")])
put(L,"s30", wstars(150, 12) + sun(960, 300, 110) +
    '<path d="M0 760 q480 -60 960 -10 q480 50 960 -20 V1080 H0 z" fill="#BDBDC8" stroke="#1B1B2F" stroke-width="8"/><ellipse cx="500" cy="900" rx="160" ry="45" fill="#9A9AA8" stroke="#1B1B2F" stroke-width="6"/><ellipse cx="1450" cy="960" rx="110" ry="30" fill="#9A9AA8" stroke="#1B1B2F" stroke-width="6"/>' +
    tag(960, 620, "no air = black sky", bg="#FFFFFF"), [(0,"#000000"),(1,"#0A0A14")])
# ch10 Mars
put(L,"s31", '<circle cx="960" cy="520" r="330" fill="#C1532E" stroke="#1B1B2F" stroke-width="10"/><circle cx="860" cy="430" r="60" fill="#9A3E22"/><circle cx="1080" cy="620" r="80" fill="#9A3E22"/>' +
    tag(420, 380, "100x thinner") + tag(1500, 380, "CO2 95%", bg="#FFFFFF") + wstars(80, 21) + chap(10, "Mars"), [(0,"#03040F"),(1,"#151A3A")])
put(L,"s32", gnd(700, "#C1532E", "#9A3E22") + rocks(820, 7) + sun(1500, 230, 90).replace("#FFE14D", "#FFF3C4") +
    "".join(f'<circle cx="{x}" cy="{y}" r="10" fill="#D98A5A" opacity=".8"/>' for x, y in [(200,200),(420,330),(700,180),(980,300),(1200,150),(1700,420),(560,480)]) +
    kid(600, 520, .45, "surprised", look=(14,-12)), MARSDAY)
put(L,"s33", BGLOW + bluesun(1250, 640, 80) + gnd(700, "#A8472A", "#7E321D") + rocks(820, 3) + rover(600, 780, .9) +
    tag(600, 160, "15/04/2015", bg="#FFFFFF") + tag(1250, 160, "Gale crater") , MARS)
put(L,"s34", BGLOW + bluesun(960, 560, 110) + "".join(f'<circle cx="{x}" cy="{y}" r="16" fill="#D98A5A" stroke="#1B1B2F" stroke-width="4"/>' for x, y in
    [(420,300),(620,460),(1300,330),(1480,520),(760,200),(1150,180)]) + gnd(760, "#C1532E", "#9A3E22") + tag(960, 130, "fine dust", bg="#FFD23F"), MARS)
put(L,"s35", '<rect x="0" y="0" width="960" height="1080" fill="#4FA3FF"/>' + sun(480, 300, 100) + OGLOW +
    '<rect x="960" y="0" width="960" height="1080" fill="#D9A066"/>' + BGLOW + bluesun(1440, 640, 80) +
    gnd(760, "#5CBF6A", "#3E9E50").replace('V1080 H0 z"', 'V1080 H0 z" clip-path="url(#lh)"') +
    '<path d="M960 760 q480 -60 960 -20 V1080 H960 z" fill="#C1532E" stroke="#1B1B2F" stroke-width="8"/>' +
    '<path d="M0 760 q480 -60 960 -10 V1080 H0 z" fill="#5CBF6A" stroke="#1B1B2F" stroke-width="8"/>' +
    tag(480, 900, "Earth", bg="#FFFFFF") + tag(1440, 900, "Mars", bg="#FFFFFF") + f'<line x1="960" y1="0" x2="960" y2="1080" stroke="{INK}" stroke-width="12"/>', SKYB)
# outro
put(L,"s36", beam(0, 300, 420, 380, "#FFFFFF", 22) + prism(560, 430, .7) + wfan(620, 410, 900, 330, 520, 12) +
    molecule(1150, 430, .6) + burst(1150, 430, 110, 230, "#4FA3FF", 8, 10) + sun(1650, 430, 90).replace("#FFE14D", "#FF8A2B") + kid(960, 740, .35, "happy"), [(0,"#1F6FE0"),(1,"#7FC0FF")])
put(L,"s37", sun(1600, 220, 110) + bigcloud(380, 250, .9) + kid(960, 560, .58, "happy", arms="up") + gnd(950) + qmark(1550, 650, .6), SKYB)
print("ok")
def glass(x, y, s=1, tint="#CFE6FF"):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-130 -200 L130 -200 L105 200 L-105 200 Z" fill="{tint}" fill-opacity=".8" stroke="{INK}" stroke-width="10" stroke-linejoin="round"/>'
            f'<path d="M-122 -120 L122 -120" stroke="#FFFFFF" stroke-width="8" opacity=".7"/></g>')
def torch(x, y):
    return f'<rect x="{x-170}" y="{y-45}" width="170" height="90" rx="20" fill="#4A4A55" stroke="{INK}" stroke-width="8"/><path d="M{x} {y-45} L{x+50} {y-75} L{x+50} {y+75} L{x} {y+45} Z" fill="#9A9AA8" stroke="{INK}" stroke-width="8"/>'
put(L,"s21a", glass(960, 520, 1.1, "#EAF2FF") + torch(560, 520) + '<rect x="1060" y="180" width="60" height="40" rx="8" fill="#FFFFFF" stroke="#1B1B2F" stroke-width="6"/>' +
    tag(960, 120, "water + milk", bg="#FFFFFF") + kid(1500, 640, .42, "happy", look=(-14,0)) + chap(5, "Try it"), [(0,"#14142A"),(1,"#2A2A48")])
put(L,"s21b", glass(860, 520, 1.1, "#A9CFFF") + torch(460, 520) + beam(1000, 520, 1500, 520, "#FF9A3D", 40) +
    '<rect x="1500" y="260" width="40" height="520" fill="#FFFFFF" stroke="#1B1B2F" stroke-width="8"/><circle cx="1490" cy="520" r="60" fill="#FF9A3D" opacity=".8"/>' +
    tag(860, 120, "side: blue", bg="#4FA3FF", fg="#FFFFFF") + tag(1350, 860, "end: orange", bg="#FF9A3D"), [(0,"#14142A"),(1,"#2A2A48")])
put(L,"s25a", qmark(960, 470, 1.2, "#FFD23F") + bigcloud(380, 300, .8) + bigcloud(1560, 320, .8) + tag(960, 110, "Quiz", bg="#FF4FA3", fg="#FFFFFF"), [(0,"#5C7DA8"),(1,"#A9C4E6")])
put(L,"s25b", '<rect x="0" y="0" width="1920" height="1080" fill="#E8EEF5"/>' + sun(1500, 260, 100) + bigcloud(500, 330, 1.0, "#FFFFFF") +
    kid(900, 620, .45, "surprised", look=(14,-12)) + gnd(990) + tag(960, 120, "white sky", bg="#FFFFFF"), [(0,"#E8EEF5"),(1,"#F5F7FA")])
