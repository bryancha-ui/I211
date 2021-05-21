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


num_one = form.getfirst('one','please enter a number')

num_two= form.getfirst('two', 'please enter a number')

added_num= num_one + num_two




print(html.format(content = 'The total is: ' + added_num))
