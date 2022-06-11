import json
from copy import deepcopy
from math import comb
import random
from PIL import Image, ImageDraw, ImageFont
import re
import os
import numpy as np

namePrefix = "Framed Eyes"
description = "A collection of NFTs built with Python"
baseUri = "ipfs://NewUriToReplace"

layer1 = 'Eye/'
layer2 = 'Eyelid/'
layer3 = 'Frame/'

base = 'layers/'

combination_list = []

num = 0
max_nfts = 500

while num < max_nfts:
    def get_numbers_from_filename(filename):
        return re.search('#(.*).png',filename).group(1)

    def get_names_from_filename(filename):
        return re.search('^(.*?)#',filename).group(1)

    def get_layer(layer):
        layer_weights = []
        # layer_names = []
        filenames = []
        for filename in os.listdir(base + layer):
            weights = get_numbers_from_filename(filename)
            layer_weights.append(weights)
            filenames.append(filename)
        draw = np.random.choice(filenames, 1, p=layer_weights,)
        file_str = ' '.join(str(e) for e in draw)
        trait_name = get_names_from_filename(file_str)
        return trait_name, file_str

    layer1_draw, layer1_filename = get_layer(layer1)
    layer2_draw, layer2_filename = get_layer(layer2)
    layer3_draw, layer3_filename = get_layer(layer3)
    # layer4_draw, layer4_filename = get_layer(layer4)
    # layer5_draw, layer5_filename = get_layer(layer5)
    # layer6_draw, layer6_filename = get_layer(layer6)

    layer1_path = base + layer1 + layer1_filename
    layer2_path = base + layer2 + layer2_filename
    layer3_path = base + layer3 + layer3_filename
    # layer4_path = base + layer4 + layer4_filename
    # layer5_path = base + layer5 + layer5_filename
    # layer6_path = base + layer6 + layer6_filename

    # combination = layer1_draw + ',' + layer2_draw + ',' + layer3_draw + ',' + layer4_draw + ',' + layer5_draw + ',' + layer5_draw + ',' + layer6_draw
    combination = layer1_draw + ',' + layer2_draw + ',' + layer3_draw
    if combination in combination_list:
        print('combination exists')
    else:
        combination_list.append(combination)
        img = Image.open(layer1_path).convert('RGBA')
        img.alpha_composite(Image.open(layer2_path).convert('RGBA'))
        img.alpha_composite(Image.open(layer3_path).convert('RGBA'))
        # img.alpha_composite(Image.open(layer4_path).convert('RGBA'))
        # img.alpha_composite(Image.open(layer5_path).convert('RGBA'))
        # img.alpha_composite(Image.open(layer6_path).convert('RGBA'))
        img.save('build/images/' + str(num) + ".png")
        def create_meta():
            BASE_JSON = {
            "name": namePrefix + ' #' + str(num),
            "description": description,
            "image": baseUri,
            "attributes": []
            }

            item_json = deepcopy(BASE_JSON)
            item_json['attributes'].append({ 'trait_type': layer1[:-1], 'value': layer1_draw })
            item_json['attributes'].append({ 'trait_type': layer2[:-1], 'value': layer2_draw })
            item_json['attributes'].append({ 'trait_type': layer3[:-1], 'value': layer3_draw })
            # item_json['attributes'].append({ 'trait_type': layer4[:-1], 'value': layer4_draw })
            # item_json['attributes'].append({ 'trait_type': layer5[:-1], 'value': layer5_draw })
            # item_json['attributes'].append({ 'trait_type': layer6[:-1], 'value': layer6_draw })
            out = json.dumps(item_json)
            jsonoutput = open('build/metadata/' + str(num) + '.json', 'w')
            jsonoutput.write(out)

        create_meta()

        print(str(num) + ' created')

        num+=1







