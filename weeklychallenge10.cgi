#! /usr/bin/env python3

print('Content-type: text/html\n')

import cgi


html = """<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Robot Delivery System Confirmation </title>
    </head>
    <body>
          <h1>Robot Delivery System Confirmation</h1>
          <p>You chose to have a {item} delivered by a {method}. </p>
          <p>Your total comes to ${total} .</p>
    </body>
</html>"""

form=cgi.FieldStorage()

item_chose=form.getfirst('delivery', 'enter item')
cost= form.getfirst('cost', 'Please enter a numeric price.')
delivery_method=form.getfirst('delivery_method', 'select valid delivery method')

total_price = int(cost) 

if delivery_method == 'Flying Drone':
    total_price += 10
elif delivery_method == 'Self Driving Car':
    total_price += 20
elif delivery_method == 'Giant Robot':
    total_price += 1000




print(html.format(item=item_chose, method= delivery_method, total= total_price))
