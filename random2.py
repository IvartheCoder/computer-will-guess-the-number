import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback  != "C":
        if low != high:
            guess = random.randint(low , high)
        else:
            guess = low or high
        
        feedback = input(f"is {guess} too high (H), too low (L) or correct (C)?").lower()
        
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        else:
            print(f"yay!!! the computer guessed your number {guess}")

         
computer_guess(10)                     
             