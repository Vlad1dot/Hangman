import random

def check(secret, word_hide, guess_letter):
    word_temp = ""
    for i in range(len(secret)):
        if guess_letter == secret[i]:
            word_temp += secret[i]
        else:
            word_temp += word_hide[i]
    return word_temp

print("H A N G M A N")
while True:
    mode = input('Type "play" to play the game, "exit" to quit:')
    if mode == "play":
        word_list = 'python', 'java', 'kotlin', 'javascript'
        secret = random.choice(word_list)
        word_hide = "-" * len(secret)
        guess_chars = []
        lives = 8


        while lives != 0 and word_hide != secret:
            print("\n" + word_hide)
            guess_letter = input("Input a letter: ")
            if len(guess_letter) != 1:
                print("You should input a single letter")
            elif guess_letter in guess_chars:
                print("You've already guessed this letter")
            elif guess_letter not in "abcdefghijklmnopqrstuvwxyz":
                print("Please enter a lowercase English letter")
            elif secret.find(guess_letter) == -1:
                print("That letter doesn't appear in the word")
                lives -= 1
                guess_chars.append(guess_letter)
            else:
                word_hide = check(secret, word_hide, guess_letter)
                guess_chars.append(guess_letter)

        if word_hide == secret:
            print("\n" + word_hide, "\nYou guessed the word!\nYou survived!")
        else:
            print("You lost!")
    elif mode == "exit":
        break
    else:
        continue
