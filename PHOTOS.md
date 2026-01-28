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
