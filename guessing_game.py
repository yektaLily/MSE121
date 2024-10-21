import numpy as np 


print("I have a number in mind, guess what it is:\n")

random_num = np.random.randint(0,100,size = 1)
guess = int(input("What's your guess? "))
    
max_guess_chances = 10 
count_of_steps = 1

while(count_of_steps <= max_guess_chances):
        if guess == random_num:
            print("Right on! You guessed in the ", i, "th try.")
            break
        elif guess < random_num:
            print("Higher")
            guess = int(input("What's your new guess? "))
            count_of_steps += 1
        else:
            print("Lower")
            guess = int(input("What's your new guess? "))
            count_of_steps += 1

if count_of_steps > max_guess_chances:    
    print("Bummer, you couldn't guess it. It was ", random_num)
