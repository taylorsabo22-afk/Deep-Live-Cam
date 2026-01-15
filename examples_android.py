#!/usr/bin/env python3
"""
Example script demonstrating Deep-Live-Cam usage on Android/Termux.
This shows how to use the application in headless mode.
"""

import os
import sys

# Add modules to path to use platform_utils
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))

try:
    import platform_utils
    HAS_PLATFORM_UTILS = True
except ImportError:
    HAS_PLATFORM_UTILS = False


def print_header():
    """Print example script header."""
    print("=" * 70)
    print("Deep-Live-Cam Android Example")
    print("Headless Mode Image Processing")
    print("=" * 70)
    print()


def check_environment():
    """Check if running on Android/Termux."""
    if HAS_PLATFORM_UTILS:
        is_android = platform_utils.is_android()
        platform_name = platform_utils.get_platform_name()
        
        if is_android:
            print(f"✓ {platform_name} environment detected")
        else:
            print(f"ℹ Running on {platform_name}")
    else:
        # Fallback if platform_utils not available
        is_android = ('ANDROID_ROOT' in os.environ or 
                      'ANDROID_DATA' in os.environ or
                      'TERMUX_VERSION' in os.environ)
        
        if is_android:
            print("✓ Android/Termux environment detected")
        else:
            print("ℹ Running on standard desktop/laptop environment")
    
    print(f"Python version: {sys.version.split()[0]}")
    print()
    return is_android


def basic_image_swap():
    """Example: Basic face swap on a single image."""
    print("Example 1: Basic Image Face Swap")
    print("-" * 70)
    print()
    print("Command:")
    print("  python run.py \\")
    print("    --source /path/to/source_face.jpg \\")
    print("    --target /path/to/target_image.jpg \\")
    print("    --output /path/to/output.jpg")
    print()
    print("This will swap the face from source_face.jpg onto target_image.jpg")
    print()


def video_processing():
    """Example: Process a video file."""
    print("Example 2: Video Face Swap")
    print("-" * 70)
    print()
    print("Command:")
    print("  python run.py \\")
    print("    --source /path/to/source_face.jpg \\")
    print("    --target /path/to/video.mp4 \\")
    print("    --output /path/to/output.mp4 \\")
    print("    --keep-fps \\")
    print("    --keep-audio \\")
    print("    --execution-provider cpu")
    print()
    print("Note: Video processing can be very slow on Android devices.")
    print("Consider using shorter videos or lower resolution.")
    print()


def multiple_faces():
    """Example: Process multiple faces."""
    print("Example 3: Swap All Faces in Image")
    print("-" * 70)
    print()
    print("Command:")
    print("  python run.py \\")
    print("    --source /path/to/source_face.jpg \\")
    print("    --target /path/to/group_photo.jpg \\")
    print("    --output /path/to/output.jpg \\")
    print("    --many-faces")
    print()
    print("This will swap all detected faces in the target image.")
    print()


def resource_limited():
    """Example: Running on low-resource Android device."""
    print("Example 4: Low-Resource Mode (for older Android devices)")
    print("-" * 70)
    print()
    print("Command:")
    print("  python run.py \\")
    print("    --source /path/to/source.jpg \\")
    print("    --target /path/to/target.jpg \\")
    print("    --output /path/to/output.jpg \\")
    print("    --max-memory 2 \\")
    print("    --execution-threads 2 \\")
    print("    --execution-provider cpu")
    print()
    print("This limits RAM usage and CPU threads for devices with limited resources.")
    print()


def termux_paths():
    """Example: Using Termux storage paths."""
    print("Example 5: Using Termux Storage Paths")
    print("-" * 70)
    print()
    print("On Termux, you need to set up storage access first:")
    print("  termux-setup-storage")
    print()
    print("Then you can access your device's storage:")
    print()
    print("Command:")
    print("  python run.py \\")
    print("    --source ~/storage/shared/Pictures/source.jpg \\")
    print("    --target ~/storage/shared/Pictures/target.jpg \\")
    print("    --output ~/storage/shared/Pictures/output.jpg")
    print()
    print("Storage locations:")
    print("  ~/storage/shared/        - Internal storage")
    print("  ~/storage/shared/DCIM/   - Camera photos")
    print("  ~/storage/shared/Pictures/ - Pictures folder")
    print("  ~/storage/shared/Download/ - Downloads folder")
    print()


def batch_processing():
    """Example: Processing multiple images."""
    print("Example 6: Batch Processing (Multiple Images)")
    print("-" * 70)
    print()
    print("Bash script to process multiple images:")
    print()
    print("#!/bin/bash")
    print("SOURCE='source_face.jpg'")
    print("for TARGET in *.jpg; do")
    print("  if [ \"$TARGET\" != \"$SOURCE\" ]; then")
    print("    OUTPUT=\"swapped_${TARGET}\"")
    print("    python run.py -s \"$SOURCE\" -t \"$TARGET\" -o \"$OUTPUT\"")
    print("  fi")
    print("done")
    print()
    print("Save this as process_batch.sh, make it executable (chmod +x process_batch.sh),")
    print("and run it to process all images in a folder.")
    print()


def main():
    """Run all examples."""
    print_header()
    
    is_android = check_environment()
    
    if not is_android:
        print("⚠ Warning: These examples are for Android/Termux environments.")
        print("They will also work on desktop systems, but desktop users typically")
        print("use the GUI interface instead.")
        print()
    
    # Show all examples
    basic_image_swap()
    video_processing()
    multiple_faces()
    resource_limited()
    termux_paths()
    batch_processing()
    
    print("=" * 70)
    print("For more information, see:")
    print("  - ANDROID.md for detailed Android/Termux setup")
    print("  - README.md for general usage and features")
    print("=" * 70)
    print()


if __name__ == '__main__':
    main()
