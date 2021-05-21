import urllib.request, re

url=input('Searching what page?: ')
print()

web_page= urllib.request.urlopen(url)

lines= web_page.read().decode(errors="replace")

web_page.close()

headings= re.findall('(?<=<div).+?(?=</div)',lines)

print('The headings in ',url)
print()

for heading in headings:
    print("\t", heading)
    
