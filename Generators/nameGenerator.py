
#imports the ability to get a random number (we will learn more about this later!)

from random import *
#Create the list of words you want to choose from.

namesList = ["Mulan", "Tiana", "Ariel", "Cindrella", "Ana", "Moanna","Elena", "Snow White", "Elsa", "Rapunzel", "Merida"]
#Generates a random integer.
namesIndex = randint(0, len(namesList)-1)

print(namesList[namesIndex])
