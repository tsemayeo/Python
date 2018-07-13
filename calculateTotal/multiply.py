def calc(list):
    blah = 1
    for number in range(len(list)):
      blah *= (list[number])
    return blah

# --- Put your main program below! ---
def main():
        listOne = [3, 4, 10, 6]
        sum = calc(listOne)
        print(sum)



# DON'T TOUCH! Setup code that runs your main() function.

if __name__ == "__main__":
    main()
