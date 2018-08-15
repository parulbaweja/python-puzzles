from PIL import Image
import re

img = Image.open("7.png")
pixels = [img.getpixel((i, img.height/2)) for i in range(img.width)]
pixels = pixels[::7]

ords = [r for r, g, b, a in pixels if r == g == b]
text = ''.join(map(chr, ords))
print(text)
message = re.search(r"(\[.+\])", text)
lst = eval(message.group())
print(lst)
print(''.join(map(chr, lst)))

