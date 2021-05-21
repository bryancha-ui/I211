#!/usr/bin/env python3

print('Content-type: text/html\n')

file=open("top100moviesAFI.txt","r")
afi=file.readlines()
file.close()

file=open("top100moviesRT.txt","r")
rt=file.readlines()
file.close()

html="""<!doctype html>
 <html>
 <head>
 <meta charset="utf-8">
 <title>Top Movie Comparison</title>
 </head>
 <body>
   <h1>Top 100 Film Comparisons</h1>
 <table border=1><tr><td>Movie</td><td>AFI Rank</td></tr>{content{</table>
 </body>
 </html>"""

table=""

for movie in sorted(set(afi) | set(rt)):
    if movie in afi:
        afiRank = afi.index(movie)
    else:
        afiRank = "--"
    if movie in rt:
        rtRank = rt.index(movie)
    else:
        rtRank = "--"
    table += "<tr><td>"+movie+"</td><td>"+str(afiRank)+"</td><td>"+str(rtRank)+"</td></tr>"


print(html.format(content=table))


