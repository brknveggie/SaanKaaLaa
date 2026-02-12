# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Saan Kaa Laa (山卡旯) is a static single-page website for a team trail challenge event in Calgary. The site is built with vanilla HTML/JavaScript—no build process required. Content is data-driven via JSON files.

## Development Commands

### Local Development
```bash
python -m http.server 8080
# Visit http://localhost:8080
```

### Photo Management
```bash
# Generate thumbnails/full-size images from originals
python3 resize_photos.py
# Note: Update SOURCE_DIR, THUMB_DIR, FULL_DIR paths at top of script first

# Generate photos.json for gallery (manual alternative to GitHub Actions)
./scripts/generate-photos-json.sh
```

### Git Workflow
- Main branch is `main` (GitHub Pages deploys from this)
- Photo changes to `assets/2025/full/` or `assets/2025/thumb/` trigger GitHub Actions to auto-update `data/photos.json`

## Architecture

### Monolithic HTML Structure
The entire application lives in `index.html` (~2200 lines). JavaScript is embedded directly within `<script>` tags. Content sections are organized as semantic HTML5 components that render dynamically based on JSON data.

### Data-Driven Content
All dynamic content is loaded from JSON files in `data/`:
- `finishers.json` - Hall of Finishers (teams, times, members, photos)
- `testimonials.json` - Challenger quotes and highlights
- `photos.json` - Auto-generated list of gallery photos

When adding new content, edit these JSON files rather than modifying HTML directly.

### Key Libraries (via CDN)
- **Tailwind CSS** - Styling with custom brand colors (teal `#0d9488`, amber `#f59e0b`)
- **Leaflet + leaflet-elevation + leaflet-gpx** - Interactive route map with GPX data
- **Swiper.js** - Photo gallery carousel
- **AOS** - Scroll animations
- **EmailJS** - Registration form handling

### Bilingual Support
The site supports English and Traditional Chinese (HK style). A language toggle switches between `data-i18n="en"` and `data-i18n="zh"` attributes throughout. All content strings exist in both languages.

### Photo Gallery System
Gallery photos are managed semi-automatically:
1. Add originals to `assets/2025/Original/`
2. Run `resize_photos.py` to generate `thumb/` (400px) and `full/` (1600px) versions
3. GitHub Actions automatically regenerates `data/photos.json` when pushed
4. JavaScript loads `photos.json` and randomly selects 8 photos for display

### Asset Organization
```
assets/
├── finishers/          # Team completion photos (referenced in finishers.json)
├── testimonials/        # Challenger avatars (referenced in testimonials.json)
└── 2025/
    ├── Original/        # Source photos (not served)
    ├── thumb/           # Gallery thumbnails (400px)
    └── full/            # Gallery full-size (1600px)
```

### Route Map Integration
The interactive map loads GPX data from `assets/YYCHKWalker.gpx`. Leaflet renders the trail route with start/end markers and an elevation profile. The map is initialized in the `initMap()` JavaScript function.

## Branding Guidelines
- **English name:** Saan Kaa Laa (with spaces)
- **Chinese name:** 山卡旯 (Traditional Chinese, HK style)
- **Hashtag:** #SaanKaaLaa (no spaces)
- **Primary color:** Teal `#0d9488`
- **Accent color:** Amber `#f59e0b`
- **Dark background:** `#0a0a0a`