import sys
import os
from PIL import Image
img_dir = sys.argv[1]
output_dir = sys.argv[2]
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
for filename in os.listdir(img_dir):
    clean_name = filename.split('.')[0]
    img = Image.open(os.path.join(img_dir, filename))
    img.save(os.path.join(output_dir, f'{clean_name}.png'),"png")
