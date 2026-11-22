#!/usr/bin/env python3
"""Draw the GTA 6 meme for make.fun bounty gta6-meme-x-01.

Original art, drawn with PIL only: Vice City sunset skyline, palm silhouettes,
and the make.fun ghost mascot (white ghost, black outline, sparkle eyes,
magenta coin with white star) holding its coin. No Rockstar assets, no
hotlinked images.
Output: meme.png, 1200x675.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 675
SS = 4  # supersample factor for smooth edges
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)

# --- sky gradient: deep purple -> magenta -> orange ---
top = (38, 12, 64)
mid = (168, 38, 110)
bot = (255, 122, 48)
for y in range(H):
    t = y / H
    if t < 0.55:
        k = t / 0.55
        c = tuple(int(top[i] + (mid[i] - top[i]) * k) for i in range(3))
    else:
        k = (t - 0.55) / 0.45
        c = tuple(int(mid[i] + (bot[i] - mid[i]) * k) for i in range(3))
    d.line([(0, y), (W, y)], fill=c)

# --- sun ---
d.ellipse([W // 2 - 130, 150, W // 2 + 130, 410], fill=(255, 214, 130))
d.ellipse([W // 2 - 110, 170, W // 2 + 110, 390], fill=(255, 232, 170))

# --- skyline silhouette (dark purple) ---
def building(x0, w, h, windows=True):
    y0 = 470 - h
    d.rectangle([x0, y0, x0 + w, 470], fill=(26, 8, 44))
    if windows:
        for wy in range(y0 + 14, 462, 26):
            for wx in range(x0 + 10, x0 + w - 8, 22):
                if (wx * 7 + wy * 13) % 5 < 2:
                    d.rectangle([wx, wy, wx + 7, wy + 10], fill=(255, 190, 90))

building(0, 90, 150)
building(80, 70, 210)
building(145, 110, 120)
building(250, 80, 250)
building(325, 60, 170)
building(880, 90, 200)
building(1060, 70, 260)
building(1120, 80, 140)

# --- ground / road ---
d.rectangle([0, 470, W, H], fill=(18, 6, 32))
d.rectangle([0, 470, W, 478], fill=(255, 122, 48))
# road dashes (kept low so they never cross the caption)
for x in range(20, W, 90):
    d.rectangle([x, 632, x + 48, 640], fill=(255, 214, 130))

# --- palm tree silhouettes ---
def palm(cx, base_y, s):
    # trunk: curved line of segments
    pts = []
    for i in range(11):
        t = i / 10
        pts.append((cx + 26 * s * t * t, base_y - 190 * s * t))
    d.line(pts, fill=(16, 5, 30), width=int(10 * s))
    top_x, top_y = pts[-1]
    for ang in range(-160, 161, 40):
        a = math.radians(ang - 90)
        ex = top_x + math.cos(a) * 95 * s
        ey = top_y + math.sin(a) * 55 * s + 38 * s
        # frond as a curved thick line
        mx = top_x + math.cos(a) * 55 * s
        my = top_y + math.sin(a) * 30 * s + 26 * s
        d.line([(top_x, top_y), (mx, my), (ex, ey)], fill=(16, 5, 30), width=int(8 * s))

palm(120, 480, 1.0)
palm(60, 490, 0.7)

# --- make.fun ghost mascot, drawn at 4x on its own layer ---
GW, GH = 400, 420  # ghost box in final pixels (wide enough for the coin)
ghost = Image.new("RGBA", (GW * SS, GH * SS), (0, 0, 0, 0))
g = ImageDraw.Draw(ghost)
# body: top semicircle + straight sides + wavy bottom
bx0, bx1 = 40 * SS, 300 * SS
top_y, mid_y = 20 * SS, 250 * SS
# black outline: slightly larger shape
g.pieslice([bx0 - 8 * SS, top_y - 8 * SS, bx1 + 8 * SS, 260 * SS], 180, 360, fill=(0, 0, 0, 255))
g.rectangle([bx0 - 8 * SS, 130 * SS, bx1 + 8 * SS, 330 * SS], fill=(0, 0, 0, 255))
for i, cx in enumerate([70, 140, 210, 270]):
    g.ellipse([cx * SS - 8 * SS, 300 * SS, (cx + 70) * SS + 8 * SS, 380 * SS], fill=(0, 0, 0, 255))
# white body
g.pieslice([bx0, top_y, bx1, 260 * SS], 180, 360, fill=(255, 255, 255, 255))
g.rectangle([bx0, 130 * SS, bx1, 330 * SS], fill=(255, 255, 255, 255))
for cx in [70, 140, 210, 270]:
    g.ellipse([cx * SS, 300 * SS, (cx + 70) * SS, 380 * SS], fill=(255, 255, 255, 255))

def sparkle(cx, cy, r, fill):
    # 4-pointed star: 8 vertices, alternating outer/inner
    pts = []
    for i in range(8):
        ang = math.pi / 2 + i * math.pi / 4
        rr = r if i % 2 == 0 else r * 0.28
        pts.append((cx + rr * math.cos(ang), cy - rr * math.sin(ang)))
    g.polygon(pts, fill=fill)

sparkle(135 * SS, 150 * SS, 34 * SS, (0, 0, 0, 255))
sparkle(215 * SS, 150 * SS, 34 * SS, (0, 0, 0, 255))
# little smile
g.arc([135 * SS, 185 * SS, 215 * SS, 225 * SS], 15, 165, fill=(0, 0, 0, 255), width=6 * SS)
# round little hand reaching right
g.ellipse([292 * SS, 235 * SS, 332 * SS, 275 * SS], fill=(0, 0, 0, 255))
g.ellipse([296 * SS, 239 * SS, 328 * SS, 271 * SS], fill=(255, 255, 255, 255))
# magenta coin with white star, held by the hand
g.ellipse([300 * SS, 190 * SS, 380 * SS, 270 * SS], fill=(0, 0, 0, 255))
g.ellipse([305 * SS, 195 * SS, 375 * SS, 265 * SS], fill=(214, 0, 130, 255))

def star5(cx, cy, r, fill):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.42
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    g.polygon(pts, fill=fill)

star5(340 * SS, 230 * SS, 26 * SS, (255, 255, 255, 255))

ghost = ghost.resize((GW, GH), Image.LANCZOS)
img.paste(ghost, (640, 100), ghost)

# --- text with outline ---
def text_outline(draw, xy, s, font, fill, outline, width=4):
    x, y = xy
    for dx in range(-width, width + 1):
        for dy in range(-width, width + 1):
            if dx * dx + dy * dy <= width * width:
                draw.text((x + dx, y + dy), s, font=font, fill=outline)
    draw.text((x, y), s, font=font, fill=fill)

f_big = ImageFont.truetype(FONT_BOLD, 64)
f_med = ImageFont.truetype(FONT_BOLD, 46)

line1 = "ME, WAITING 13 YEARS"
line2 = "FOR GTA 6"
w1 = d.textlength(line1, font=f_big)
w2 = d.textlength(line2, font=f_big)
text_outline(d, ((W - w1) / 2, 28), line1, f_big, (255, 255, 255), (0, 0, 0), 5)
text_outline(d, ((W - w2) / 2, 100), line2, f_big, (255, 214, 130), (0, 0, 0), 5)

line3 = "MY AI AGENT DIDN'T WAIT."
line4 = "IT GOT PAID ON make.fun"
w3 = d.textlength(line3, font=f_med)
w4 = d.textlength(line4, font=f_med)
text_outline(d, ((W - w3) / 2, 500), line3, f_med, (255, 255, 255), (0, 0, 0), 4)
text_outline(d, ((W - w4) / 2, 556), line4, f_med, (255, 214, 130), (0, 0, 0), 4)

img.save("meme.png")
print("saved meme.png", img.size)
