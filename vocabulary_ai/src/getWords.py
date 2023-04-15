#!/usr/bin/env python3

import os
import shutil
import warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning, DependencyWarning

warnings.simplefilter('ignore', InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(category=DependencyWarning)

def main():
    # Ignore insecure request warnings
    warnings.simplefilter('ignore', InsecureRequestWarning)

    source = "/mnt/c/Users/ogarc/OneDrive/Desktop/Schedule_090918 - Definitions.csv"
    destination = "words.csv"

    # Check if the source file exists
    if os.path.isfile(source):
        try:
            # Copy the file from the source location to the destination
            shutil.copy(source, destination)
            # Remove the original file, effectively "moving" the file between filesystems
            os.remove(source)
        except Exception as e:
            print(f"Error while moving the file: {e}")
    else:
        print(f"File not found: {source}")

if __name__ == "__main__":
    main()

