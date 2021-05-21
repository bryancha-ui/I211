import re
import urllib.request

url=input("Please enter a movie link: ")
char_rep=input("Please enter a character to replace: ")
per_rep=input("Please enter a person to replace: ")
web_page= urllib.request.urlopen(url)
contents= web_page.read().decode(errors="replace")
contents=re.findall('(?<=/span></h2>).+(?=<h2><span class="mw-headline" id="Cast")',contents, re.DOTALL)

web_page.close()

contents= re.sub(char_rep,per_rep,'{}'.format(contents))

print(contents)
                 
