import time
from tkinter import *

# Class to Perform Typing Speed functionality for tkinter window
class CountDown:

    def __init__(self, window):
        self.window = window
        # Set as False to indicate timer isn't running
        self.timer_running = False
        self.times = 0

        # Create Entry Widgets for HH MM SS
        self.sec = StringVar()
        Entry(self.window, textvariable=self.sec, width=2, font='Helvetica 12').place(x=290, y=0)
        self.sec.set('00')

        self.mins = StringVar()
        Entry(self.window, textvariable=self.mins, width=2, font='Helvetica 12').place(x=250, y=0)
        self.mins.set('02')

        self.hrs = StringVar()
        Entry(self.window, textvariable=self.hrs, width=2, font='Helvetica 12').place(x=210, y=0)
        self.hrs.set('00')

        #Create Entry Widget for calculated typing speed
        self.words_per_min = StringVar()
        Entry(self.window, textvariable=self.words_per_min, width=5, font='Helvetica 12').place(x=320, y=520)
        self.words_per_min.set('00')


    #Function to montior when a key has been pressed to indicate typing has started
    def handle_keypress(self, event):
        if not self.timer_running:
            self.countdowntimer()


    # Define the function for the timer to start
    def countdowntimer(self):
        self.timer_running = True

        # Timer functionality
        self.times = int(self.hrs.get()) * 3600 + int(self.mins.get()) * 60 + int(self.sec.get())

        def timer_step():
            if self.times > 0 and self.timer_running is True:
                minute, second = (self.times // 60, self.times % 60)
                hour = 0
                if minute > 60:
                    hour, minute = (minute // 60, minute % 60)
                self.sec.set(second)
                self.mins.set(minute)
                self.hrs.set(hour)
                # Update the time
                self.times -= 1
                self.window.after(1000, timer_step)

                #By using the time.sleep it makes the gui unresponsive for 1 second
                #self.window.update()
                #time.sleep(1)
            elif (self.times == 0):
                self.timer_running = False
                self.sec.set('00')
                self.mins.set('00')
                self.hrs.set('00')

        timer_step()


    # Function to caluclate words per minute
    def calculated_time(self, number_of_words):
        # Stop timer
        self.timer_running = False

        # Get the time remaining and subtract by 2 minutes
        total_time = 120
        typing_time = (total_time - self.times) / 60

        # Divide this by the time spent typing
        cal_words_per_min = number_of_words/typing_time
        self.words_per_min.set(str(round(cal_words_per_min, 2)))


    # Function to restart typing
    def restart_typing(self):
        # Reset all class attributes
        self.timer_running = False
        self.times = 0
        self.sec.set('00')
        self.mins.set('02')
        self.hrs.set('00')
        self.words_per_min.set('00')



