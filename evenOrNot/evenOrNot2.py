def isEven(num):
    if num % 2 == 0:
        return True
    if num % 2 != 0:
        return False



# --- Put your main program below! ---
def main():
    while True:
        answer = int(input("Give me a number "))
        response = isEven(answer)
        print(response)


# DON'T TOUCH! Setup code that runs your main() function.

if __name__ == "__main__":
    main()
