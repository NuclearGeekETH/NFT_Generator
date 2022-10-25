# Python 3
# sort all files in natural order then renumber the files starting at 4001

import os
import argparse
import re


def rename_files(directory=None):
    if not directory:
        # get the current working directory
        directory = os.getcwd()
    if directory == os.path.dirname(__file__):
        print("ERROR: You are about to rename all the files in the directory containing this scripts")
        exit()

    # get the list of files in the current working directory
    files = os.listdir(directory)

    # sort the files in natural order
    files.sort(key=lambda x: [int(c) if c.isdigit() else c for c in re.split('(\d+)', x)])

    # renumber the files starting at 4001
    for i in range(len(files)):
        print("renaming {name}".format(name=str(i+4001)+'.json'))
        #os.rename(files[i], str(i+4001)+'.json')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-d', '--directory', default=None, type=str, help='the directory containing the file you want to rename')
    arguments = parser.parse_args()
    rename_files(arguments.directory)
