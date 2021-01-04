from poker import *

class Game:
    __slots__ = ["__deck", "__players", "__board"]
    def __init__(self, deck: Queue, players: list):
        self.__deck = deck
        self.__players = players
        self.__board = []

    def board(self):
        return self.__board

    def start(self):
        self.__deck.shuffle()

        for _ in range(2):
            for player in self.__players:
                player.add_card(self.__deck.dequeue())

        for player in self.__players:
            if not player.is_cpu():
                print(player)

    def round(self):
        for player in self.__players:
            player.bet()


def main():
    deck = Queue()
    
    for suit in SUITS:
        for rank in RANKS:
            deck.enqueue(Card(rank, suit))

    player = Player()
    cpu_one = Player(True)
    cpu_two = Player(True)
    cpu_thr = Player(True)

    players = [player, cpu_one, cpu_two, cpu_thr]

    game = Game(deck, players)

    game.start()



if __name__ == "__main__": main()