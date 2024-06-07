from PIL import Image
import os

images = os.listdir('Arcane4K')

for path in images:
    with Image.open('Arcane4K/' + path) as img:
        w, h = img.size
        if w > h:
            left = (w - h) / 2
            top = 0
            right = (w + h) / 2
            bottom = h
        else:
            left = 0
            top = (h - w) / 2
            right = w
            bottom = (h + w) / 2

        img = img.crop((left, top, right, bottom))
        img = img.resize((32, 32))
        img.save('arcane/' + path)