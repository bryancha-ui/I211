import re

file=open("message.txt", "r")
text=file.read()

text= re.sub('\s+@\s',"redacted",text)
text= re.sub('^\(\d{3}\)\s\d{3}-\d{4}',"redacted",text)
text= re.sub('[A-Z][a-zA-Z]*',"redacted",text)

print(text)
