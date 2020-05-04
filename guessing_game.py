import random
n = random.randint(1, 99)
guess = int(input("enter a number between 1 through 99"))
while n != "guess":
    print
    if guess < n:
        print ("guess is to low")
        guess = int(input("enter a number between 1 and 99: "))
    elif guess > n:
        print("guess is too high")
        guess = int(input("enter a number between 1 and 99: "))
    else:
        print("you guessed it right GREAT JOB")
        break
    print        
#-----------------------------------------------------------------
# Jordans below
def guessing_game():                  
    while True:                       
        print('What is your guess?')  
        guess = input()              
        
        if guess == '42':            
            print('You correctly guessed it')  
            return False                       
        else:
            print(f'No, {guess} is not the anwer try again\n')   
guessing_game() 