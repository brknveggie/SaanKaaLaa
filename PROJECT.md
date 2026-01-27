# SaanKaaLaa 山卡旯 - Project Documentation

## Overview
**SaanKaaLaa 山卡旯** is a self-organized team trail challenge event in Calgary, Alberta, inspired by Trailwalker Hong Kong. The goal is to bring the team challenge experience to Hong Kong people living in Calgary.

- **Website:** Single-page event site (`index.html`)
- **Target audience:** Primarily Hong Kong people in Calgary (bilingual EN/Traditional Chinese HK style)
- **Event philosophy:** "一個人走得快，一班人走得遠" (If you want to go far, go together)

## Event Details

### 2026 Edition
- **Date:** August 29, 2026
- **Registration deadline:** July 29, 2026 (one month before)
- **Entry fee:** $80 CAD per team (voluntary, to support the race)
- **Team size:** 4 people (must start and finish together)
- **Contact:** brknveggie@gmail.com

### Race Categories
| Category | Distance | Status | Notes |
|----------|----------|--------|-------|
| **SKL50** | ~54K | Active | Full route info available |
| **SKL100** | ~100K | Coming Soon | Same finish point, different (earlier) start — extension before 50K route |

### Route (SKL50)
- Uses existing GPX: `assets/YYCHKWalker.gpx`
- **Aid Stations:**
  1. Powderface Ridge Trailhead (15km)
  2. Elbow Fall Parking Lot (29km) — suggested cutoff 2:00 PM
  3. Moose Mountain Trailhead Parking (39.5km)
- **Finish:** Allen Bill Day Use Area (54km)
- **Total elevation:** ~1,950m gain
- **Time limit:** 14 hours (6:00 AM - 8:00 PM)

### Route (SKL100)
- Different start point, same finish as SKL50
- Details TBD — currently shows "Coming Soon" overlay on website

## Inspiration
Inspired by **Trailwalker Hong Kong** — not a copy, but bringing the team challenge spirit to let HK people in Calgary experience long-distance team racing. The name 山卡旯 (SaanKaaLaa) is Cantonese slang for "middle of nowhere" — fitting for Calgary's backcountry trails.

## Technical Stack
- **Frontend:** Single HTML file with Tailwind CSS (CDN)
- **Maps:** Leaflet + leaflet-elevation + leaflet-gpx
- **Forms:** EmailJS for registration
- **Hosting:** TBD (likely GitHub Pages or similar)

## File Structure
```
SaanKaaLaa/
├── index.html          # Main website
├── PROJECT.md          # This file
├── resize_photos.py    # Script to resize photos for web
├── assets/
│   ├── YYCHKWalker.gpx # 50K route GPX
│   ├── SKL_Logo.png    # Official logo (used in hero)
│   ├── head1.jpg       # Hero background image
│   ├── start.png       # Map marker
│   ├── end.png         # Map marker
│   └── 2025/           # Photos from 2025 edition
│       ├── Original/   # Full resolution originals (DO NOT serve directly)
│       ├── thumb/      # 400px thumbnails for gallery grid
│       └── full/       # 1600px for lightbox viewing
```

## Photo Management
- **Original photos** go in `assets/2025/Original/`
- Run `python3 resize_photos.py` to generate web-optimized versions
- Thumbnails (400px) → `assets/2025/thumb/`
- Full size (1600px) → `assets/2025/full/`
- Gallery shows 8 random photos on each page load
- Lightbox supports left/right navigation

## Key Features
- **Language toggle:** EN / 中文 (Traditional Chinese, HK wording)
- **Distance toggle:** SKL50 / SKL100 — single toggle above Route section controls BOTH route and timeline/schedule sections together
- **100K blur overlay:** Shows "Coming Soon" until details finalized
- **Responsive design:** Mobile-friendly
- **2025 Recap section:** Photo gallery (8 random photos, shuffled, no duplicates) + testimonials (placeholders for now)
- **Promo video:** Vimeo embed (video ID: 1141338574)

## Design Direction
- Current: Clean, functional V1
- Future goal: More UTMB-style aesthetic (V2)
- Color scheme: `race-red` (#dc2626), `race-blue` (#2563eb), `race-yellow` (#eab308)

## Hidden/Prepared Sections
- **Sponsors section:** Hidden in HTML, ready to unhide when sponsors confirmed

## Social
- Instagram: [@yycoutdoorhker](https://www.instagram.com/yycoutdoorhker)
- Telegram: [yycOutdoorHK](https://t.me/yycOutdoorHK)
- Hashtag: #SaanKaaLaa

## Development Notes
- Photos: Placeholders in gallery; Max will upload actual photos to `assets/2025/` later
- Video: Placeholder for 2025 highlight video
- Registration: Currently EmailJS form; may upgrade to proper system later

## For AI Assistants
When working on this project:
1. Keep bilingual (EN + Traditional Chinese HK style) — 香港口語
2. Maintain the brand: "SaanKaaLaa 山卡旯" is the brand, "SKL50"/"SKL100" are race categories
3. Don't change core event philosophy — it's about team challenge, not individual racing
4. 100K details are TBD — keep the blur overlay until Max provides route info
5. Check `assets/` for available images before adding placeholders
