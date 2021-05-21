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

  <p>{content}</p>

</body>

</html>"""

num_one = eval(form.getfirst('one','1'))
num_two= eval(form.getfirst('two','2'))

math= form.getfirst('opp','add')

if math == 'add':
    total =num_one + num_two
elif math == 'subtract':
    total =num_one - num_two
elif math == 'multiply':
    total =num_one * num_two
else:
    total= num_one / num_two

print(html.format(content = 'The answer is: ' + str(total))
