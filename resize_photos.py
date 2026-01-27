#!/usr/bin/env python3
"""
Resize photos for web distribution:
- Thumbnails: 400px (for gallery grid)
- Full: 1600px (for lightbox viewing)
Both maintain aspect ratio and use high-quality JPEG compression
"""

import os
from PIL import Image
from pathlib import Path

SOURCE_DIR = Path("/home/msze/clawd/SaanKaaLaa/assets/2025/Original")
THUMB_DIR = Path("/home/msze/clawd/SaanKaaLaa/assets/2025/thumb")
FULL_DIR = Path("/home/msze/clawd/SaanKaaLaa/assets/2025/full")

THUMB_SIZE = 600  # px (longest edge)
FULL_SIZE = 1600  # px (longest edge)
JPEG_QUALITY = 85  # Good balance of quality/size

def resize_image(src_path, dest_path, max_size):
    """Resize image maintaining aspect ratio"""
    with Image.open(src_path) as img:
        # Handle EXIF orientation
        try:
            from PIL import ExifTags
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = img._getexif()
            if exif is not None:
                orientation_value = exif.get(orientation)
                if orientation_value == 3:
                    img = img.rotate(180, expand=True)
                elif orientation_value == 6:
                    img = img.rotate(270, expand=True)
                elif orientation_value == 8:
                    img = img.rotate(90, expand=True)
        except (AttributeError, KeyError, IndexError):
            pass
        
        # Convert to RGB if necessary (for PNG with transparency)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        # Calculate new size maintaining aspect ratio
        ratio = max_size / max(img.size)
        if ratio < 1:  # Only resize if larger than target
            new_size = tuple(int(dim * ratio) for dim in img.size)
            img = img.resize(new_size, Image.Resampling.LANCZOS)
        
        # Save as JPEG
        img.save(dest_path, 'JPEG', quality=JPEG_QUALITY, optimize=True)
        return True

def main():
    # Create output directories
    THUMB_DIR.mkdir(parents=True, exist_ok=True)
    FULL_DIR.mkdir(parents=True, exist_ok=True)
    
    # Get all images
    images = list(SOURCE_DIR.glob("*.jpg")) + list(SOURCE_DIR.glob("*.JPG")) + \
             list(SOURCE_DIR.glob("*.jpeg")) + list(SOURCE_DIR.glob("*.JPEG")) + \
             list(SOURCE_DIR.glob("*.png")) + list(SOURCE_DIR.glob("*.PNG"))
    
    print(f"Found {len(images)} images to process")
    
    for i, src in enumerate(sorted(images), 1):
        name = src.stem.lower() + ".jpg"
        thumb_path = THUMB_DIR / name
        full_path = FULL_DIR / name
        
        print(f"[{i}/{len(images)}] Processing {src.name}...")
        
        try:
            resize_image(src, thumb_path, THUMB_SIZE)
            resize_image(src, full_path, FULL_SIZE)
        except Exception as e:
            print(f"  Error: {e}")
            continue
    
    print(f"\nDone! Created thumbnails in {THUMB_DIR}")
    print(f"Created full-size in {FULL_DIR}")
    
    # List file sizes
    thumb_total = sum(f.stat().st_size for f in THUMB_DIR.glob("*.jpg"))
    full_total = sum(f.stat().st_size for f in FULL_DIR.glob("*.jpg"))
    print(f"\nThumb total: {thumb_total / 1024 / 1024:.1f} MB")
    print(f"Full total: {full_total / 1024 / 1024:.1f} MB")

if __name__ == "__main__":
    main()
