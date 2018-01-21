#get a picture from a website, namely the GOES EAST CONUS views
#save the pictures
#set picture as the background

#helper websites
#http://www.pythonforbeginners.com/requests/using-requests-in-python
#https://packaging.python.org/tutorials/installing-packages/
#http://docs.python-requests.org/en/latest/user/install/
#https://www.geeksforgeeks.org/downloading-files-web-using-python/
import requests
import ctypes

#https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/
#there is a latest.jpg that is good enough, could consider reading the json file and scrapping for different images
url = 'https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/latest.jpg'
r = requests.get(url, allow_redirects=True)
open('goes_east.jpg ', 'wb').write(r.content)


#update the desktop background
#https://stackoverflow.com/questions/40941167/changing-desktop-background-in-windows-10-via-python
directory = "C:\Users\joshua.buck\Documents\GitHub\POTD\POTD\POTD"
imagePath = directory + "\goes_east.jpg"

def changeBG(imagePath):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imagePath , 3)
    return;

changeBG(imagePath)
