#! /usr/bin/env python3

print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()   

html = """<!doctype html>

<html>

<head><meta charset="utf-8">

<link rel="stylesheet" href="https://cgi.sice.indiana.edu/~dpierz/i211.css">

<title>Form in CGI</title></head>

<body>

  <h1>Greetings!</h1>

  <p>{content}</p>

</body>

</html>"""

user = form.getfirst('username','Who are you?')

print(html.format(content = 'Hello,' + user))
