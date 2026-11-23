#!/usr/bin/env python3
"""long.py - landscape 16:9 long-form version of reel.py (same project.json format).
  python3 long.py project.json [--preview] [--cover] [--only sNN]
Differences: 1920x1080, smaller word captions (size 100), 0.5 s gap between scenes,
and it writes build/chapters.txt (YouTube timestamps) from scenes that have a "chapter" key."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reel
reel.W, reel.H = 1920, 1080
reel.GAP = 0.7
reel.word_img.__defaults__ = (100,)

_orig_render = reel.render_scene
def _render_resume(job):
    """Skip scenes already rendered (lets a long render resume after an interruption).
    Delete build/scene_*.mp4 to force a re-render after changing a scene."""
    out = f"{job[3]['build']}/scene_{job[0]['id']}.mp4"
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        return out
    return _orig_render(job)
reel.render_scene = _render_resume

_orig_main = reel.main
def chapters():
    pj = os.path.abspath(sys.argv[1]); d = os.path.dirname(pj)
    P = json.load(open(pj)); t = 0.0; out = []
    import hashlib
    voice, rate, pitch = P.get("voice"), P.get("rate", "+8%"), P.get("pitch", "+0Hz")
    for i, sc in enumerate(P["scenes"]):
        h = hashlib.md5(f"{sc['text']}|{voice}|{rate}|{pitch}".encode()).hexdigest()[:10]
        mp3 = f"{d}/build/tts/{sc['id']}_{h}.mp3"
        if sc.get("chapter"):
            out.append(f"{int(t//60)}:{int(t%60):02d} {sc['chapter']}")
        hold = sc.get("hold", 1.6 if i == len(P["scenes"]) - 1 and P.get("end_text") else reel.GAP)
        t += round((reel.duration(mp3) + hold) * reel.FPS) / reel.FPS
    open(f"{d}/build/chapters.txt", "w").write("\n".join(out) + "\n")
    print("".join(l + "\n" for l in out) + f"total {t/60:.1f} min")

if __name__ == "__main__":
    _orig_main()
    chapters()
