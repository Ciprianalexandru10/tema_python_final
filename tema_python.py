import itertools
import random
from tkinter import *
from tkinter.ttk import *

def create_phrase():
    words_array = [["Eu","Tu"],["Joaca", "Iubire"],["Hochei","Fotbal"]]
    
    # itertools.product () computes the cartesian product of input iterables.
    # It is equivalent to nested for-loops
    for word in itertools.product(*words_array):
        print(word)

def guess_number_game():
    
    name = input("Please enter your name:\n")
    print(f'You entered {name}')

    value = input("Do you wanna play a game, YES or NO? \n")
    print(f'You select {value}')

    if (value.lower() == "yes"):
        random_number = random.randint(1,10)
        number_guessed= int(input("Enter a number from 1 to 10: "))

        game_is_on = True
        
        while game_is_on:
            if number_guessed < random_number:
                print("Number is low")
                number_guessed = int(input("Enter a number from 1 to 10: "))
            elif number_guessed > random_number:
                print("Number is to big")
                number_guessed = int(input("Enter a number from 1 to 10: "))
            else:
                print(f"Nice! You got it the number was {random_number}")
                game_is_on = False
                break

    else: 
        print("Closing the game")
        return

def show_popup():
    root = Tk()
    root.title("1 to 10 Numbers")
    root.geometry("500x500")

    # Create the text display
    text = Entry(root, width=30, background="White")
    text.pack(pady=10)

    def text_updation(number):
        text.delete(0, END)
        text.insert(0, number)
    
    button_dict = {}
    for number in range(1,11):
        
        def action(x = number): 
            return text_updation(x)
            
        # create the buttons 
        button_dict[number] = Button(root, text = number,
                                command = action)
        button_dict[number].pack(pady=10)

    root.mainloop()

def print_number(number):
    print(number)