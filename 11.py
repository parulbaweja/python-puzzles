from PIL import Image

img = Image.open("11.jpg")
rgb_img = img.convert("RGB")

new_size = (img.width//2, img.height//2)
even = Image.new(img.mode, new_size)
odd = Image.new(img.mode, new_size)
for i in range(img.width):
    for j in range(img.height):
        pixel = rgb_img.getpixel((i, j))
        if (i + j) % 2 == 0:
            even.putpixel((i//2, j//2), pixel)
        else:
            odd.putpixel((i//2, j//2), pixel)

even.show()
odd.show()
