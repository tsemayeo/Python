def calc(list):
    blah = 0
    for number in range(len(list)):
      blah += (list[number])
    return blah

# --- Put your main program below! ---
def main():
        listOne = [42, 37, 48, 17, 2, 69]
        sum = calc(listOne)
        print(sum)



# DON'T TOUCH! Setup code that runs your main() function.

if __name__ == "__main__":
    main()
