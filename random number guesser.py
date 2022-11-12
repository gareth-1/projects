#menu interface
print("============================================================")
print("guessing game")
print("can you guess the secret number?")
print("select a number between 1 to 10")
print("see how many tries it takes you to guess it")
print("============================================================")



#initialise 
secret = 0 
count = 0

#import random num generator 
import random 
#random number generation
secret = random.randint(1,10)
 
#user input
temp = True
while temp : 
    guess = int(input("guess a random number between 1-10 : "))
    #correct guess 
    if guess == secret : 
        count += 1 
        print(f"congrats you have guess the correct number in {count} times ")
        temp = False
    elif guess < secret :
        count += 1 
        print("your guess is too low try higher")
    elif guess > secret :
        count += 1 
        print("your guess is too high try lower")
    


