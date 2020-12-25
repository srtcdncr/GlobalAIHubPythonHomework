import random

print("""
-----------------------------------------------
        Welcome to the Hangman Game
-----------------------------------------------
""")

kelimeler = ["MERCURY", "VENUS","EARTH", "MARS", "JUPITER", "SATURN", "URANUS", "NEPTUNE"]

def fully_encrypted_word(word):
    return len(word) * " _ "

def encrypted_word(allowed_letters:list, word):
    return "".join([x if x in allowed_letters else "_" for x in word])

kelime = kelimeler[random.randint(0, 7)]
max_tahmin_hakki = int(len(kelime)/2)
print(f"You have {max_tahmin_hakki} attempts. Guess the word. The words are planet names.")

print(f"The word {fully_encrypted_word(kelime)}", kelime)

tahmin_hakki = 0
tahminler = []
while(1):
    if tahmin_hakki<max_tahmin_hakki:
        print("\nType a letter or whole word: ", end=" ")
        tahmin = str(input()).upper()
        if len(tahmin) > 1:
            if tahmin == kelime:
                print(f"CONGRATULATIONS! THE WORD WAS {kelime}.")
                break
            else:
                if tahmin_hakki<max_tahmin_hakki:
                    print(f"Wrong answer. Try again.")
                    tahmin_hakki += 1
                    continue
                else:
                    print(f"\nYOU DID ALL ATTEMPTS. THE WORD WAS {kelime}. GAME OVER")
                    break
        tahminler.append(tahmin)
        print(encrypted_word(tahminler, kelime))
        tahmin_hakki += 1
    else:
        print(f"\nYOU DID ALL ATTEMPTS. THE NUMBER WAS {kelime}. GAME OVER")
        break