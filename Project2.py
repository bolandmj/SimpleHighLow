# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 14:26:37 2022

@author: maxwe
"""

import random

number = random.randint(1,10)
game = "N"

print("Welcome to the guessing game!")

print("Enter your first guess for a number between (1-10)")

guess = input("> ")
guess = int(guess)
attempts = 1

while(game == "N"):
    guess = int(guess)
    
    if(guess == number):        
        print("Congrats that is the correct number in "
          + str(attempts) + " attempts.")
        game = "Y"
    elif(guess < number):
        print("Your guess was lower than the random number.")
        attempts += 1
        guess = input("Enter your next guess: ")
    elif(guess > number):
        print("Your guess was higher than the random number.")
        attempts += 1
        guess = input("Enter your next guess: ")
        


