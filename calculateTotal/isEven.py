def isEven(num):
    evenList = []
    for i in range(len(num)):
        if num[i] % 2 == 0:
            evenList.append(num[i])
    return evenList

# --- Put your main program below! ---
def main():
        answer = [9,10,26,28,190,27,34,45,98,67]
        response = isEven(answer)
        print(response)




# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
