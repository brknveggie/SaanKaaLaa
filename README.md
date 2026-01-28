# Saan Kaa Laa 山卡旯

<div align="center">

![Saan Kaa Laa Logo](assets/SKL_Logo.png)

**A self-organized team trail challenge in Calgary, Alberta**

[Website](https://brknveggie.github.io/SaanKaaLaa) • [Instagram](https://www.instagram.com/yycoutdoorhker) • [Telegram](https://t.me/yycOutdoorHK)

*"一個人走得快，一班人走得遠"*  
*If you want to go far, go together.*

</div>

---

## 🏔️ What is Saan Kaa Laa?

**Saan Kaa Laa 山卡旯** (Cantonese for "middle of nowhere") is a team trail challenge inspired by Trailwalker Hong Kong, bringing the spirit of long-distance team challenges to Hong Kong people living in Calgary.

This is a **challenge, not a race** — designed to be approachable while pushing teams to discover what they're capable of together in the backcountry.

### 2026 Edition
- **Date:** August 29, 2026
- **Registration Deadline:** July 29, 2026
- **Entry Fee:** $80 CAD per team (voluntary, to support the challenge)
- **Team Size:** 4 people (must start and finish together)

## 🎯 Challenge Categories

| Category | Distance | Elevation Gain | Time Limit | Status |
|----------|----------|----------------|------------|--------|
| **SKL50** | ~54km | ~1,950m | 14 hours | ✅ Active |
| **SKL100** | ~100km | TBD | 30 hours | 🔜 Coming Soon |

## 🗺️ SKL50 Route

Starting from Kananaskis Country, finishing at Allen Bill Day Use Area:

1. **Section 1:** Start → Aid Station 1 (15km, 500m↑) — Moderate
2. **Section 2:** Aid Station 1 → 2 (14km, 680m↑) — Difficult  
3. **Section 3:** Aid Station 2 → 3 (10.5km, 600m↑) — Easy
4. **Section 4:** Aid Station 3 → Finish (14.5km, 170m↑, 750m↓) — Easy

**Aid Stations:**
- Aid Station 1: Powderface Ridge Trailhead
- Aid Station 2: Elbow Falls Parking Lot (suggested cutoff: 2:00 PM)
- Aid Station 3: Moose Mountain Trailhead Parking

The route uses existing trail systems with GPX data available in `assets/YYCHKWalker.gpx`.

## 🌟 Philosophy

**This is not a race.** There are no prizes, no podiums, no winners and losers. Just teams challenging themselves to complete something difficult together.

We're inspired by Trailwalker Hong Kong — not copying it, but bringing that same team challenge spirit to let HK people in Calgary experience long-distance trail challenges in the Rockies.

**Teamwork over competition.** All 4 members must stay together and cross the finish line as a team.

## 💻 Technical Stack

- **Frontend:** Single-page app with vanilla HTML/JS
- **Styling:** Tailwind CSS (CDN)
- **Maps:** Leaflet + leaflet-elevation + leaflet-gpx
- **Gallery:** Swiper.js carousel
- **Animations:** AOS (Animate On Scroll)
- **Forms:** EmailJS integration for registration
- **Fonts:** Inter (body), Oswald (headings), Noto Sans TC (Chinese)

## 🗂️ Project Structure

```
SaanKaaLaa/
├── index.html              # Main website
├── README.md               # This file
├── resize_photos.py        # Photo processing script
├── assets/
│   ├── YYCHKWalker.gpx    # 50K route GPX data
│   ├── SKL_Logo.png       # Official logo
│   ├── head1.jpg          # Hero background
│   ├── banner1-3.jpg      # Section backgrounds
│   ├── start.png          # Map marker (start)
│   ├── end.png            # Map marker (finish)
│   └── 2025/              # 2025 edition photos
│       ├── Original/      # Full resolution (not served)
│       ├── thumb/         # 400px thumbnails
│       └── full/          # 1600px for lightbox
└── data/
    ├── finishers.json     # Hall of Finishers data
    └── testimonials.json  # Challenger testimonials
```

## 🎨 Branding

- **English name:** Saan Kaa Laa (with spaces)
- **Chinese name:** 山卡旯 (Traditional Chinese, HK style)
- **Hashtag:** #SaanKaaLaa (no spaces)
- **Color scheme:**
  - Primary (Teal): `#0d9488`
  - Accent (Amber): `#f59e0b`
  - Dark Background: `#0a0a0a`

## 🚀 Development

### Local Development
```bash
# Start local server
python3 -m http.server 8080

# Visit http://localhost:8080
```

### Photo Processing
```bash
# Resize photos for web (creates thumb/ and full/ directories)
python3 resize_photos.py
```

## 📝 Data Files

### finishers.json
Hall of Finishers data structure:
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
Challenger testimonials:
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

## 🌐 Features

- **Bilingual:** English / Traditional Chinese (HK style)
- **Distance toggle:** Switch between SKL50 and SKL100 info
- **Dark theme:** Modern UTMB-inspired aesthetic
- **Responsive design:** Mobile-first approach
- **Sticky navigation:** Appears after scrolling past hero
- **Interactive route map:** With elevation profile
- **2025 Recap:**
  - Video highlights
  - Hall of Finishers
  - Challenger testimonials
  - Photo gallery carousel

## 📞 Contact & Community

- **Email:** brknveggie@gmail.com
- **Instagram:** [@yycoutdoorhker](https://www.instagram.com/yycoutdoorhker)
- **Telegram:** [yycOutdoorHK](https://t.me/yycOutdoorHK) — **Main communication channel**

## 📜 License

This is a community-organized event. All rights reserved.

---

<div align="center">

**一個人走得快，一班人走得遠**  
If you want to go far, go together.

</div>
