#! python3
# searchpypi.py  - Opens several search results.

import requests, sys, webbrowser, bs4

print('Searching...')    # display text while downloading the search result page
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')

# Open a browser tab for each result.
numOpen = min(5, len(linkElems))
for link in linkElems[:numOpen]:
    urlToOpen = 'https://pypi.org' + link.get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)