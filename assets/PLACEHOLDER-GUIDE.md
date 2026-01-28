# Creating Placeholder Images (Optional)

If you want placeholder images while waiting for real photos:

## Option 1: Use ImageMagick (if installed)

```bash
# Finisher placeholder (800x600, dark with text)
convert -size 800x600 xc:'#1a1a1a' -gravity center \
  -pointsize 48 -fill '#0d9488' -annotate +0+0 'Team Photo' \
  assets/placeholder.jpg

# Testimonial placeholder (200x200, circular avatar style)
convert -size 200x200 xc:'#1a1a1a' -gravity center \
  -pointsize 24 -fill '#7c3aed' -annotate +0+0 'Photo' \
  assets/placeholder-avatar.jpg
```

## Option 2: Use any image editor
- Create 800x600px dark image with "Team Photo" text → save as `assets/placeholder.jpg`
- Create 200x200px dark image with person icon → save as `assets/placeholder-avatar.jpg`

## Option 3: Skip placeholders
The site will handle missing images gracefully. Add photos when ready!
