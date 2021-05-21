import re

file=open("quote.txt", "r")
text=file.read()
print("Caps: ", re.findall('[A-Z][\w]*', text), "\n")
print('End in ing', re.findall('[\w]*ing', text), "\n")
print('Two "a"s:', re.findall('[\w]*a[\w]*a[\w]*', text), "\n")
print("Clauses: ", re.findall(',[^.!?,]+,',text), "\n")
print('Number words starting with "v": ', len(re.findall('[vV][\w]*', text)), "\n")
