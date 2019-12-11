def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer")
            score = score + 3 - attempt
            still_guessing = False
        else:
           if attempt < 2:
               guess = input("Sorry wrong answer. Try again. ")
           attempt = attempt + 1
           
           
    if attempt == 3:
        print("The correct answer is ' + answer)
        
        
score = 0
print("Guess the Animal!")
guess1 = input("Which bear lives in the Arctic? ")
check_guess(guess, 'Polar Bear")
guess2 = input("What is the fastest land animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("What is the the largest Mammal? ")
check_guess(guess3, "Blue Whale")
guess4 = input("Which animal has three hearts? ")
check_guess(guess4, "Octopus")
guess5 = input("Which one of these is not a fish?\n \
A) Parrot Fish\n B) Dolphin\n C) Shark\n D)Barracuda\n \
Type A, B, C, D ")
check_guess(guess, "B")
guess6 = input("What kind of Mammal can fly? ")
check_guess(guess, "Bat")


print("Your score is " + str(score))
