"""Project No. 1 - Animal Quiz"""

#build a function
def check_guess(guess,answer): #Q why do we have to write the function before calling it?
    global score #ensures that changes to the variable score can be seen throughout the program (not only in this function)
    still_guessing = True
    attempt =  0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower(): #ignore case
            print('Correct answer')
            score += 1
            still_guessing = False
        else:
           if attempt<2:
               guess = input('Sorry wrong answer. Try again: ')

           attempt += 1

    if attempt == 3:
        print('The correct answer is '+ answer)

score = 0
print('Guess the Animal')
guess1 = input('Which is the tallest animal in the world?')
check_guess(guess1,'giraffe')

guess2 = input('Which animal has the longest lifeline?')
check_guess(guess2,'arctic whale')

guess3 = input('What is a group of lions called?')
check_guess(guess3,'pride')

print('Total Score: '+ str(score))



