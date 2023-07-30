import os, sys
from PIL import Image, ImageOps

size = (36, 36)

def letterbox_image(image, size):
    '''resize image with unchanged aspect ratio using padding'''
    iw, ih = image.size
    w, h = size
    scale = min(w/iw, h/ih)
    nw = int(iw*scale)
    nh = int(ih*scale)

    image = image.resize((nw,nh), Image.LANCZOS)
    new_image = Image.new('RGB', size, (0,0,0))
    new_image.paste(image, ((w-nw)//2, (h-nh)//2))
    return new_image

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + "2.jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                # bg = Image.new("RGB", (im.width, im.height), (255, 255, 255))
                # mask = Image.new("L", im.size, 255)
                # # img.save("image.png", "PNG")
                # im = Image.composite(im, bg, mask)

                # im2 = ImageOps.fit(im, size, Image.LANCZOS, bleed=0.0, centering=(0.5,0.5))
                # im2.save("abc.jpg")

                # im3 = ImageOps.contain(im, size, Image.LANCZOS)
                # im3.save("abc2.jpg")
                im2 = letterbox_image(im, size)
                im2.save("abc.jpg")

        except OSError:
            print("cannot create thumbnail for", infile)