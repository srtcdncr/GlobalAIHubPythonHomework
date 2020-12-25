import random

print("""
---------------------------------------------
WELCOME TO THE GAME OF GUESS THE NUMBER AHMET
---------------------------------------------
""")

print("You have 5 attempts. Guess the number which between 1 and 100. Good luck!\n\n")

sayi = random.randint(1,100)

tahmin_hakki=1

while(tahmin_hakki<6):
    print(f"{tahmin_hakki}. guess: ", end=" ")
    try:
        tahmin = int(input())
    except ValueError:
        print("Your input is invalid. Please type valid number.")
        continue

    if tahmin == sayi:
        print(f"CONGRATULATIONS! THE NUMBER WAS {sayi}.")
        break
    else:
        print("Your guess is not correct. Try again.")
        
        if sayi > tahmin:
            print("Hint -> The number greater than your guess ;)")
        elif sayi < tahmin:
            print("Hint -> The number smaller than your guess ;)")

        
        if tahmin_hakki==5:
            print(f"\nYOU DID ALL ATTEMPTS. THE NUMBER WAS {sayi}. GAME OVER")
            break
    tahmin_hakki+=1