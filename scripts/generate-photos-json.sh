#!/bin/bash
# Generate photos.json from assets/2025/full/*.jpg

set -e

cd "$(dirname "$0")/.."

echo "🔍 Scanning assets/2025/full/ for photos..."

ls assets/2025/full/*.jpg 2>/dev/null | xargs -n1 basename | sed 's/.jpg$//' | \
python3 -c "import sys, json; photos = [line.strip() for line in sys.stdin if line.strip()]; print(json.dumps({'photos': photos}, indent=2))" \
> data/photos.json

PHOTO_COUNT=$(cat data/photos.json | python3 -c "import sys, json; print(len(json.load(sys.stdin)['photos']))")

echo "✅ Generated data/photos.json with $PHOTO_COUNT photos"
