from poker import *

def main():
    deck = Queue()
    
    for suit in SUITS:
        for rank in RANKS:
            deck.enqueue(Card(rank, suit))
    
    deck.shuffle()
    print(deck)
    print(deck.length())

if __name__ == "__main__": main()