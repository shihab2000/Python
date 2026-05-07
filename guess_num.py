import random
print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to quess the number.Let's start!")

low=int(input("Enter the Lower Bound : "))
high=int(input("Enter the uppor Bound: "))
print(f"\nYou have 7 chances to quess the number between {low} and {high}.Let's start!")

num=random.randint(low,high)
ch=7
gc=0

while gc<ch:
    gc +=1
    guess=int(input("Enter your quess : "))

    if guess ==num:
        print(f"Correct! The number is {num}.You guessed it in {gc} attempts")
    elif gc>=ch and guess !=num:
        print(f"Sorry! The number was {num}.Better luck next time.")
    elif guess>num:
        print('Too high! Try a lower number.')
    elif guess<num:
        print("To low! Try a higher number.")