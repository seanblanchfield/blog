#!/usr/bin/env python3
"""Generate consistent editorial covers for published posts without an image.

This intentionally uses only vector drawing plus Pillow. Covers contain no text,
remain legible as small cards, and are saved as optimized 1600×900 JPEGs.
"""
from __future__ import annotations

import argparse
import hashlib
import math
import re
from pathlib import Path

import yaml
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
POSTS = PROJECT / "content/posts"
IMAGES = PROJECT / "content/images/covers"

PALETTES = [
    ("#10253d", "#20a39e", "#f4e9cd"),
    ("#17213a", "#e07a5f", "#f4f1de"),
    ("#203349", "#f2b134", "#edf2f4"),
    ("#1f2937", "#63b3a6", "#f4d35e"),
    ("#243447", "#9c89b8", "#f0e6ef"),
    ("#263238", "#ef8354", "#e8eef2"),
]

# Exact concepts for the current uncovered archive. The keyword fallback below
# handles future posts while this map keeps ambiguous old titles accurate.
EXACT_SUBJECTS = {
    'Network Attached Storage Problems': 'storage',
    "I'm a complainer": 'form',
    'O2 Ireland Overcharging Me for Data Roaming': 'signal',
    'Collision-Free': 'paths',
    'Exciting New Company': 'idea',
    'Python Memoize with Expiry': 'clock',
    'Multiple asynchronous event handling with Flexunit': 'nodes',
    'Cherokee-admin tunnel script': 'tunnel',
    'Logging Unhandled Exceptions in Actionscript': 'target',
    'Enterprise and Optimism': 'rocket',
    'The secret history of Eurovision': 'microphone',
    'Games Development and R&D': 'controller',
    'The Dangers of Excessive Effectiveness': 'clock',
    'Fixing the Boxee Box Remote': 'remote',
    'The Lean Reality Check': 'compass',
    'Interview at Architalks#7': 'microphone',
    'The Talented 38: Ireland’s top technology and startup leaders': 'network',
    '4G to Empower Indigenous Digital Industry': 'signal',
    'Scale Front featured in the Irish Times': 'layers',
    'Speaking on the Dublin Startup Scene at Irish Times FUSION': 'microphone',
    'Ditching the Pitch': 'megaphone',
    'Awkward Bedfellows: Xero and AIB': 'bridge',
    'Trademark Phishing Scam': 'hook',
    'Looking to the UK - Entrepreneurial Incentives': 'stairs',
    'Employee Ownership Schemes in Ireland': 'pie',
    'Interview with Gary Fox - The Entrepreneur Experiment': 'microphone',
    'Interview with Mark Kelly - The AI Ireland': 'nodes',
}

# One visual symbol per subject family. Matching is deliberately explicit so a
# future missing-cover build remains predictable rather than generative.
SUBJECTS = [
    (("email", "archiv"), "envelope"),
    (("storage", "nas"), "storage"),
    (("complain", "overcharg", "tax", "budget"), "scales"),
    (("collision",), "paths"),
    (("company", "startup", "enterprise", "capital", "entrepreneur"), "rocket"),
    (("memoize", "expiry", "asynchronous", "event", "logging", "exception", "software"), "code"),
    (("flash",), "lightning"),
    (("tunnel",), "tunnel"),
    (("ubuntu", "natty", "laptop"), "laptop"),
    (("boxee", "remote"), "remote"),
    (("desktop",), "windows"),
    (("eurovision",), "microphone"),
    (("games", "development", "r&d"), "controller"),
    (("effectiveness",), "target"),
    (("lean", "reality"), "funnel"),
    (("interview", "speaking", "fusion", "irish times"), "microphone"),
    (("talented",), "network"),
    (("4g", "digital industry"), "signal"),
    (("scale front",), "layers"),
    (("pitch",), "megaphone"),
    (("xero", "aib", "bank"), "bridge"),
    (("trademark", "phishing", "scam"), "hook"),
    (("employee ownership",), "pie"),
    (("incentive",), "stairs"),
    (("ai ireland",), "nodes"),
]


def subject_for(title: str, body: str) -> str:
    if title in EXACT_SUBJECTS:
        return EXACT_SUBJECTS[title]
    title_text = title.lower()
    body_text = body[:1200].lower()
    # Titles carry far more signal than incidental words in an excerpt.
    for needles, subject in SUBJECTS:
        if any(n in title_text for n in needles):
            return subject
    for needles, subject in SUBJECTS:
        if any(n in body_text for n in needles):
            return subject
    return "idea"


def polygon(draw, points, fill):
    draw.polygon([(int(x), int(y)) for x, y in points], fill=fill)


def draw_symbol(draw: ImageDraw.ImageDraw, symbol: str, fg: str, accent: str, paper: str):
    # All symbols occupy the centre 750×500 zone and survive card-size cropping.
    lw = 34
    if symbol == "envelope":
        draw.rounded_rectangle((430, 260, 1170, 700), 32, fill=paper, outline=fg, width=lw)
        draw.line((450, 290, 800, 555, 1150, 290), fill=fg, width=lw, joint="curve")
        draw.line((450, 670, 700, 470), fill=accent, width=lw)
    elif symbol == "storage":
        for y in (245, 405, 565):
            draw.rounded_rectangle((470, y, 1130, y + 125), 28, fill=paper, outline=fg, width=24)
            draw.ellipse((1010, y + 38, 1055, y + 83), fill=accent)
    elif symbol == "scales":
        draw.line((800, 245, 800, 690), fill=fg, width=lw)
        draw.line((545, 350, 1055, 350), fill=fg, width=lw)
        draw.line((610, 350, 525, 575, 695, 575, 610, 350), fill=accent, width=18)
        draw.line((990, 350, 905, 575, 1075, 575, 990, 350), fill=paper, width=18)
        draw.line((650, 700, 950, 700), fill=fg, width=lw)
    elif symbol == "paths":
        draw.arc((370, 220, 850, 720), 270, 90, fill=paper, width=lw)
        draw.arc((750, 220, 1230, 720), 90, 270, fill=accent, width=lw)
        polygon(draw, [(760, 235), (855, 300), (750, 340)], accent)
        polygon(draw, [(840, 660), (745, 600), (850, 555)], paper)
    elif symbol == "rocket":
        polygon(draw, [(800, 185), (1010, 570), (800, 510), (590, 570)], paper)
        draw.ellipse((720, 315, 880, 475), fill=accent, outline=fg, width=20)
        polygon(draw, [(700, 525), (565, 690), (735, 625)], accent)
        polygon(draw, [(900, 525), (1035, 690), (865, 625)], accent)
        polygon(draw, [(745, 615), (800, 790), (855, 615)], "#f4d35e")
    elif symbol == "code":
        draw.rounded_rectangle((400, 235, 1200, 705), 36, fill=paper, outline=fg, width=26)
        draw.ellipse((445, 280, 480, 315), fill=accent)
        draw.ellipse((500, 280, 535, 315), fill=accent)
        draw.line((595, 420, 485, 505, 595, 590), fill=fg, width=lw, joint="curve")
        draw.line((1005, 420, 1115, 505, 1005, 590), fill=fg, width=lw, joint="curve")
        draw.line((735, 620, 865, 390), fill=accent, width=lw)
    elif symbol == "lightning":
        polygon(draw, [(850, 170), (570, 535), (760, 535), (690, 760), (1030, 390), (825, 390)], accent)
    elif symbol == "tunnel":
        draw.arc((430, 210, 1170, 910), 180, 360, fill=paper, width=65)
        draw.line((430, 555, 430, 750), fill=paper, width=65)
        draw.line((1170, 555, 1170, 750), fill=paper, width=65)
        for x in (675, 800, 925):
            draw.line((x, 590, x, 760), fill=accent, width=18)
    elif symbol == "laptop":
        draw.rounded_rectangle((490, 245, 1110, 650), 28, fill=paper, outline=fg, width=28)
        draw.rectangle((535, 295, 1065, 600), fill=accent)
        polygon(draw, [(420, 680), (1180, 680), (1100, 765), (500, 765)], paper)
        polygon(draw, [(850, 210), (940, 90), (915, 255)], "#f4d35e")
    elif symbol == "remote":
        draw.rounded_rectangle((650, 170, 950, 760), 80, fill=paper, outline=fg, width=28)
        draw.ellipse((735, 250, 865, 380), fill=accent)
        for x, y in ((735, 460), (825, 460), (735, 550), (825, 550)):
            draw.ellipse((x, y, x + 40, y + 40), fill=fg)
    elif symbol == "windows":
        for x, y in ((500, 260), (820, 260), (500, 520), (820, 520)):
            draw.rounded_rectangle((x, y, x + 280, y + 210), 22, fill=paper, outline=fg, width=18)
        draw.line((800, 210, 800, 760), fill=accent, width=24)
    elif symbol == "microphone":
        draw.rounded_rectangle((650, 170, 950, 555), 145, fill=paper, outline=fg, width=28)
        draw.arc((545, 320, 1055, 720), 0, 180, fill=accent, width=lw)
        draw.line((800, 690, 800, 785), fill=accent, width=lw)
        draw.line((660, 785, 940, 785), fill=accent, width=lw)
    elif symbol == "controller":
        polygon(draw, [(510, 360), (675, 285), (925, 285), (1090, 360), (1190, 655), (1040, 720), (875, 575), (725, 575), (560, 720), (410, 655)], paper)
        draw.line((580, 470, 730, 470), fill=fg, width=lw)
        draw.line((655, 395, 655, 545), fill=fg, width=lw)
        draw.ellipse((930, 390, 990, 450), fill=accent)
        draw.ellipse((1010, 475, 1070, 535), fill=accent)
    elif symbol == "target":
        for r, c in ((300, paper), (215, accent), (120, paper), (48, accent)):
            draw.ellipse((800-r, 485-r, 800+r, 485+r), fill=c)
        draw.line((960, 325, 1160, 125), fill=fg, width=26)
        polygon(draw, [(1160, 125), (1100, 138), (1147, 185)], fg)
    elif symbol == "funnel":
        polygon(draw, [(430, 240), (1170, 240), (920, 525), (855, 525), (855, 735), (745, 735), (745, 525), (680, 525)], paper)
        draw.line((520, 340, 1080, 340), fill=accent, width=28)
    elif symbol == "clock":
        draw.ellipse((520, 205, 1080, 765), fill=paper, outline=fg, width=28)
        draw.line((800, 485, 800, 300), fill=fg, width=lw)
        draw.line((800, 485, 955, 570), fill=accent, width=lw)
        draw.ellipse((765, 450, 835, 520), fill=accent)
    elif symbol == "compass":
        draw.ellipse((500, 185, 1100, 785), fill=paper, outline=fg, width=28)
        polygon(draw, [(800, 260), (900, 545), (800, 500), (700, 545)], accent)
        polygon(draw, [(800, 710), (700, 425), (800, 470), (900, 425)], fg)
        draw.ellipse((765, 450, 835, 520), fill=paper, outline=fg, width=16)
    elif symbol == "form":
        draw.rounded_rectangle((520, 180, 1080, 755), 25, fill=paper, outline=fg, width=24)
        for y in (300, 410, 520, 630):
            draw.rectangle((600, y, 655, y + 55), outline=accent, width=16)
            draw.line((710, y + 25, 980, y + 25), fill=fg, width=20)
        draw.line((590, 330, 655, 375, 735, 255), fill=accent, width=22)
    elif symbol == "network" or symbol == "nodes":
        pts=[(800,250),(545,410),(1055,410),(625,670),(975,670),(800,520)]
        for a,b in ((0,1),(0,2),(1,3),(1,5),(2,4),(2,5),(3,5),(4,5)):
            draw.line((*pts[a],*pts[b]), fill=paper, width=20)
        for i,(x,y) in enumerate(pts):
            r=58 if i==5 else 42
            draw.ellipse((x-r,y-r,x+r,y+r), fill=accent if i==5 else paper, outline=fg, width=12)
    elif symbol == "signal":
        draw.line((800, 640, 800, 760), fill=paper, width=lw)
        draw.ellipse((755, 575, 845, 665), fill=accent)
        for pad in (100, 210, 325):
            draw.arc((800-pad, 620-pad, 800+pad, 620+pad), 205, 335, fill=paper, width=30)
    elif symbol == "layers":
        for off, color in ((150,accent),(75,paper),(0,"#f4d35e")):
            polygon(draw, [(800,220+off),(1130,390+off),(800,560+off),(470,390+off)], color)
    elif symbol == "megaphone":
        polygon(draw, [(440,370),(820,270),(1080,165),(1080,640),(820,535),(440,440)], paper)
        draw.rectangle((760,505,880,735), fill=accent)
        for y in (280,405,530):
            draw.line((1145,y,1250,y), fill=accent, width=24)
    elif symbol == "bridge":
        draw.arc((440,220,1160,850), 180,360, fill=paper,width=45)
        draw.line((450,550,1150,550), fill=accent,width=32)
        for x in (560,680,800,920,1040):
            draw.line((x,405,x,550),fill=paper,width=16)
    elif symbol == "hook":
        draw.arc((560,280,1030,760), 320,180,fill=paper,width=56)
        draw.line((830,235,830,560),fill=paper,width=56)
        polygon(draw,[(830,185),(760,290),(900,290)],accent)
    elif symbol == "pie":
        draw.pieslice((500,185,1100,785),0,270,fill=paper,outline=fg,width=24)
        draw.pieslice((500,185,1100,785),270,360,fill=accent,outline=fg,width=24)
    elif symbol == "stairs":
        polygon(draw,[(430,700),(430,590),(610,590),(610,470),(790,470),(790,350),(970,350),(970,230),(1170,230),(1170,700)],paper)
        polygon(draw,[(1060,160),(1210,235),(1060,310)],accent)
    else:
        draw.ellipse((580,215,1020,655), fill=paper, outline=fg, width=28)
        polygon(draw, [(740,620),(860,620),(910,760),(690,760)], accent)
        for angle in range(0,360,45):
            x=800+math.cos(math.radians(angle))*330
            y=435+math.sin(math.radians(angle))*330
            draw.ellipse((x-22,y-22,x+22,y+22),fill=accent)


def create_cover(title: str, body: str, destination: Path):
    digest=int(hashlib.sha256(title.encode()).hexdigest()[:8],16)
    bg, accent, paper=PALETTES[digest % len(PALETTES)]
    img=Image.new('RGB',(1600,900),bg)
    draw=ImageDraw.Draw(img)
    # Sparse decorative geometry gives each cover variation without visual noise.
    draw.ellipse((-210,-320,700,590),fill=accent)
    draw.ellipse((1190,580,1800,1190),fill=paper)
    draw.rectangle((0,840,1600,900),fill=accent)
    draw_symbol(draw,subject_for(title,body),bg,accent,paper)
    destination.parent.mkdir(parents=True,exist_ok=True)
    img.save(destination,'JPEG',quality=84,optimize=True,progressive=True)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--apply',action='store_true',help='write covers and update post front matter')
    args=parser.parse_args()
    candidates=[]
    for post in sorted(POSTS.glob('*.md')):
        raw=post.read_text(encoding='utf-8')
        if not raw.startswith('---\n'):
            continue
        _,front,body=raw.split('---',2)
        data=yaml.safe_load(front) or {}
        if data.get('draft') or data.get('image'):
            continue
        title=str(data.get('title') or post.stem)
        image_name=post.stem[11:]+'.jpg'
        destination=IMAGES/image_name
        candidates.append((post,title,body,destination))
    print(f'{len(candidates)} published posts need covers')
    for post,title,body,destination in candidates:
        symbol=subject_for(title,body)
        print(f'{post.name}: {symbol} -> /images/covers/{destination.name}')
        if not args.apply:
            continue
        create_cover(title,body,destination)
        raw=post.read_text(encoding='utf-8')
        marker='layout: post\n'
        if marker not in raw:
            raise ValueError(f'No layout marker in {post}')
        raw=raw.replace(marker,marker+f'image: /images/covers/{destination.name}\n',1)
        post.write_text(raw,encoding='utf-8')


if __name__=='__main__':
    main()
