# Python 3
# sort all files in natural order then renumber the files starting at 4001

import os
import argparse
import re



def rename_files(directory: str = None, starting_offset: int = None):
    """

    :param directory: the directory containing the files to rename
    :param starting_offset: the starting numeric value for the offset
    :return: nothing
    :raises ValueError if the starting_offset is not present or the
    :raises Excpetion if the starting_offset is not present or the
    """
    if not starting_offset:
        raise ValueError("The starting_offset is not set.")

    if not directory:
        # get the current working directory
        directory = os.getcwd()

    current_script_path = os.path.dirname(os.path.realpath(__file__))
    if directory == current_script_path:
        raise Exception("You are about to rename all the files in the directory containing this scripts, you probably want to run this in a different directory or specify the directory at the command line.")

    # get the list of files in the current working directory
    files = os.listdir(directory)

    # sort the files in natural order
    files.sort(key=lambda x: [int(c) if c.isdigit() else c for c in re.split('(\d+)', x)])

    # renumber the files starting at 4001
    count = 0
    for file in files:
        print("renaming {orig} to {name}".format(orig=file, name=str(count+starting_offset)+'.json'))
        #os.rename(files[i], str(i+4001)+'.json')
        count += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-d', '--directory', default=None, type=str, help='the directory containing the files you want to rename')
    parser.add_argument('-s', '--starting_offset', default=4001, type=int,
                        help='the numerical offset to start the renaming at.')
    arguments = parser.parse_args()
    rename_files(arguments.directory, arguments.starting_offset)
    