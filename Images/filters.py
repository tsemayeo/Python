from PIL import Image
#Opens File
def load_img(filename):
  im = Image.open(filename)
  return im
#Shows Image
def show_img(im):
  im.show()
# Saves Image
def save_img(im, filename):
  im.save(filename, "jpeg")
  show_img(im)

def obamaIcon(im):
    pixels = im.getdata()
    newPixels = []

    darkBlue = (0,51,76)
    red = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252,227,166)
# changing the intensity
    for p in pixels:
        intensity = p[0]+p[1]+p[2]

        if intensity in range(0,182):
            newPixels.append(darkBlue)
        elif intensity in range(183, 364):
            newPixels.append(red)
        elif intensity in range(365, 564):
            newPixels.append(lightBlue)
        else:
            newPixels.append(yellow)

    newImage = Image.new("RGB", im.size)
    newImage.putdata(newPixels)
    return newImage


def myFilter(im):
    pixels = im.getdata()
    newPixels = []

    darkBlue = (31, 237, 41)
    red = (181, 23, 160)
    lightBlue = (27, 207, 195)
    yellow = (247, 246, 222)
# changing the intensity
    for p in pixels:
        intensity = p[0]+p[1]+p[2]

        if intensity in range(0,182):
            newPixels.append(darkBlue)
        elif intensity in range(183, 364):
            newPixels.append(red)
        elif intensity in range(365, 564):
            newPixels.append(lightBlue)
        else:
            newPixels.append(yellow)

    newImage = Image.new("RGB", im.size)
    newImage.putdata(newPixels)
    return newImage
