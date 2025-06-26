from PIL import Image, ImageDraw


img = Image.new("RGB", size=(100, 100), color=(238, 238, 238))


draw = ImageDraw.Draw(img)


draw.polygon(
    xy=[(10, 10), (90, 10), (90, 90), (10, 90)],
    outline=(0, 0, 0),
    width=10
)


img.show()  

