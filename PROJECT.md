# Saan Kaa Laa 山卡旯 - Project Documentation

## Overview
**Saan Kaa Laa 山卡旯** is a self-organized team trail challenge event in Calgary, Alberta, inspired by Trailwalker Hong Kong. The goal is to bring the team challenge experience to Hong Kong people living in Calgary.

- **Website:** Single-page event site (`index.html`)
- **Target audience:** Primarily Hong Kong people in Calgary (bilingual EN/Traditional Chinese HK style)
- **Event philosophy:** "一個人走得快，一班人走得遠" (If you want to go far, go together)

## Event Details

### 2026 Edition
- **Date:** August 29, 2026
- **Registration deadline:** July 29, 2026 (one month before)
- **Entry fee:** $80 CAD per team (voluntary, to support the challenge)
- **Team size:** 4 people (must start and finish together)
- **Contact:** brknveggie@gmail.com
- **Primary communication:** Telegram channel (https://t.me/yycOutdoorHK)

### Challenge Categories
| Category | Distance | Elevation | Time Limit | Status |
|----------|----------|-----------|------------|--------|
| **SKL50** | ~54K | ~1,950m | 14 hours | Active |
| **SKL100** | ~100K | TBD | 30 hours | Coming Soon |

### Route (SKL50)
- Uses existing GPX: `assets/YYCHKWalker.gpx`
- **Sections & Difficulty:**
  1. Start → Aid Station 1 (15km, 500m↑) — **Moderate**
  2. Aid Station 1 → 2 (14km, 680m↑) — **Difficult**
  3. Aid Station 2 → 3 (10.5km, 600m↑) — **Easy**
  4. Aid Station 3 → Finish (14.5km, 170m↑, 750m↓) — **Easy**
- **Aid Stations:**
  1. Powderface Ridge Trailhead
  2. Elbow Fall Parking Lot — suggested cutoff 2:00 PM
  3. Moose Mountain Trailhead Parking
- **Finish:** Allen Bill Day Use Area

### Route (SKL100)
- Different start point, same finish as SKL50
- Details TBD — currently shows "Coming Soon" overlay on website

## Branding
- **English name:** Saan Kaa Laa (with spaces)
- **Chinese name:** 山卡旯
- **Meaning:** Cantonese slang for "middle of nowhere" — fitting for Calgary's backcountry trails
- **Hashtag:** #SaanKaaLaa (no spaces)
- **Philosophy:** This is a **challenge**, not a race — approachable for newcomers

## Inspiration
Inspired by **Trailwalker Hong Kong** — not a copy, but bringing the team challenge spirit to let HK people in Calgary experience long-distance team challenges. Emphasizes teamwork over competition.

## Technical Stack
- **Frontend:** Single HTML file with Tailwind CSS (CDN)
- **Animations:** AOS (Animate On Scroll)
- **Gallery:** Swiper.js carousel
- **Maps:** Leaflet + leaflet-elevation + leaflet-gpx
- **Forms:** EmailJS for registration
- **Fonts:** Inter (body), Oswald (headings), Noto Sans TC (Chinese)

## Color Scheme
| Color | Hex | Usage |
|-------|-----|-------|
| Primary (Teal) | #0d9488 | Main brand, buttons, highlights |
| Light Teal | #14b8a6 | Secondary accents |
| Accent (Amber) | #f59e0b | Time/achievement highlights |
| Rose | #e11d48 | "Last Year" section |
| Violet | #7c3aed | "The Challenge" section, testimonials |
| Dark | #0a0a0a | Background |

## File Structure
```
SaanKaaLaa/
├── index.html          # Main website
├── PROJECT.md          # This file
├── resize_photos.py    # Script to resize photos for web
├── assets/
│   ├── YYCHKWalker.gpx # 50K route GPX
│   ├── SKL_Logo.png    # Official logo
│   ├── head1.jpg       # Hero background
│   ├── banner1-3.jpg   # Section backgrounds
│   ├── start.png       # Map marker
│   ├── end.png         # Map marker
│   └── 2025/           # Photos from 2025 edition
│       ├── Original/   # Full resolution (DO NOT serve)
│       ├── thumb/      # 400px thumbnails
│       └── full/       # 1600px for lightbox
└── data/
    ├── finishers.json  # Hall of Finishers data
    └── testimonials.json # Challenger testimonials
```

## Data Files

### finishers.json
```json
{
  "teams": [
    {
      "id": 1,
      "name_zh": "隊伍中文名",
      "name_en": "Team English Name",
      "time": "12:34:56",
      "year": 2025,
      "category": "SKL50",
      "members": ["Name1", "Name2", "Name3", "Name4"],
      "icon": "users"
    }
  ]
}
```

### testimonials.json
```json
{
  "testimonials": [
    {
      "id": 1,
      "name": "Johnny",
      "year": 2025,
      "category": "SKL50",
      "quote_zh": "中文心聲全文...",
      "quote_en": "English testimonial...",
      "highlight_zh": "精選金句",
      "highlight_en": "Key highlight quote"
    }
  ]
}
```

## Key Features
- **Language toggle:** EN / 中文 — synced between floating switch and sticky nav
- **Distance toggle:** SKL50 / SKL100 — controls stats, route, and schedule sections
- **100K blur overlay:** Shows "Coming Soon" until details finalized
- **Dark theme:** Modern UTMB-inspired aesthetic
- **Responsive:** Mobile-first design
- **Sticky navigation:** Appears after scrolling past hero
- **2025 Recap section:**
  - Teams counter (auto-loaded from JSON)
  - Video embed (Vimeo)
  - Hall of Finishers (loaded from JSON)
  - Challenger Stories (testimonials from JSON)
  - Photo gallery (8 random photos, Swiper carousel)

## Social Links
- Instagram: [@yycoutdoorhker](https://www.instagram.com/yycoutdoorhker)
- Telegram: [yycOutdoorHK](https://t.me/yycOutdoorHK) — **Main communication channel**

## Development Notes
- Run local server: `python3 -m http.server 8080`
- Photo resizing: `python3 resize_photos.py`
- Registration emails go to: brknveggie@gmail.com

## For AI Assistants
When working on this project:
1. Keep bilingual (EN + Traditional Chinese HK style) — 香港口語
2. Brand names: "Saan Kaa Laa" (EN), "山卡旯" (ZH), "#SaanKaaLaa" (hashtag)
3. This is a **challenge**, not a race — keep wording approachable
4. 100K details are TBD — keep the blur overlay
5. Data-driven: Use JSON files for finishers/testimonials
6. Telegram is the main communication channel
