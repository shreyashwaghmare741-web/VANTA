import os
import sys

# Get the project's root directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the src folder
SRC_DIR = os.path.join(ROOT_DIR, "src")

# Add src to Python's import path
sys.path.insert(0, SRC_DIR)

# Move into src so relative paths work
os.chdir(SRC_DIR)

# Start EON
from main import main

if __name__ == "__main__":
    main()