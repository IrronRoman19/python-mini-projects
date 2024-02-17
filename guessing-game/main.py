import random

hidden_num = random.randint(1, 100)
hooked_num = 0
attempts = 0

while hidden_num != hooked_num:
    hooked_num = int(input("Guess the hidden number: "))
    if hooked_num == hidden_num:
        attempts += 1
        print(f"You won! The number is {hooked_num}")
        print(f"Number of attempts: {attempts}")
        print(f"Game over!")

    if hooked_num > hidden_num:
        attempts += 1
        print("Too bigger!")
        
    if hooked_num < hidden_num:
        attempts += 1
        print("Too smaller!")
        
            

            


