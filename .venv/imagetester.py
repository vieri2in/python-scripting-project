from PIL import Image, ImageFilter
# img = Image.open("Pokedex/pikachu.jpg")
# # print(img) # size=640x640
# # filtered_img = img.filter(ImageFilter.BLUR)
# grayImage = img.convert("L")
# crooked = grayImage.rotate(90)
# crooked.show()
# crooked.save("Pokedex/gray.png","png")
imgAstro = Image.open('Pokedex/astro.jpg')
# print(imgAstro.size)
newImage = imgAstro.resize((400,400))
newImage.save('Pokedex/astro_thumbnail.jpg')
print(newImage)
