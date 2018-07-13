
# --- Define your functions below! ---
def intro():
    print("Hello. My name is Paul. Your Helping Hand")

def sayGreeting():
    print("Hola!")

def sayDefault():
    print("Coolio")

def processInput(answer):
    if answer == "hi" or answer == "hello":
        sayGreeting()
    else:
        sayDefault()

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("What will you say? ")
        processInput(answer)



# DON'T TOUCH! Setup code that runs your main() function.

if __name__ == "__main__":
    main()
