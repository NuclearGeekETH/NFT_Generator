# make a gif from frames in a folder
import argparse
import imageio.v2 as imageio
import os
from tqdm import tqdm


def make_gif(inpath: str, outpath: str, delay: float, final_delay: float, loop: bool):
    """

    :param inpath: directory containing the png images to combine into a gif
    :param outpath: the output filename and directory for the final animated gif
    :param delay: the frame delay between images
    :param final_delay: the final delay, if not set defaults to None
    :param loop: whether the animation should loop, defaults to False
    :return: nothing
    """
    # get images
    images = []
    print("Combining images")
    for f in tqdm(sorted(os.listdir(inpath))):
        if f.endswith('.png'):
            images.append(imageio.imread(inpath+'/'+f))
    # save gif
    print("Saving gif, this may take a few minutes depending on the number of images you are combining")
    imageio.mimsave(outpath, images, duration=delay, loop=loop)
    # add final delay frame
    if final_delay:
        imageio.imwrite(outpath, imageio.core.util.Array([0,0,0,0]).astype('uint8'), format='GIF', duration=final_delay)
    print("Gif creation complete")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-i', '--inpath', type=str, default='build/images/',
                        help='directory containing the png images to combine into a gif')
    parser.add_argument('-o', '--outpath', type=str, default='gif/output.gif',
                        help='the output filename and directory for the final animated gif')
    parser.add_argument('-d', '--delay', type=float, default=0.2,
                        help='the frame delay between images')
    parser.add_argument('-fd', '--final_delay', type=float, default=None,
                        help='the final delay')
    parser.add_argument('-l', '--loop', default=False, action='store_true')

    arguments = parser.parse_args()
    make_gif(arguments.inpath, arguments.outpath, arguments.delay, arguments.final_delay, arguments.loop)
