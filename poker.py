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

    def face(a_rank):
        if a_rank == 11:
            return "Jack"
        elif a_rank == 12:
            return "Queen"
        elif a_rank == 13:
            return "King"
        elif a_rank == 14:
            return "Ace"
    
    def rank(self):
        return self.__rank

    def suit(self):
        return self.__suit

    def __str__(self):
        return self.__name

class Queue:
    __slots__ = []

# Make a deck of Cards using a List Queue 
