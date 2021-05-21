#! /usr/bin/env python3

print('Content-type: text/html\n')

import cgi

html= """

<!doctype html>
<html>
<head><meta charset="utf-8"><link rel="stylesheet" href="http://cgi.soic.indiana.edu/~dpierz/i211.css">
<title>PizzaNet Order - Confirmation</title></head>
    <body>
<p>Your order:
A {size} {crust} pizza, with {toppings}.<p>Total Cost: ${total}</p></p>
    </body>
</html> """

form=cgi.FieldStorage()
toppings=form.getlist('toppings')
size=form.getfirst('size', 'enter size')
crust=form.getfirst('crust', 'please select crust')
dis_code=form.getfirst('discount', 'what is the discount code?')

if len(toppings) == 5:
    topp_str= topp_str= str(toppings[0])+', '+str(toppings[1])+', '+str(toppings[2])+', '+str(toppings[3])+', and '+str(toppings[4])
elif len(toppings) == 4:
    topp_str= str(toppings[0])+', '+str(toppings[1])+', '+str(toppings[2])+', and '+str(toppings[3])
elif len(toppings) == 3:
    topp_str= str(toppings[0])+', '+str(toppings[1])+', and '+str(toppings[2])
elif len(toppings) == 2:
    topp_str= str(toppings[0])+'and'+str(toppings[1])
elif len(toppings) == 1:
    topp_str= str(toppings[0])
else:
    topp_str= 'no toppings'
    
    

if size == 'small':
    total_cost= 8.5
elif size == 'medium':
    total_cost= 10.5
else:
    total_cost = 12.5

total_cost= ((len(toppings)*2)) + total_cost

if dis_code == 'PYTHON':
    total_cost= (total_cost) * 0.9
else:
    total_cost= total_cost

total_cost= '{:.2f}'.format(total_cost)

print(html.format(size=size, crust=crust, toppings=topp_str, total=total_cost))

