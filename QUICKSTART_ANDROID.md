# Android Quick Start Guide

Quick reference for using Deep-Live-Cam on Android/Termux.

## Installation (Quick)

```bash
# Install Termux from F-Droid (not Google Play!)
# Open Termux and run:

pkg update && pkg upgrade -y
pkg install -y python git cmake ninja build-essential libjpeg-turbo libpng ffmpeg opencv
git clone https://github.com/hacksider/Deep-Live-Cam.git
cd Deep-Live-Cam
python -m venv venv
source venv/bin/activate
pip install -r requirements-android.txt
```

## Basic Usage

### Process Single Image
```bash
python run.py -s source.jpg -t target.jpg -o output.jpg
```

### Process Video (slow!)
```bash
python run.py -s source.jpg -t video.mp4 -o output.mp4 --keep-fps --keep-audio
```

### Multiple Faces
```bash
python run.py -s source.jpg -t photo.jpg -o output.jpg --many-faces
```

### Low Memory Mode
```bash
python run.py -s source.jpg -t target.jpg -o output.jpg --max-memory 2 --execution-threads 2
```

## Termux Storage Access

```bash
# Enable storage access first
termux-setup-storage

# Use these paths to access your files
~/storage/shared/Pictures/  # Pictures folder
~/storage/shared/DCIM/      # Camera photos
~/storage/shared/Download/  # Downloads
```

## Common Issues

**Out of memory?**
```bash
python run.py ... --max-memory 2 --execution-threads 2
```

**Too slow?**
- Use smaller images (resize first)
- Reduce video length/resolution
- Close other apps

**FFmpeg not found?**
```bash
pkg install ffmpeg
```

**Import errors?**
```bash
source venv/bin/activate  # Activate virtual environment
pip install --upgrade pip
pip install -r requirements-android.txt
```

## Performance Tips

1. **Resize images before processing:**
   ```bash
   pkg install imagemagick
   convert large.jpg -resize 50% smaller.jpg
   ```

2. **Extract short video clips:**
   ```bash
   ffmpeg -i long_video.mp4 -t 10 short_video.mp4
   ```

3. **Keep device cool** - Heavy processing generates heat

4. **Use good lighting** - Better face detection

## Full Documentation

- Complete guide: See [ANDROID.md](ANDROID.md)
- General usage: See [README.md](README.md)
- Examples: Run `python examples_android.py`

## Platform Check

```bash
python -c "from modules import platform_utils; platform_utils.print_platform_info()"
```

## Getting Help

- Check ANDROID.md for troubleshooting
- Verify all dependencies installed
- Report Android-specific issues on GitHub
