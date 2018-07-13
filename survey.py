import json

f = open("survey.json", 'r')

stored = json.load(f)

f.close()

surveyJson = open("survey.json", 'w+')
# --- Define your functions below! ---
questions = ["What is your name? ","During what season were you born? ", "What is your favorite season? "]

length = len(questions)

answer = {}
# name = []
# season = []
# favoriteSeason = []
lists = ['name', 'season', 'favoriteSeason']

def survey():
    for i in range(length):
        response = input(questions[i])
        # lists[i].append(response)
        answer[lists[i]] = response
    json.dump(answer, f)
    json.dump(stored, f)

    endProgram()



def endProgram():
    response = input("Do you wish to take the survey again? If no type no and the survey will end. If yes type yes and the program will restart ")
    if response == "no":
        print("Survey Completed!")
        exit()
    elif response == "yes":
        survey()
    else:
        print("That's not an answer!")
        endProgram()


# --- Put your main program below! ---
def main():
        survey()



# DON'T TOUCH! Setup code that runs your main() function.

if __name__ == "__main__":
    main()

surveyJson.close()
