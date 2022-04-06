from wand.image import Image

def shitify(img):
    with Image(filename = img) as image:
        with Image(filename ='shit.png') as water:
            with image.clone() as watermark:
                for i in range(0, 21):
                    for j in range(0, 21):
                        watermark.watermark(water, 0.5, int(image.width/20*j), int(image.width/20*i))
                watermark.save(filename ='shitted.jpg')