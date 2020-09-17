depricated = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',}

import random

file = open('dictionary.txt','r')
dictionary = file.readlines()

rnd = random.randint(0,len(dictionary)-1)

theWord = dictionary[rnd]
theWord=theWord[:-1]


turns=1
progress = ['-']
correct = 0
i=1
while i<len(theWord):
    i+=1
    progress.append('-')

guesses= set([])

print("Wellcome to Hanging with Keeda!\n")

while (theWord!=(''.join(progress)))and(turns<=10):
#    os.system("CLS")
    guess = input("Tries left: "+ str(11-turns) +"\n\nGuess a letter: ")
    if guess in guesses:
        print("You have already guesssed '"+guess+"'!")
    else:
        guesses.add(guess)

        if guess in theWord :
            correct = correct+1
            i =0
            while i< len(theWord):
                if theWord[i]==guess:
                    progress[i]=guess
                i=i+1
        else:
            turns = turns + 1
    for element in progress:
        print(element,end="")

    print("")

    print("Letters Guessed: ",end='')
    for element in guesses:
        print(element,end='')


    print("\n..............................................")

if theWord == (''.join(progress)):
    print("Congratulations! you won with "+str(turns-1)+" wrong letter(s)")
else:
    print("The word was: " + theWord)
    print("Game Over, Better luck next time!")

