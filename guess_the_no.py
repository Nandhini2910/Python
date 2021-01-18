import random

def guess(x):

    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x} : "))
        if guess > random_number:
            print("Too high")
        elif guess < random_number:
            print("Too low")
    print(f"Hurray!! you found the {random_number} correctly!!")

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(f"is {guess} too low(L) or too high(H) or corredt(C)").lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1

    print(f'yay!! computer guessed {guess} correctly')

computer_guess(1000)