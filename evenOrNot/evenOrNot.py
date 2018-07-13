def evenOrNot():
    number = int(input("Ask me a number "))

    if number % 2 == 0:
        print("This number is even.")
    else:
        print("This number is odd.")

#Main Code
def main():
    while True:
        evenOrNot()

# DON'T TOUCH! Setup code that runs your main() function.

if __name__ == "__main__":
    main()
