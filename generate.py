import argparse
import json
from PIL import Image
import re
import os
import numpy as np
from typing import Dict, List


def _get_numbers_from_filename(filename):
    return re.search('#(.*).png', filename).group(1)


def _get_names_from_filename(filename):
    return re.search('^(.*?)#', filename).group(1)


def _get_layer(base, layer):
    layer_weights = []
    filenames = []
    for filename in os.listdir(f'{base}/{layer}/'):
        weights = _get_numbers_from_filename(filename)
        layer_weights.append(weights)
        filenames.append(filename)
    draw = np.random.choice(filenames, 1, p=layer_weights)
    file_str = ' '.join(str(e) for e in draw)
    trait_name = _get_names_from_filename(file_str)
    return trait_name, file_str


def _create_meta(name_prefix: str, num: int, description: str, base_uri: str, trait_attributes: Dict[str, str]):
    """

    :param name_prefix:
    :param num:
    :param description:
    :param base_uri:
    :param trait_attributes:
    :return:
    """
    item_json = {
        "name": f'{name_prefix} #{num}',
        "description": description,
        "image": base_uri,
        "attributes": []
    }
    for trait, value in trait_attributes.items():
        item_json['attributes'].append({'trait_type': trait, 'value': value})
    jsonoutput = open(f'build/metadata/{num}.json', 'w')
    jsonoutput.write(json.dumps(item_json))


def generate(name_prefix: str = None, description: str = None, base_uri: str = None, base_layer_directory: str = None, layers: List[str] = None, max_nfts: int = 500, starting_num: int = 0):
    """

    :param name_prefix: The name for your project
    :param description: The description for your project
    :param base_uri: The base ipfs uri for your project
    :param base_layer_directory: The base directory where all the layers are stored
    :param layers: The list of layers in the base_layer_directory to be combined
    :param max_nfts: The maximum number of nfts to generate
    :return: nothing
    """
    if not name_prefix:
        raise ValueError("name_prefix not defined")
    if not description:
        raise ValueError("description not defined")
    if not base_uri:
        raise ValueError("base_uri not defined")
    if not layers:
        raise ValueError("layers not defined")
    if not max_nfts:
        raise ValueError("max_nfts not defined")

    nft_number = starting_num
    count = 0
    combination_list = []

    while count < max_nfts:
        trait_attributes = {}
        layers_draw = []
        layers_path = []
        for layer in layers:
            layer_draw, layer_filename = _get_layer(base_layer_directory, layer)
            trait_attributes[layer] = layer_draw

            layers_draw.append(layer_draw)
            layers_path.append(f'{base_layer_directory}/{layer}/{layer_filename}')

        combination = ",".join(layers_draw)
        if combination in combination_list:
            print('combination exists')
        else:
            combination_list.append(combination)
            img = Image.open(layers_path[0]).convert('RGBA')
            for layer_path in layers_path[1:]:
                img.alpha_composite(Image.open(layer_path).convert('RGBA'))
            img.save(f'build/images/{nft_number}.png')
            _create_meta(name_prefix, nft_number, description, base_uri, trait_attributes)

            print(f'{nft_number} created')
            nft_number += 1
            count += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-n', '--name_prefix', default="Framed Eyes", type=str, help='The name prefix for your project')
    parser.add_argument('-d', '--description', default="A collection of NFTs built with Python", type=str,
                        help='The description of your collection.')
    parser.add_argument('-u', '--base_uri', default="ipfs://NewUriToReplace", type=str, help='The name prefix for your project')
    parser.add_argument('-b', '--base_layer_directory', default="layers", type=str,
                        help='the location of the layer directories relative to the script')

    parser.add_argument('-l', '--layers', type=json.loads, default='["Eye", "Eyelid", "Frame"]',
                        help='use to define layer subdirectories in the base_layer_directory, expects json in format \'["Eye", "Eyelid", "Frame"]\'')

    parser.add_argument('-m', '--max_nfts', default=500, type=int,
                        help='the maximum number of nfts to generate')
    parser.add_argument('-s', '--starting_number', default=0, type=int,
                        help='the starting number to use for creating the images')

    arguments = parser.parse_args()
    generate(arguments.name_prefix, arguments.description, arguments.base_uri, arguments.base_layer_directory, arguments.layers, arguments.max_nfts, arguments.starting_number)
