import argparse

from PIL import Image
import os


def create_collage(width: int = None, height: int = None, rows: int = None, path: str = None, output_filename: str = None):
    """

    :param width: the width of the collage
    :param height: the height of the collage
    :param rows: the number of rows in the collage
    :param path: the path of the files to be used to create the collage
    :param output_filename: the output filename for the final collage
    :return: nothing
    """
    if not width:
        raise ValueError("width not defined")
    if not height:
        raise ValueError("height not defined")
    if not rows:
        raise ValueError("rows not defined")
    if not path:
        raise ValueError("path not defined")
    if not output_filename:
        output_filename = 'collage'

    # create a new image with a size of 28 x 28
    new_image = Image.new('RGB', (width, height))
    # open all images and put them in a list
    images = []
    for file in os.listdir(path):
        f = os.path.join(path, file)
        if file.endswith('.png'):
            images.append(Image.open(f))

    # paste images into the new image
    x = 0
    y = 0
    for i in range(0, len(images)):
        newsize = int(width/rows), int(width/rows)
        new = images[i].resize(newsize)
        new_image.paste(new, (x, y))
        if x + new.width == new_image.width:
            x = 0
            y = y + new.height
        else:
            x = x + new.width

    print(f"Saving {output_filename}.png")
    # save the new image
    new_image.save(f'{output_filename}.png')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-W', '--width', default=1920, type=int, help='the width of the collage')
    parser.add_argument('-H', '--height', default=1080, type=int, help='the height of the collage')
    parser.add_argument('-r', '--rows', default=8, type=int, help='the number of rows in the collage')
    parser.add_argument('-p', '--path', default='collage', type=int,
                        help='the directory which contains the files to be made into the collage')
    parser.add_argument('-o', '--output_filename', default='collage', type=int,
                        help='the name of the output file, don\'t include the file extension')
    arguments = parser.parse_args()
    create_collage(arguments.width, arguments.height, arguments.rows, arguments.path, arguments.output_filename)
