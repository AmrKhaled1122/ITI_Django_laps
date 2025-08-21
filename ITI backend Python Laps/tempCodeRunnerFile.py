import random
words=["apple","orange","banana","watermelon"]
name=input(f"enter your name: ")
print(f"welcom {name} ready for play hangman game!")
word=random.choice(words)
guesses=''
turns=7
while turns>0:
    guess=input(f"you have {turns} turns guess any alphabet: ").lower()
    guesses += guess
    missed=0
    for char in word:
        if char in guesses:
            print(f"{char} ",end="")
        else:
            print("_ ",end="")
            missed+=1
    if missed == 0:
        print("congratulations you guessed the word")
        break
    if guess not in word:
            turns -= 1
            print("Wrong guess.")
            print(f"You have {turns} turns left.")

            if turns == 0:
                print(f"Game Over. The word was: {word}")
                break