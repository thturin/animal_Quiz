"""Project No. 1 - Animal Quiz"""
"""Upgrades 
make it multiple choice 

better score for fewer attempts

make a true or false quiz 

change the difficulty - make less attempts 

choose another topic

"""

#build a function
def check_guess(guess,answer): #Q why do we have to write the function before calling it?
    global score #ensures that changes to the variable score can be seen throughout the program (not only in this function)
    still_guessing = True
    attempt =  0
    while still_guessing and attempt < 2: #two attempts only
        if guess.lower() == answer.lower(): #ignore case
            print('Correct answer')
            score += 3 - attempt # this will subtract how many attempts the user needed
            still_guessing = False
        else:
           if attempt<1:
               guess = input('Sorry wrong answer. Try again: ')

           attempt += 1

    if attempt == 2:
        print('The correct answer is '+ answer)
    print("Total Score: "+ str(score))
score = 0
print('Guess the Animal')
guess1 = input('Which is the tallest animal in the world? \n A) Gorilla \n B) Ostrich \n '
               'C) Giraffe \n D) Charizard \n Enter A B C or D: ')
check_guess(guess1,'C')

guess2 = input('Which animal has the longest lifeline?')
check_guess(guess2,'arctic whale')

guess3 = input('What is a group of lions called?')
check_guess(guess3,'pride')

print('Total Score: '+ str(score))