# Deep-Live-Cam for Android (Termux)

This guide explains how to run Deep-Live-Cam on Android devices using Termux.

## Important Notes

⚠️ **Performance Warning**: Deep-Live-Cam performs real-time AI face swapping which is computationally intensive. On Android devices:
- Processing will be **significantly slower** than on desktop/laptop
- Real-time face swapping may not be achievable on most Android devices
- Works best for **image processing** rather than video/live mode
- Recommended: Use a high-end Android device with at least 8GB RAM

⚠️ **GUI Limitation**: The GUI (customtkinter) does not work on Android. You must use **headless/CLI mode** only.

## Prerequisites

1. **Android Device Requirements**:
   - Android 7.0 or higher
   - At least 4GB RAM (8GB+ recommended)
   - At least 5GB free storage space
   - ARM64 processor (most modern Android devices)

2. **Install Termux**:
   - Download from [F-Droid](https://f-droid.org/en/packages/com.termux/) (recommended)
   - NOT from Google Play Store (outdated version)

## Installation

### Step 1: Set Up Termux Environment

Open Termux and run these commands:

```bash
# Update package lists
pkg update && pkg upgrade -y

# Install essential build tools and dependencies
pkg install -y python python-pip git cmake ninja build-essential

# Install media libraries
pkg install -y libjpeg-turbo libpng ffmpeg

# Install OpenCV dependencies
pkg install -y opencv
```

### Step 2: Clone Repository

```bash
# Navigate to storage (optional, for easier file access)
cd ~/storage/shared

# Clone the repository
git clone https://github.com/hacksider/Deep-Live-Cam.git
cd Deep-Live-Cam
```

### Step 3: Install Python Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate

# Install Android-compatible dependencies
pip install -r requirements-android.txt
```

**Note**: 
- Installation may take 30-60 minutes and require significant storage space.
- The requirements file uses PyTorch 2.6.0+ to address known security vulnerabilities.
- If you encounter issues, ensure you have at least 2GB free space for PyTorch alone.

### Step 4: Download Models

Download the required models and place them in the `models` folder:

1. [GFPGANv1.4.pth](https://huggingface.co/hacksider/deep-live-cam/resolve/main/GFPGANv1.4.pth)
2. [inswapper_128_fp16.onnx](https://huggingface.co/hacksider/deep-live-cam/resolve/main/inswapper_128_fp16.onnx)

You can download these on your Android device browser and move them to the models folder:

```bash
# Create models directory if it doesn't exist
mkdir -p models

# Move downloaded files (adjust path based on your download location)
mv ~/storage/downloads/GFPGANv1.4.pth models/
mv ~/storage/downloads/inswapper_128_fp16.onnx models/
```

## Usage

### Image Processing (Recommended for Android)

Process a single image with face swap:

```bash
python run.py \
  --source /path/to/source_face.jpg \
  --target /path/to/target_image.jpg \
  --output /path/to/output.jpg \
  --execution-provider cpu
```

Example:
```bash
python run.py \
  -s ~/storage/shared/Pictures/source.jpg \
  -t ~/storage/shared/Pictures/target.jpg \
  -o ~/storage/shared/Pictures/output.jpg
```

### Video Processing (Slow on Android)

Process a video file:

```bash
python run.py \
  --source /path/to/source_face.jpg \
  --target /path/to/video.mp4 \
  --output /path/to/output.mp4 \
  --execution-provider cpu \
  --keep-fps \
  --keep-audio
```

**Note**: Video processing will be very slow. Consider using a shorter video or lower resolution.

### Platform Information

Check if Android is properly detected:

```bash
python -c "from modules import platform_utils; platform_utils.print_platform_info()"
```

## Command Line Options

Deep-Live-Cam runs in headless mode on Android. Available options:

```
Required:
  -s, --source SOURCE_PATH       Source face image
  -t, --target TARGET_PATH       Target image or video
  -o, --output OUTPUT_PATH       Output file path

Optional:
  --frame-processor {face_swapper,face_enhancer}
                                 Frame processors to use
  --keep-fps                     Keep original video fps
  --keep-audio                   Keep original audio
  --many-faces                   Process every detected face
  --execution-provider {cpu}     Execution provider (use 'cpu' on Android)
  --execution-threads N          Number of CPU threads (default: 4)
  --max-memory N                 Maximum RAM in GB
```

## Troubleshooting

### Out of Memory Errors

If you encounter memory issues:

```bash
# Limit memory usage
python run.py -s source.jpg -t target.jpg -o output.jpg --max-memory 2

# Reduce execution threads
python run.py -s source.jpg -t target.jpg -o output.jpg --execution-threads 2
```

### Package Installation Failures

If pip packages fail to install:

```bash
# Update pip
pip install --upgrade pip setuptools wheel

# Install packages one by one to identify issues
pip install numpy
pip install opencv-python-headless
# ... continue with other packages
```

### OpenCV Issues

If OpenCV doesn't work:

```bash
# Reinstall OpenCV from Termux packages
pkg uninstall opencv
pkg install opencv python-opencv
```

### FFmpeg Not Found

```bash
# Install FFmpeg
pkg install ffmpeg

# Verify installation
which ffmpeg
ffmpeg -version
```

### Python Version Issues

Deep-Live-Cam requires Python 3.9+:

```bash
# Check Python version
python --version

# If version is too old, update Termux
pkg update && pkg upgrade
```

## Performance Tips

1. **Use Lower Resolution**: Resize images before processing
   ```bash
   # Using ImageMagick (install: pkg install imagemagick)
   convert large_image.jpg -resize 50% smaller_image.jpg
   ```

2. **Process Shorter Videos**: Split long videos into smaller segments
   ```bash
   # Using ffmpeg to extract first 10 seconds
   ffmpeg -i input.mp4 -t 10 output_short.mp4
   ```

3. **Close Other Apps**: Free up RAM by closing background apps

4. **Use Cooling**: Keep device cool to prevent thermal throttling

## Limitations

- ❌ No GUI support (tkinter doesn't work on Android)
- ❌ No real-time webcam mode (too slow for real-time processing)
- ❌ Limited GPU acceleration (most Android devices don't support CUDA/DirectML)
- ⚠️ Slower processing compared to desktop (CPU-only execution)
- ⚠️ High battery consumption during processing

## Alternative: Remote Processing

For better performance, consider using your Android device as a client to a desktop server:

1. Run Deep-Live-Cam on a desktop/laptop
2. Use SSH or a web interface to control it from Android
3. Transfer files via network share or cloud storage

Example using SSH:
```bash
# On Android (Termux)
ssh user@desktop-ip "cd Deep-Live-Cam && python run.py -s source.jpg -t target.jpg -o output.jpg"
```

## Support

For issues specific to Android/Termux:
1. Check Termux documentation: https://wiki.termux.com
2. Verify all dependencies are installed correctly
3. Report Android-specific issues on the GitHub repository

For general Deep-Live-Cam issues, see the main README.md
