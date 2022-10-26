# make a gif from frames in a folder
import argparse
import imageio
import os


def make_gif(inpath: str, outpath: str, delay: float, final_delay: float, loop: bool):
    # get images
    images = []
    for f in sorted(os.listdir(inpath)):
        if f.endswith('.png'):
            images.append(imageio.imread(inpath+'/'+f))
    # save gif
    imageio.mimsave(outpath, images, duration=delay, loop=loop)
    # add final delay frame
    if final_delay:
        imageio.imwrite(outpath, imageio.core.util.Array([0,0,0,0]).astype('uint8'), format='GIF', duration=final_delay)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-i', '--inpath', type=str, default='build/images/',
                        help='directory containing the png images to combine into a gif')
    parser.add_argument('-i', '--outpath', type=str, default='gif/output.gif',
                        help='the output filename and directory for the final animated gif')
    parser.add_argument('-d', '--delay', type=float, default=0.2,
                        help='the frame delay between images')
    parser.add_argument('-fd', '--final_delay', type=float, default=None,
                        help='the final delay')
    parser.add_argument('-l', '--loop', default=False, action='store_true')

    arguments = parser.parse_args()
    make_gif(arguments.inpath, arguments.outpath, arguments.delay, arguments.final_delay, arguments.loop)
