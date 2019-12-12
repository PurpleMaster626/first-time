import random
import string


adjectives = ["sleepy", "slow", "smelly",
              "wet", "fat", "red",
              "orange", "yellow", "green",
              "blue", "purple", "fluffy",
              "white", "proud", "brave"]
              
              
nouns = ["apple", "dinosaur", "ball",
         "toster", "goat", "dragon",              
         "hammer", "duck", "panda"]  


print("Welcome to Password Picker!")


while True:
    adjective = random.choice(adjective)
    nouns = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.puncuation)
    
    
    password = adjective + noun + str(number) + special_char
    print("Your new password is: %s' % password)
    
    
    
    response = input("Would you like another password? Type y or n: ")
    if response == "n":
       break
