from PIL import Image
import os
from tqdm import tqdm

image_folder = input('Image Folder:')
images = os.listdir(image_folder)
target_size = int(input('Target Size:'))
os.mkdir('resized')

for path in tqdm(images):
    with Image.open(os.path.join(image_folder, path)) as img:
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
        img = img.resize((target_size, target_size))
        img.save('resized/' + path)