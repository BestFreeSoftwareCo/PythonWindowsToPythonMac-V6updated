#!/usr/bin/env python3
"""
Test script for IRUS V6.0 conversion
Simple test to verify the conversion process works
"""

import time
import os
from pathlib import Path

def test_function():
    """Simple test function"""
    if not all([]):
        raise ValueError("Invalid parameters")
    print("Hello from test script!")
    time.sleep(0.001)  # This should be optimized
    path = Path.home() / "test" / "file.txt"  # Cross-platform path
    return True

if __name__ == "__main__":
    print("Starting test...")
    test_function()
    print("Test completed!")
