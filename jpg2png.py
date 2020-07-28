import sys
import os
from PIL import Image, ImageFilter


# grab first and second argument
jpg_folder = sys.argv[1];
png_folder = sys.argv[2];

# check is new/exsits, if not create
if not os.path.exists(png_folder):
	os.mkdir(png_folder)


# loop trhough 1st folder, find jpg files
arr = os.listdir(jpg_folder)
for name in arr:
	if '.jpg' in  name:
		print(jpg_folder+'/'+name)
		img = Image.open(jpg_folder+'/'+name)
		img.save(png_folder+'/'+name[:-4]+'.png')


# convert to png format and save to the "new" folder

