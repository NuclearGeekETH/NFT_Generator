#Append JSON data

import os
import json

folder = 'build/metadata/'
field = "image"

for x in range(0, 500):
    value = ("ipfs://UPDATE URI HERE/" + str(x) + ".png")
    # if x.endswith(".json"):
    with open(os.path.join(folder, str(x) + ".json"), 'r+') as f:
        data = json.load(f)
        data[field] = value
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()
