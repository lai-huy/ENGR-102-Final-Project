# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: HUY Q LAI       132000359
#       BRANDON A WHITE 331004571
# Section:      ENGR-102-569
# Assignment:   Simon Says
# Date:         07 December 2021

import random
import tkinter as tk

FONT = ("Times New Roman", 12)
RULES = (
    "Player inputs a difficulty that must be greater than or equal to 0.",
    "The program will output a sequence of numbers based on the difficulty.",
    "The player will input this sequence in order from memory.",
    "The program will then count how many numbers the player did not remember correctly.",
)

choice = []
wrong = []


def simon() -> None:
    """
    Runs Simon game

    :return: None
    """

    window = tk.Tk()
    window.title("Simon Says")

    frame = tk.Frame(window)
    frame.pack()

    title_label = tk.Label(frame, text="Welcome to Simon Says!", font=FONT)
    title_label.pack()

    question_label = tk.Label(frame, text="Enter a level number", font=FONT)
    question_label.pack()

    difficulty_entry = tk.Entry(frame, width=40)
    difficulty_entry.focus_set()
    difficulty_entry.pack()

    start_button = tk.Button(frame, text="Okay", font=FONT, command=(lambda n=difficulty_entry: play(n)))
    start_button.pack()

    rules_button = tk.Button(frame, text="Rules", font=FONT, command=rules)
    rules_button.pack()

    quit_button = tk.Button(frame, text="Quit", font=FONT, command=window.destroy)
    quit_button.pack()

    window.mainloop()


def rules() -> None:
    """
    Displays a window with the rules for the game
    
    :return: None
    """

    window = tk.Tk()
    window.title("Rules")
    frame = tk.Frame(window)
    frame.pack()

    text_label = tk.Label(frame, font=FONT, text="\n".join(RULES))
    text_label.pack()

    window.mainloop()


def gen_num(numbers_len: int) -> list[int]:
    """
    Generate and return a list of random integers between 0 and 9 inclusive.

    :param numbers_len: the amount of numbers to generate
    :return: the list
    """

    temp = []

    for i in range(numbers_len):
        temp.append(random.randint(0, 9))

    return temp


def ask_user(window: tk.Tk, numbers) -> None:
    """
    Displays a window to get numbers from the user.

    :param window:  Window that this method was called from
    :param numbers: the list of numbers that the user needs to remember
    :return: None
    """

    window.destroy()

    window = tk.Tk()
    window.title(f"Remember the numbers")
    window.geometry("400x300")

    frame = tk.Frame(window)
    frame.pack()

    label = tk.Label(frame, text=f"Try to remember the {len(numbers)} numbers.\n"
                                 f"Enter each number individually and hit \"Submit\" after entering the number")
    label.pack()

    entry = tk.Entry(frame)
    entry.pack()

    button = tk.Button(frame, text="Submit", command=lambda: store_num(entry, window, numbers))
    button.pack()

    window.mainloop()


def check(window: tk.Tk, numbers: list[int]):
    """
    Check the numbers the user entered against the numbers that the user needed to remember

    :param window:
    :param numbers:
    :return:
    """

    window.destroy()
    wrong.clear()

    for i in range(len(numbers)):
        if numbers[i] != choice[i]:
            wrong.append(i)

    window = tk.Tk()
    window.title("Results")
    window.geometry("400x300")

    frame = tk.Frame(window)
    frame.pack()

    label = tk.Label(frame, text=f"You got {len(wrong)} wrong.")
    label.pack()

    window.mainloop()


def store_num(entry: tk.Entry, window: tk.Tk, numbers: int) -> None:
    user = entry.get();
    if user == "e":
        window.destroy()

    choice.append(int())
    entry.text = ""

    if len(choice) == len(numbers):
        check(window, numbers)


def play(level: tk.Entry):
    """
    Plays a Simon Says game based input difficulty

    :param level: difficulty level of the game
    :return: None
    """

    choice.clear()

    numbers_len = 2 * int(level.get()) + 2
    numbers = gen_num(numbers_len)

    window = tk.Tk()
    window.title("Remember these numbers!")

    frame = tk.Frame(window)
    frame.pack()

    label = tk.Label(frame, text=str(numbers))
    label.pack()

    window.after(3000, lambda: ask_user(window, numbers))
    window.mainloop()
