
#imports the ability to get a random number (we will learn more about this later!)

from random import *
#Create the list of words you want to choose from.

burgersList = ["Texas Luau", "Lockhart Legend","Mac n Cheese", "Good Ole Cheese", "Chipotle", "Bacon Daddy"]
shakesList = ["Banana Split", "Cookies n Cream", "Hazelnut Spread","Double Fudge", "Vanilla", "Cotton Candy"]
friesList = ["Curly", "Skinny", "Salt n Vinegar", "Sour Cream n Onion", "Regular", "Sweet Potatoe","Cheesy"]
#Generates a random integer.
burgersIndex = randint(0, len(burgersList)-1)
shakesIndex = randint(0, len(shakesList)-1)
friesIndex = randint(0, len(friesList)-1)

print("Burger: " + burgersList[burgersIndex])
print("Shake: " + shakesList[shakesIndex])
print("Fries: "+ friesList[friesIndex])
