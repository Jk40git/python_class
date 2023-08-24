




def guess_game():
    
    attempts = 0 
    score =20
   
    while attempts < score:
        import random

        randomNumber= random.randint(1,20)
        guessedNumber = int(input("Guess the number between 1 and 20: "))
        print("guessedNumber:",guessedNumber)
        print("randomNumber:",randomNumber)
        
        attempts += 1
        x= score-attempts
        
        if guessedNumber == randomNumber:
            print(f"Congratulations,you guessed the number in the {x} attempts left!")
            break
        elif guessedNumber > randomNumber:
            print(f'''Too High! Try again! you have {x} attempts left''') 
        elif guessedNumber < randomNumber:
            print(f'''Too low! Try again! You have {x} attempts left''') 
        
    else: 
        print("Sorry, you lost")

guess_game()

