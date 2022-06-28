#!/usr/bin/env python

from itertools import count
from operator import length_hint
import random
import time

def main():
    print("\nIt is Hangman time!\n")
    name = input ("Enter your name: ")
    print("Hello, " + name + "! May the Forth be with you.")
    time.sleep(2)
    print("You need to save yourself.\n Run!")
    time.sleep(3)

    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    flowers = ["rose", "jasmine", "orchid", "carnation", "daisy", "sunflower", "camellia", "crysanthemum", "dandelion", "lavender", "hibiscus"]

    word = random.choice(flowers)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("Do you want another chance? Type Y for Yes and N for No. So?")
    while play_game not in ["Y", "N"]:
        play_game = input("Do you another chance? Type Y for Yes and N for No. So?")
        if plat_game == "Y":
            main()
        elif play_game == "N":
            print("It was good while it lasted.")
            exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("Save yourself, guess the word: " + display + "Enter your guess: \n")
   
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >=2 or guess <="9":
        print("Ops, try again.\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try another letter.\n")
        count += 1

        if count == 1:
            time.sleep(1)
            print("   ______ \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess." + str(limit - count) + "guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   ______ \n"
                  "  |      | \n"
                  "  |      |\n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess." + str(limit - count) + "guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   ______ \n"
                  "  |      | \n"
                  "  |      |\n"
                  "  |      | \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + "guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   ______ \n"
                  "  |      | \n"
                  "  |      |\n"
                  "  |      | \n"
                  "  |      o \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + "guesses remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   ______ \n"
                  "  |      | \n"
                  "  |      |\n"
                  "  |      | \n"
                  "  |      o  \n"
                  "  |     /|\ \n"
                  "  |     / \ \n"
                  "__|__\n")
            print("Say your prayers. You are hanged!\n")
            print("The word was:", already_guessed, word)
            play_loop()

        if word == '_' * length:
            print("Aye aye, captain! You have guessed the correct word!")
            play_loop()

        elif count != limit:
            hangman()

main()

hangman()