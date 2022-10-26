# Append JSON data

import os
import json
import argparse


def append_json(folder: str, field: str, ipfs_url: str):
    """
    Do through a set of json metadata files and add the field with the image urls added
    :param folder: the folder to read the metadata from
    :param field: the field to write the url to in the metadata
    :param ipfs_url: the ipfs_url to use for writing the image location in the json
    :return: nothing
    """
    if not ipfs_url:
        raise ValueError("ipfs_url value is not set")

    for x in range(0, 500):
        value = f"ipfs://{ipfs_url}/{x}.png"
        # if x.endswith(".json"):
        with open(os.path.join(folder, f'{x}.json'), 'r+') as f:
            data = json.load(f)
            data[field] = value
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-fd', '--folder', type=str, default='build/metadata/',
                        help='the folder to read the metadata from')
    parser.add_argument('-fi', '--field', type=str, default='image',
                        help='the field to write the url to in the metadata')
    parser.add_argument('-i', '--ipfs_url', type=str, default=None,
                        help='the ipfs_url to use for writing the image location in the json')

    arguments = parser.parse_args()
    append_json(arguments.folder, arguments.field, arguments.ipfs_url)


