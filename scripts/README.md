# Scripts

## generate-photos-json.sh

Automatically generates `data/photos.json` from photos in `assets/2025/full/`.

### Manual Usage

```bash
./scripts/generate-photos-json.sh
```

### How It Works

1. Scans `assets/2025/full/*.jpg`
2. Extracts filenames (without extension)
3. Generates `data/photos.json` with array of photo names
4. Website JavaScript loads this file dynamically

### Automatic Updates

The GitHub Action (`.github/workflows/generate-photos.yml`) runs automatically when:
- Photos are added/removed in `assets/2025/full/` or `assets/2025/thumb/`
- Pushed to `main` branch
- Manually triggered via GitHub Actions tab

The action will:
1. Run the generation script
2. Commit `data/photos.json` if it changed
3. Push back to the repo

### Benefits

- No hardcoded photo lists in HTML
- Add/remove photos by just updating the folders
- GitHub Pages automatically rebuilds with new photos
- Script can be run locally before committing

### Local Development

After adding/removing photos locally:

```bash
./scripts/generate-photos-json.sh
git add data/photos.json
git commit -m "Update gallery photos"
git push
```

Or just push the photo changes and let GitHub Actions handle it!
