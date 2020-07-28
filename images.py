from PIL import Image, ImageFilter

img = Image.open('./image_playground/pikachu.jpg')

img2= img.filter(ImageFilter.BLUR)
filtered_img = img2.filter(ImageFilter.SHARPEN)
filtered_img.save('./image_playground/sharpened_pikachu.png')
img3 = img.convert('L')
img3.save('./image_playground/grey_pikachu.png')
resize = img3.resize((300,300))
resize.save('./image_playground/resize_grey_pikachu.png')
resize.show()

img = Image.open('./image_playground/astr.jpg')
resize = img.resize((400,400))
resize.save('./image_playground/resize_astr.png')
img.thumbnail((400, 400))
img.save('./image_playground/astr_thumbnail.jpg')

#print(dir(img))
