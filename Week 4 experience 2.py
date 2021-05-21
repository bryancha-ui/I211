import urllib.request, urllib.parse, urllib.error
import re

url = input('searching:  ')
html = urllib.request.urlopen(url).read()
links = re.findall(b'href=\"(http://.*?)\"', html)
print("Found the following urls:")
for link in links:
    print(link.decode())
