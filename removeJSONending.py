# Python 3
# remove .json from files in directory

import os

for filename in os.listdir("."):
    if filename.endswith(".json"):
        os.rename(filename, filename[:-5])