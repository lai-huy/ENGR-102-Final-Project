# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: HUY Q LAI       132000359
#       BRANDON A WHITE 331004571
# Section:      ENGR-102-569
# Assignment:   LCR
# Date:         07 December 2021

import random as rand
import tkinter as tk

FONT = ("Times New Roman", 12)
DICE = [1, 2, 3, 'L', 'C', 'R']
RULES = (
    "The user will input the number of players.",
    "Each player starts with three chips",
    "For each player, the program will roll three dice.",
    "If one of the three dice rolls a C, the player will lose one chip.",
    "If one of the three dice rolls a R, the player will give one chip to the player on his/her right.",
    "If one of the three dice rolls an L, the player will give one chip to the player on his/her left.",
    "If the dice rolls any other number, do nothing.",
    "If the player does not have any chips do not roll the dice.",
    "A player wins by having all other players have no chips."
)


class Player:
    """
    Handles a player for the game
    """

    def __init__(self, id: int):
        self.chips = 3
        self.id = id

    def give(self):
        self.chips += 1

    def take(self) -> bool:
        if self.chips > 0:
            self.chips -= 1
            return True
        return False


def create_players(num_player: int):
    """
    Creates a list of Players
    :param num_players: the number of players.
    :return: the list of players. 
    """

    temp = [None] * num_player

    for i in range(num_player):
        temp[i] = Player(i)

    return temp


def print_round(r_num: int) -> None:
    """
    Prints the round number to the console
    :param r_num: the round number to print
    :return: None
    """

    print("-"*10)
    print(f"Round {r_num}")
    print("-"*10)
    print()


def give_chip(players: list[Player], i: int, roll: str):
    """
    Gives chips to players based off of the roll
    :param players: list of players
    :i: current round number
    :roll: the roll
    """
    print(f"Rolled {roll}")
    if roll == 'L':
        if players[i].take():
            print(f"Giving 1 chip to Player {players[i - 1].id}")
            players[i - 1].give()
        else:
            print("Out of chips")
    elif roll == 'R':
        if players[i].take():
            print(f"Giving 1 chip to Player {players[(i + 1) % len(players)].id}")
            players[(i + 1) % len(players)].give()
        else:
            print("Out of chips")
    elif roll == 'C':
        if players[i].take():
            print(f"Giving 1 chip to the Center")
        else:
            print("Out of chips")
    else:
        print(f"Do nothing")
        pass
    print()


def rules() -> None:
    """
    Display the rules for this game

    :return: None
    """

    window = tk.Tk()
    window.title("Rules")
    frame = tk.Frame(window)
    frame.pack()

    text_label = tk.Label(frame, font=FONT, text="\n".join(RULES))
    text_label.pack()

    window.mainloop()


def start(entry: tk.Entry) -> None:
    """
    Starts the game

    :param entry: an entry holding the number of players
    :return: None
    """

    n_play = int(entry.get())
    players = create_players(n_play)
    round_number = 1
    chips = []

    while True:
        print_round(round_number)

        for i in range(len(players)):
            player = players[i]
            print(f"Player {player.id} has {player.chips} chips")

            user = input("Press enter to roll, e to exit. ")
            if user == "e":
                print("Quitting...")
                return

            if player.chips <= 0:
                print(f"No chips, skipping turn")
                pass
            else:
                print()
                for roll in rand.choices(DICE, k=3):
                    give_chip(players, i, roll)
            print()

            chips.clear()
            for player in players:
                chips.append(player.chips)

            chips.sort()
            print(chips)
            if not any(chips[:-1]):
                for player in players:
                    if player.chips:
                        print(f"Player {player.id} wins with {player.chips} chips")
                        return
        round_number += 1


def lcr():
    """
    "Main" function
    """
    
    window = tk.Tk()
    window.title("LCR")

    frame = tk.Frame(window)
    frame.pack()

    title_label = tk.Label(frame, text="Welcome to LCR!", font=FONT)
    title_label.pack()

    question_label = tk.Label(frame, text="Enter in a number of players", font=FONT)
    question_label.pack()

    num_player_entry = tk.Entry(frame, width=40)
    num_player_entry.focus_set()
    num_player_entry.pack()

    start_button = tk.Button(frame, text="Okay", font=FONT, command=(lambda: start(num_player_entry)))
    start_button.pack()

    rules_button = tk.Button(frame, text="Rules", font=FONT, command=rules)
    rules_button.pack()

    quit_button = tk.Button(frame, text="Quit", font=FONT, command=window.destroy)
    quit_button.pack()

    window.mainloop()
