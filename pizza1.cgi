#! /usr/bin/env python3

print('Content-type: text/html\n')

import cgi

html = """


<!doctype html>
<html>
<head><meta charset="utf-8"><link rel="stylesheet" href="http://cgi.soic.indiana.edu/~dpierz/i211.css">
<title>PizzaNet Order [2]</title></head>
    <body>
	What do you want on your {ch_size} pizza with {ch_crust}-style crust?
	Each topping costs $2 to add.
<p>
<form method="post" action="pizza2.cgi">
<p><input type="checkbox" name="toppings" value="pepperoni"> pepperoni</p>
<p><input type="checkbox" name="toppings" value="mushroom"> mushroom</p>
<p><input type="checkbox" name="toppings" value="onion"> onion</p>
<p><input type="checkbox" name="toppings" value="bell pepper"> bell pepper</p>
<p><input type="checkbox" name="toppings" value="extra cheese"> extra cheese</p>
<p>Enter discount code here: <input type="text" name="discount"></p>
<input type="hidden" name='size' value={ch_size}>
<input type="hidden" name='crust' value={ch_crust}>

	<button type="submit">Next</button>
</form></p>
    </body>
</html> """

form=cgi.FieldStorage()
size=form.getfirst('size', 'enter size')
crust=form.getfirst('crust', 'please select crust')

print(html.format(ch_size=size, ch_crust=crust))
