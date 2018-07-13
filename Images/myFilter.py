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
