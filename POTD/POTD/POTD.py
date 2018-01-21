#get a picture from a website, namely the GOES EAST CONUS views
#save the pictures
#set picture as the background

#helper websites
#http://www.pythonforbeginners.com/requests/using-requests-in-python
#https://packaging.python.org/tutorials/installing-packages/
#http://docs.python-requests.org/en/latest/user/install/
#https://www.geeksforgeeks.org/downloading-files-web-using-python/
import requests

#https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/
#there is a latest.jpg that is good enough, could consider reading the json file and scrapping for different images
url = 'https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/latest.jpg'
r = requests.get(url, allow_redirects=True)
open('goes_east.jpg ', 'wb').write(r.content)

