# Подключение библиотек
import numpy as np
import matplotlib.pyplot as plt
import imageio
from PIL import Image
from cycler import cycler

def crop(fileName, outfileName):
    with Image.open(fileName) as image:
        image.load()
    crop = image.crop(((810, 540, 1015, 835)))
    crop.save(outfileName)

def callibration(rgb):
    mxr = 0
    mxb = 0
    mxlb = 0
    mxg = 0
    nmxr = 0
    nmxg = 0
    nmxb = 0
    nmxlb = 0
    for i in range(len(rgb) - 1):
        if rgb[i][0] > mxr:
            mxr = rgb[i][0]
            nmxr = i
        if rgb[i][1] > mxg:
            mxg = rgb[i][1]
            nmxg = i
        if rgb[i][2] > mxb:
            mxb = rgb[i][2]
            nmxb = i
        if rgb[i][2] > mxlb  and 200 < i < 250:
            mxlb = rgb[i][2]
            nmxlb = i
    return [nmxr, nmxg, nmxb, nmxlb]

def readIntensity(photoName, plotName, lamp, surface):
    im = Image.open(photoName)
    photo = imageio.v2.imread(photoName)
    background = photo.swapaxes(0, 1)
    cut = photo.swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig = plt.figure(figsize=(10, 5), dpi=200)

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')

    plt.plot(rgb[:, 0], label=('r'))
    plt.plot(rgb[:, 1], label=('g'))
    plt.plot(rgb[:, 2], label=('b'))
    plt.plot(luma, 'w', label='I')
    plt.legend()

    plt.imshow(background, origin='lower')

    plt.savefig(plotName)
    return rgb, luma

def albedo(blue, white):
    ba = []
    for i in range(len(blue)):
        if white[i] < 1:
            ba.append(0)
        else:
            ba.append(blue[i] / (white[i]))
    return ba