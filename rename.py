# Python 3
# sort all files in natural order then renumber the files starting at 4001

import os
import sys
import re

# get the current working directory
cwd = os.getcwd()

# get the list of files in the current working directory
files = os.listdir(cwd)

# sort the files in natural order
files.sort(key=lambda x: [int(c) if c.isdigit() else c for c in re.split('(\d+)', x)])

# renumber the files starting at 4001
for i in range(len(files)):
    os.rename(files[i], str(i+4001)+'.json')