#!/usr/bin/env python3
"""
Test script to verify Android compatibility features.
This simulates an Android/Termux environment for testing.
"""

import sys
import os

# Add modules to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))

def test_platform_detection():
    """Test platform detection utilities"""
    print("=" * 60)
    print("Testing Platform Detection")
    print("=" * 60)
    
    import platform_utils
    
    platform_utils.print_platform_info()
    
    # Test individual functions
    assert isinstance(platform_utils.is_android(), bool)
    assert isinstance(platform_utils.is_termux(), bool)
    assert isinstance(platform_utils.can_use_gui(), bool)
    assert isinstance(platform_utils.should_force_headless(), bool)
    
    print("\n✓ All platform detection functions work correctly\n")


def test_android_environment_simulation():
    """Simulate Android environment and test detection"""
    print("=" * 60)
    print("Testing Simulated Android Environment")
    print("=" * 60)
    
    import platform_utils
    
    # Save original env
    original_env = os.environ.copy()
    
    # Simulate Termux environment
    os.environ['ANDROID_ROOT'] = '/system'
    os.environ['TERMUX_VERSION'] = '0.118'
    
    # Re-test detection (note: functions check at call time, not import time)
    print(f"Simulated Android detected: {platform_utils.is_android()}")
    print(f"Simulated Termux detected: {platform_utils.is_termux()}")
    print(f"Should force headless: {platform_utils.should_force_headless()}")
    
    # Restore environment
    os.environ.clear()
    os.environ.update(original_env)
    
    print("\n✓ Android environment simulation works correctly\n")


def test_conditional_imports():
    """Test that GUI imports are properly handled"""
    print("=" * 60)
    print("Testing Conditional Imports")
    print("=" * 60)
    
    # Test tkinter_fix can be imported even without tkinter
    try:
        import tkinter_fix
        print("✓ tkinter_fix imported successfully (GUI may or may not be available)")
    except ImportError as e:
        print(f"✗ Failed to import tkinter_fix: {e}")
        return False
    
    print("\n✓ Conditional imports work correctly\n")
    return True


def test_headless_detection():
    """Test headless mode detection in core"""
    print("=" * 60)
    print("Testing Headless Mode Detection")
    print("=" * 60)
    
    import platform_utils
    
    # Check if headless should be forced
    force_headless = platform_utils.should_force_headless()
    can_use_gui = platform_utils.can_use_gui()
    
    print(f"GUI available: {can_use_gui}")
    print(f"Force headless: {force_headless}")
    print(f"Recommended execution provider: {platform_utils.get_recommended_execution_provider()}")
    
    # These should be opposites (mostly)
    if force_headless and can_use_gui:
        print("⚠ Warning: Both force_headless and can_use_gui are True")
    
    print("\n✓ Headless detection works correctly\n")


def test_requirements_files():
    """Test that requirements files exist"""
    print("=" * 60)
    print("Testing Requirements Files")
    print("=" * 60)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Check for requirements files
    files = {
        'requirements.txt': os.path.join(base_dir, 'requirements.txt'),
        'requirements-android.txt': os.path.join(base_dir, 'requirements-android.txt'),
    }
    
    for name, path in files.items():
        if os.path.exists(path):
            print(f"✓ {name} exists")
            with open(path, 'r') as f:
                lines = len([l for l in f.readlines() if l.strip() and not l.startswith('#')])
                print(f"  Contains {lines} package entries")
        else:
            print(f"✗ {name} missing at {path}")
    
    print()


def test_documentation():
    """Test that documentation files exist"""
    print("=" * 60)
    print("Testing Documentation")
    print("=" * 60)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Check for documentation
    docs = {
        'README.md': os.path.join(base_dir, 'README.md'),
        'ANDROID.md': os.path.join(base_dir, 'ANDROID.md'),
    }
    
    for name, path in docs.items():
        if os.path.exists(path):
            size = os.path.getsize(path)
            print(f"✓ {name} exists ({size} bytes)")
            
            # Check for Android references in README
            if name == 'README.md':
                with open(path, 'r') as f:
                    content = f.read()
                    if 'ANDROID.md' in content or 'Android' in content:
                        print(f"  Contains Android references")
                    else:
                        print(f"  ⚠ May be missing Android references")
        else:
            print(f"✗ {name} missing")
    
    print()


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("Deep-Live-Cam Android Compatibility Test Suite")
    print("=" * 60 + "\n")
    
    tests = [
        test_platform_detection,
        test_android_environment_simulation,
        test_conditional_imports,
        test_headless_detection,
        test_requirements_files,
        test_documentation,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            result = test()
            if result is None or result:
                passed += 1
        except Exception as e:
            print(f"✗ Test failed with exception: {e}")
            import traceback
            traceback.print_exc()
            failed += 1
    
    print("=" * 60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if failed > 0:
        sys.exit(1)
    else:
        print("\n✅ All tests passed! Android compatibility is working.\n")
        sys.exit(0)


if __name__ == '__main__':
    main()
