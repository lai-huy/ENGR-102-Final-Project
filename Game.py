# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: HUY Q LAI       132000359
#       BRANDON A WHITE 331004571
# Section:      ENGR-102-569
# Assignment:   Game
# Date:         07 December 2021

import tkinter as tk

import LCR
import Simon
import War

FONT = ("Times New Roman", 12)


def main() -> None:
    """
    Display the main menu

    :return: None
    """
    window = tk.Tk()
    window.title("Game")

    frame = tk.Frame(window)
    frame.pack()

    war_button = tk.Button(frame, text="War", font=FONT, command=War.war, width=30, height=5)
    war_button.pack()

    simon_button = tk.Button(frame, text="Simon Says", font=FONT, command=Simon.simon, width=30, height=5)
    simon_button.pack()

    lcr_button = tk.Button(frame, text="LCR", font=FONT, command=LCR.lcr, width=30, height=5)
    lcr_button.pack()

    quit_button = tk.Button(frame, text="Quit", font=FONT, command=window.destroy, width=30, height=5)
    quit_button.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
