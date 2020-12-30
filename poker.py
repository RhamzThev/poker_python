import random

RED = "\033[31m"
BLACK = "\033[34m"
RESET = "\033[0m"

class Card:
    __slots__ = ["__name", "__rank", "__suit"]

    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit
        self.__name = self.make_name(rank, suit)

    def make_name(self, rank, suit):
        a_rank = rank

        if a_rank == 11:
            a_rank = "Jack"
        elif a_rank == 12:
            a_rank = "Queen"
        elif a_rank == 13:
            a_rank = "King"
        elif a_rank == 14:
            a_rank = "Ace"

        return f"{a_rank} of {suit}"

    def rank(self):
        return self.__rank

    def suit(self):
        return self.__suit

    def __repr__(self):
        return self.__name

    def __str__(self):
        if self.__rank == 10:
            a_rank = 10
        elif self.__rank > 10:
            a_rank = self.__name[0]
        else:
            a_rank = self.__rank 
        
        a_suit = self.__suit[0]

        if a_suit == "C" or a_suit == "S":
            card = BLACK + str(a_rank) + a_suit + RESET
            return card
        elif a_suit == "D" or a_suit == "H":
            card = RED + str(a_rank) + a_suit + RESET
            return card

class Queue:
    slots = ["__list"]

    def __init__(self):
        self.__list = []

    def next(self):
        try:
            if len(self.__list) > 0:
                return self.__list[-1]
            else:
                raise IndexError
        except IndexError:
            print("Can't do that. Queue is empty.")

    def enqueue(self, item):
        self.__list.append(item)

    def dequeue(self):
        try:
            if len(self.__list) > 0:
                item = self.__list.pop(0)
                return item
            else:
                raise IndexError
        except IndexError:
            print("Can't do that. Queue is empty.")

    def length(self):
        return len(self.__list)

    def shuffle(self):
        random.shuffle(self.__list)

    def __str__(self):
        string = ""
        for item in self.__list:
            string += str(item) + " "
        return string.strip()
        
RANKS = [i for i in range(2, 15)]

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

# Next step: Apply steps to make poker game happen.
