"""cartoon_wide.py - landscape 1920x1080 canvas for long-form Foudoul Science videos.
Use with the faceless-cartoon-reel skill's cartoon.py (props) and tools/long.py (renderer):
    from cartoon import *
    from cartoon_wide import svg_wide
"""
def svg_wide(body, bg):
    stops = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in bg)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">{stops}</linearGradient>
<radialGradient id="glow"><stop offset="0" stop-color="#FFF6C8" stop-opacity=".9"/><stop offset="1" stop-color="#FFF6C8" stop-opacity="0"/></radialGradient></defs>
<rect width="1920" height="1080" fill="url(#bg)"/>
{body}
</svg>'''
