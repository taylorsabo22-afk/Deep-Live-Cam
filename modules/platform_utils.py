"""
Platform detection and compatibility utilities for Deep-Live-Cam.
Supports Windows, macOS, Linux, and Android (via Termux).
"""

import os
import sys
import platform


def is_android() -> bool:
    """
    Detect if running on Android (typically via Termux).
    
    Returns:
        bool: True if running on Android, False otherwise
    """
    # Check for Android-specific environment variables
    if 'ANDROID_ROOT' in os.environ or 'ANDROID_DATA' in os.environ:
        return True
    
    # Check for Termux-specific paths
    if os.path.exists('/data/data/com.termux'):
        return True
    
    # Check system platform (some Android environments report 'linux')
    if platform.system().lower() == 'linux':
        # Additional checks for Android
        try:
            with open('/proc/version', 'r') as f:
                version_info = f.read().lower()
                if 'android' in version_info:
                    return True
        except:
            pass
    
    return False


def is_termux() -> bool:
    """
    Detect if running specifically in Termux environment.
    
    Returns:
        bool: True if running in Termux, False otherwise
    """
    return 'TERMUX_VERSION' in os.environ or os.path.exists('/data/data/com.termux')


def can_use_gui() -> bool:
    """
    Determine if GUI (tkinter) can be used on current platform.
    
    Returns:
        bool: True if GUI is available, False otherwise
    """
    # Android/Termux typically doesn't support tkinter
    if is_android():
        return False
    
    # Try to import tkinter to verify availability
    try:
        import tkinter
        return True
    except ImportError:
        return False


def get_platform_name() -> str:
    """
    Get a human-readable platform name.
    
    Returns:
        str: Platform name (e.g., 'Windows', 'macOS', 'Linux', 'Android')
    """
    if is_android():
        if is_termux():
            return 'Android (Termux)'
        return 'Android'
    
    system = platform.system()
    if system == 'Darwin':
        return 'macOS'
    return system


def get_camera_backend() -> str:
    """
    Get the appropriate camera backend for the current platform.
    
    Returns:
        str: Camera backend identifier ('opencv', 'android', 'directshow', etc.)
    """
    if is_android():
        return 'opencv'  # OpenCV works on Android with proper build
    elif platform.system() == 'Windows':
        return 'directshow'
    else:
        return 'opencv'


def should_force_headless() -> bool:
    """
    Determine if the application should run in headless mode due to platform constraints.
    
    Returns:
        bool: True if headless mode is required, False otherwise
    """
    return is_android() or not can_use_gui()


def get_recommended_execution_provider() -> str:
    """
    Get recommended ONNX execution provider for the platform.
    
    Returns:
        str: Recommended execution provider
    """
    if is_android():
        # Android best supports CPU or NNAPI (if available)
        return 'cpu'
    elif platform.system() == 'Darwin':
        # macOS can use CoreML
        return 'coreml'
    else:
        # Default to CPU, user can override for CUDA/DirectML/etc
        return 'cpu'


def print_platform_info():
    """Print detailed platform information for debugging."""
    print(f"Platform: {get_platform_name()}")
    print(f"System: {platform.system()}")
    print(f"Machine: {platform.machine()}")
    print(f"Python: {platform.python_version()}")
    print(f"Android: {is_android()}")
    print(f"Termux: {is_termux()}")
    print(f"GUI Available: {can_use_gui()}")
    print(f"Force Headless: {should_force_headless()}")
    print(f"Recommended Provider: {get_recommended_execution_provider()}")
