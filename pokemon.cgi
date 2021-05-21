#! /usr/bin/env python3

print('Content-type: text/html\n')

import cgi, random


html = """
<!doctype html>
<html><head><meta charset="utf-8">
<title>Form in CGI </title></head>

…

<p>You chose: {user} </p>

<img src="{img1}" height="300">

<p>Computer chose: {computer} </p>

<img src="{img2}" height="300">

<h2>{result}</h2>

…

"""

form=cgi.FieldStorage()
pokemon= form.getfirst('pokemon', 'water')

pokemon_list= ['Fire', 'Water', 'Grass']

comp_choice= random.choice(pokemon_list)

if pokemon == "Fire":
    image1= "fire.png"
elif pokemon == "Water":
    image1= "water.png"
else:
    image1="grass.png"

if comp_choice == "Fire":
    image2= "fire.png"
elif comp_choice == "Water":
    image2= "water.png"
else:
    image2="grass.png"

if pokemon == 'Fire' and comp_choice == 'Grass':
    result= 'Congratulations! Your pokemon Won!'
elif pokemon == 'Fire' and comp_choice == 'Water':
    result= 'Sorry. Your Pokemon Lost.'
elif pokemon == 'Water' and comp_choice == 'Fire':
    result= 'Congratulations! Your pokemon Won!'
elif pokemon == 'Water' and comp_choice == 'Grass':
    result= 'Sorry. Your Pokemon Lost.'
elif pokemon == 'Grass' and comp_choice == 'Water':
    result= 'Congratulations! Your pokemon Won!'
elif pokemon == 'Grass' and comp_choice == 'Fire':
    result= 'Sorry. Your Pokemon Lost.'
else:
    result= 'It was a Tie.'
    

print(html.format(img1 = image1, img2 = image2, result = result, computer= comp_choice, user= pokemon))
