# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: HUY Q LAI       132000359
#       BRANDON A WHITE 331004571
# Section:      ENGR-102-569
# Assignment:   War
# Date:         07 December 2021

from colorama import Fore, Style
import random as rand
import tkinter as tk


class Card:
    """
    Represents a Card
    """

    SPADE: str = Fore.BLACK + Style.BRIGHT + chr(0x2660) + Fore.RESET + Style.NORMAL
    """The Spade Suit"""

    DIAMOND: str = Fore.RED + Style.BRIGHT + chr(0x2663) + Fore.RESET + Style.NORMAL
    """The Diamond Suit"""

    CLUBS: str = Fore.BLACK + Style.BRIGHT + chr(0x2666) + Fore.RESET + Style.NORMAL
    """The Club Suit"""

    HEART: str = Fore.RED + Style.BRIGHT + chr(0x2665) + Fore.RESET + Style.NORMAL
    """The Heart Suit"""

    def __init__(self, suit: str, value: int):
        """
        Creates a Card class with a given suit and value

        :param suit: str holding the suit of the card. One of four different values
        :param value: int holding the value of the card. Can be between 1 and 13 inclusive
        """

        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        """
        Converts Card to a string

        :return: String representation of this Card
        """

        value_str = str(self.value)

        if self.value == 1:
            value_str = "Ace"
        elif self.value == 11:
            value_str = "Jack"
        elif self.value == 12:
            value_str = "Queen"
        elif self.value == 13:
            value_str = "King"

        return f"{value_str} {self.suit}"

    def __gt__(self, other) -> bool:
        if self.value == 1:
            return True
        return self.value > other.value

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __lt__(self, other) -> bool:
        if self.value == 1:
            return False
        return self.value < other.value

    def __le__(self, other) -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other) -> bool:
        return self.__gt__(other) or self.__eq__(other)


class Player:
    """
    A Player class
    """

    def __init__(self, id: int):
        """
        Creates a player with an empty hand
        """

        self.hand: list[Card] = []
        self.id: int = id

    def add_cards(self, cards: list[Card]) -> bool:
        """
        Adds a list of cards to the player's hand

        :param cards: list of cards to add
        :return: True
        """
        self.hand.extend(cards)

    def add_card(self, card: Card) -> bool:
        """
        Adds a single card to the end of the players hand
        :param card:
        :return:
        """

        self.hand.append(card)
        return True

    def deal_card(self) -> Card:
        """
        Removes the first card from the player's hand

        :return: the first card
        """
        return self.hand.pop(0)

    def is_out(self) -> bool:
        """
        Determines if a player had cards in their hand

        :return: True when out, False otherwise
        """
        return len(self.hand) == 0


SUITS = [Card.SPADE, Card.DIAMOND, Card.CLUBS, Card.HEART]
VALUE = range(1, 14)
FONT = ("Times New Roman", 12)
RULES = ("All players play the top card from their respective hands.",
         "Highest value card wins.",
         "The player that played this card will add all cards played to the end of their deck.",
         "If there a tie, the players that played the tie card will play their next card.",
         "This card will determine who will win.",
         "This tie breaking process repeats until a player runs out of cards or the tie is broken.",
         "The winner of the tie break will get all cards that were played up until the tie was broken.",
         "The game will automatically end after 10000 rounds.",
         "If the game ends in this manner, whoever has the most cards will win.")


def create_deck() -> list[Card]:
    """
    Creates a list of shuffled Cards

    :return: shuffled list of cards
    """

    deck = []

    for v in VALUE:
        for s in SUITS:
            deck.append(Card(s, v))

    rand.shuffle(deck)
    return deck


def war() -> None:
    """
    Plays War

    :return: None
    """

    window = tk.Tk()
    window.title("War")

    frame = tk.Frame(window)
    frame.pack()

    title_label = tk.Label(frame, text="Welcome to War!", font=FONT)
    title_label.pack()

    question_label = tk.Label(frame, text="Enter in a number of players", font=FONT)
    question_label.pack()

    num_player_entry = tk.Entry(frame, width=40)
    num_player_entry.focus_set()
    num_player_entry.pack()

    start_button = tk.Button(frame, text="Okay", font=FONT, command=(lambda n=num_player_entry: start(n)))
    start_button.pack()

    rules_button = tk.Button(frame, text="Rules", font=FONT, command=rules)
    rules_button.pack()

    quit_button = tk.Button(frame, text="Quit", font=FONT, command=window.destroy)
    quit_button.pack()

    window.mainloop()


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


def deal_cards(deck: list[Card], players: list[Player]) -> None:
    """
    Give all players cards from the deck.

    :param deck: list of all cards
    :param players: list of all players
    :return: None
    """

    while len(deck) > 0:
        for i in range(len(players)):
            try:
                card = deck.pop()
            except IndexError as ie:
                break
            players[i].add_card(card)


def is_tie(field: list[Card], max_card: Card) -> bool:
    """
    Determine if there is a tie to break

    :return: True if a tie needs to be broken; False otherwise
    """

    count = 0
    for card in field:
        if card.value == max_card.value:
            count += 1

    return count > 1


def determine_winner(field: list[Card]):
    """
    Determine Winner for the round.

    :return: the index of the player that wins and the card it played
    """

    max_card = Card(Card.CLUBS, 0)
    index = -1

    for i in range(len(field)):
        if field[i] > max_card:
            max_card = field[i]
            index = i

    return index, max_card


def end_game(field: list, round_num: int) -> bool:
    """
    Determine if the game needs to end

    :param field: a list of played cards
    :param round_num: the round number
    :return: True if the game needs to end; False otherwise
    """

    if len(field) == 1:
        print("End of Game")
        return True

    if round_num >= 10000:
        print("Game is too long")
        return True

    return False


def play_cards(players: list[Player]) -> list[Card]:
    """
    For each player, play a single card

    :return: list[Card] of cards played
    """

    temp_field = []

    for i in range(len(players)):
        player = players[i]
        print()
        if player.is_out():
            print(f"Player {player.id} is out of cards")
        else:
            card = player.deal_card()
            temp_field.append(card)
            print(f"Player {player.id} plays {card}")

    print()
    return temp_field


def start(entry: tk.Entry) -> None:
    """
    Starts the game

    :param entry: an entry holding the number of players
    :return: None
    """

    # Game Data
    deck = create_deck()
    n_play = int(entry.get())

    # Ensure that there is at least one player
    if not n_play:
        print("There are Zero Players!")
        print("Please enter a number greater than 0")
        return

    players = [None] * n_play

    # Create Players
    for i in range(len(players)):
        players[i] = Player(i)

    deal_cards(deck, players)

    # Main Game
    round_num = 0

    while True:
        round_num += 1
        print(f"Round {round_num}")

        field = play_cards(players)

        if end_game(field, round_num):
            break

        # Determine Winner
        index, max_card = determine_winner(field)

        # Tie Breaker loop
        player_tie = []
        tie_field = field
        max_card_tie = max_card

        while is_tie(tie_field, max_card_tie):
            print("THERE IS A TIE")
            player_tie.clear()

            for i in range(len(field)):
                if field[i].value == max_card.value:
                    player_tie.append(players[i])

            tie_field = play_cards(player_tie)
            max_player_tie, max_card_tie = determine_winner(tie_field)
            field.extend(tie_field)

        # Award Winner cards
        if len(player_tie):
            index = player_tie[max_player_tie].id

        players[index].add_cards(field)
        print(f"Player {index} wins the round\n")
        field.clear()

    # Determine Winner
    win_len = 0
    win_player = None
    for player in players:
        if len(player.hand) > win_len:
            win_player = player
            win_len = len(player.hand)

    print(f"Player {win_player.id} wins the War!")
