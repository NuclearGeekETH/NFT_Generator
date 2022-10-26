# Python 3
# remove .json from files in directory

import os
import argparse


def remove_json_ending(directory: str = None):
    """
    Removes the json extension from files in a directory
    :param directory: the directory containing the files to rename
    :return: nothing
    """
    if not directory:
        directory = os.getcwd()

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            new_filename = filename[:-5]
            print(f"renaming {filename} to {new_filename}")
            os.rename(filename, new_filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-d', '--directory', default=None, type=str, help='the directory containing the files you want to rename')
    arguments = parser.parse_args()
    remove_json_ending(arguments.directory)
