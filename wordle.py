import pandas as pd, numpy as np
import random

def check_guess(word, guess):
  letters = list(pd.Series(list(word)).unique())
  checked_guess = list(np.zeros(len(word)))

  for i in range(len(word)):
    if word[i] == guess[i]:
      checked_guess[i] = word[i]
    elif guess[i] in letters:
      checked_guess[i] = "*"
      letters.remove(guess[i])
    else:
      checked_guess[i] = "-"

  return checked_guess

def main():
  words = pd.read_csv("sgb-words.csv", header=None)
  index = random.randint(0, len(words)+1)
  word = words.iloc[index][0]
  for i in range(6):
    guess = input("Guess: ")
    while len(guess)!=len(word):
      guess = input("Guess: ")
    checked_guess = check_guess(word, guess)
    if "".join(checked_guess)==word:
      print("Good Job, You Have Guessed the Word!")
      break
    elif i == 5:
      print(checked_guess)
      print(word)
      print("Better Luck Next Time!")
    else:
      print(checked_guess)

main()