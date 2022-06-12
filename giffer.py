# make a gif from frames in a folder

import imageio
import os

inpath = 'build/images/'
outpath = 'gif/output.gif'

def make_gif(inpath1, outpath2, delay, finalDelay, loop):
    # get images
    images = []
    for f in sorted(os.listdir(inpath1)):
        if f.endswith('.png'):
            images.append(imageio.imread(inpath1+'/'+f))
    # save gif
    imageio.mimsave(outpath2, images, duration=delay, loop=loop)
    # add final delay frame
    # imageio.imwrite(outpath2, imageio.core.util.Array([0,0,0,0]).astype('uint8'), format='GIF', duration=finalDelay)

if __name__ == "__main__":
    delay = 0.2
    finalDelay = 0.5
    loop = 0
    make_gif(inpath, outpath, delay, finalDelay, loop)