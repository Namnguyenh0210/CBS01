

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for suit in ['heart', 'diamond', 'club','spade'] for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
        self.shuffle()

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal_a_card(self):
        return self.cards.pop() # lay ra 1 la bai cuoi cung va xoa di

    def sort(self):
        self.cards.sort(key=lambda card: (card.suit, card.value))  # xep theo chieu tang theo chieu thu tu chats, giua chats, gia tri lá bai

    def __str__(self):
        return '\n'.join(str(card) for card in self.cards)

if __name__ == '__main__':
    while True:
        deck = Deck()
        print("Deck of cards:")
        print(deck)
        print("Shuffled deck:")
        deck.shuffle()
        print(deck)
        print("Dealt card:")
        print(deck.deal_a_card())
        print("Sorted deck:")
        deck.sort()
        print(deck)
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower()!= 'yes':
            break









