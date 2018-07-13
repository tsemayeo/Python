def isEven(num):
    if num % 2 == 0:
        return True
    if num % 2 != 0:
        return False



# --- Put your main program below! ---
def main():
    while True:
        response = input("Give me a number ")
        if response.isnumeric() == True:
            answer = int(response)
            isEven(answer)
            text = isEven(answer)
            print(text)
        else:
            print("That's not a number!")
            continue

# DON'T TOUCH! Setup code that runs your main() function.

if __name__ == "__main__":
    main()
