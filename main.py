# Build a desktop app that assesses your typing speed.
# Give the user some sample text and detect how many words they can type per minute.

# Tkinter window
from tkinter import *
import tkinter as tk
from countdown import CountDown


# Create Tkinter Window
window = Tk()
window.title("Typing Speed Test")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)
window.config(background="Light Blue")

# Create Class Instance from countdown
timer = CountDown(window)

# Window with sample text user has to type
sample_txt = open("sample.txt", "r", encoding="utf-8")
sample_test_txt = Text(window, height=10, width=60)
sample_test_txt.pack(padx=30, pady=30)
sample_test_txt.insert(tk.END, sample_txt.read())


# Function to get user text typed
def retrieve_input():
    # Get the text and calculate the number of words
    inputValue=user_text.get("1.0", END)
    number_of_words = len(inputValue.split())

    if number_of_words > 0:
        timer.calculated_time(number_of_words)


# Function to delete text in the User Text box and restart timer
def delete_text():
    # Unbind the keypress event temporarily
    user_text.unbind("<KeyPress>")
    user_text.delete("1.0", END)
    timer.restart_typing()

# Label to explain how to test typing speed
label = Label(window, text="Type the text above to test typing speed below")
label.pack(padx=20, pady=20)

# User Text box to enter text
user_text = Text(window, height=10, width=60)
user_text.pack(padx=10, pady=10)
# event parameter in the handle_keypress function == <KeyPress> starts timer when a key is pressed
user_text.bind("<KeyPress>", timer.handle_keypress)

# Calculation Label
calculation_label = Label(window, text="Number of word per min")
calculation_label.place(x=170, y=520)

# Button to click when finished typing
stop_button = Button()
stop_button = Button(text="Stop Timer", command=retrieve_input)
stop_button.place(x=170, y=480)

#Restart Button
restart_button = Button()
restart_button = Button(text="Restart Timer", command=delete_text)
restart_button.place(x=288, y=480)

#Keep Tkinter window open until user clicks exit
window.mainloop()
