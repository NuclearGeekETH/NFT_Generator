from PIL import Image
import os


width = 1920
height = 1080
row = 8
# create a new image with a size of 28 x 28
new_image = Image.new('RGB', (width, height))
path = 'collage'
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
    newsize = int(width/row), int(width/row)
    new = images[i].resize(newsize)
    new_image.paste(new, (x, y))
    if x + new.width == new_image.width:
        x = 0
        y = y + new.height
    else:
        x = x + new.width

# save the new image
new_image.save('collage.png')