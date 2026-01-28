# Photo Management Guide

## Finisher Team Photos

**Location:** `assets/finishers/`

### How to Add Team Photos

1. **Prepare the photo:**
   - Recommended size: 800x600px or similar landscape orientation
   - Format: JPG (best for photos)
   - File naming: Use team name in English, lowercase, with hyphens (e.g., `four-hikers.jpg`, `team-sloth.jpg`)

2. **Add to project:**
   ```bash
   # Copy photo to finishers directory
   cp your-team-photo.jpg assets/finishers/team-name.jpg
   ```

3. **Update JSON:**
   Edit `data/finishers.json` and add the `photo` field:
   ```json
   {
     "id": 1,
     "name_zh": "四Hike佬",
     "name_en": "Four Hikers",
     "time": "13:34:30",
     "year": 2025,
     "category": "SKL50",
     "members": ["Ben", "Gabbie", "Johnny", "Tin"],
     "photo": "assets/finishers/four-hikers.jpg"
   }
   ```

### Design Notes
- Photo becomes the card background with a dark gradient overlay
- Text appears at the bottom with drop shadows for readability
- Card has hover effect (slight zoom on photo)
- If no photo is specified, placeholder will be used

---

## Testimonial Photos

**Location:** `assets/testimonials/`

### How to Add Testimonial Photos

1. **Prepare the photo:**
   - Recommended size: 200x200px (square, will be cropped to circle)
   - Format: JPG
   - File naming: Use person's first name, lowercase (e.g., `johnny.jpg`)

2. **Add to project:**
   ```bash
   # Copy photo to testimonials directory
   cp person-photo.jpg assets/testimonials/johnny.jpg
   ```

3. **Update JSON:**
   Edit `data/testimonials.json` and add the `photo` field:
   ```json
   {
     "id": 1,
     "name": "Johnny",
     "year": 2025,
     "category": "SKL50",
     "photo": "assets/testimonials/johnny.jpg",
     "quote_zh": "...",
     "quote_en": "..."
   }
   ```

### Design Notes
- Photo appears as a circular avatar (48px diameter)
- Has a colored ring (violet) around it
- If no photo specified, placeholder will be used

---

## Placeholder Images

If you don't have photos yet:
- Finishers: Site will use `assets/placeholder.jpg` (dark background)
- Testimonials: Site will use `assets/placeholder-avatar.jpg` (generic avatar)

You can create simple placeholders or leave them until photos are ready.

---

## Gallery Photos (2025)

**Location:** `assets/2025/full/` and `assets/2025/thumb/`

### How to Add/Remove Gallery Photos

**Option 1: Automatic (Recommended)**
1. Add or remove photos in `assets/2025/full/` and `assets/2025/thumb/`
2. Push to GitHub
3. GitHub Actions automatically regenerates `data/photos.json`
4. Gallery updates automatically!

**Option 2: Manual**
1. Add/remove photos from both folders
2. Run: `./scripts/generate-photos-json.sh`
3. Commit: `git add data/photos.json && git commit -m "Update gallery photos"`
4. Push to GitHub

### Photo Requirements
- **Full size:** Place in `assets/2025/full/` (1600px recommended)
- **Thumbnail:** Place in `assets/2025/thumb/` (400px recommended)
- **Naming:** Both files must have the same name (e.g., `z62_8299.jpg`)
- **Format:** JPG

### How It Works
- Gallery photos are dynamically loaded from `data/photos.json`
- No hardcoded lists in HTML!
- Script scans `assets/2025/full/` and generates JSON
- Website shows 8 random photos from the available pool

See `scripts/README.md` for more details on the automation.

---

## Quick Commands

```bash
# Add finisher photo
cp ~/Downloads/team-photo.jpg assets/finishers/team-name.jpg

# Add testimonial photo
cp ~/Downloads/person-photo.jpg assets/testimonials/firstname.jpg

# Resize a photo (if needed)
convert input.jpg -resize 800x600^ -gravity center -extent 800x600 assets/finishers/output.jpg
```

---

**Updated:** 2026-01-29
