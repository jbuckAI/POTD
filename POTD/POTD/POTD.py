#update the desktop background
#https://stackoverflow.com/questions/40941167/changing-desktop-background-in-windows-10-via-python

import ctypes

directory = "C:\Users\joshua.buck\Documents\GitHub\POTD\POTD\POTD"
imagePath = directory + "\goes_east.jpg"

def changeBG(imagePath):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imagePath , 3)
    return;

changeBG(imagePath)
