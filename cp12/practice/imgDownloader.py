#!/usr/bin/python
# imgDownloader - Downloads the images that match the search keyword
# from imagur

import sys, os, requests, bs4
from pathlib import Path

if len(sys.argv) < 1:
    print("Usage: imgDownloader <keyword>")
    sys.exit()

# makes sure it only unpacks the required argument
file, keyword = sys.argv

imagurRes = requests.get('https://imgur.com/search?q='+keyword)
soup = bs4.BeautifulSoup(imagurRes.text, 'html.parser')

imgElems = soup.select('.image-list-link img')

os.makedirs(keyword, exist_ok=True)
for imgTag in imgElems:
    imgName = os.path.basename(imgTag.get('src'))

    imgRes = requests.get('https://i.imgur.com/'+imgName)

    try:
        imgRes.raise_for_status()
        with open(Path(Path.cwd()/keyword/imgName), 'wb') as imgFile:
            for chunk in imgRes.iter_content(10000):
                imgFile.write(chunk)
        print('Downloaded img %s' % imgName)
    except:
        print('Image url %s is invalid' % imgRes.url)
