from Card import Card
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.default_hand = [Card("flower") for _ in range(3)] + [Card("skull")]
        self.hand = self.default_hand.copy()
        self.pile = []
        self.discard = []
        self.score = 0
        self.active = True

    def play_card(self):
        """Override in child classes"""
        raise NotImplementedError
    
    def time_to_bid(self):
       raise NotImplementedError

    def choose_bid(self, current_bid, max_possible):
        """Override in child classes"""
        raise NotImplementedError

    def reveal_cards(self, game, to_reveal, revealed):
        """Override in child classes"""
        raise NotImplementedError

    def lose_random_card(self):
        if not self.default_hand:
            self.active = False
            return
        lost = random.choice(self.default_hand)
        self.discard.append(lost.kind)
        self.default_hand.remove(lost)
        print(f"{self.name} loses a card ({lost.kind})!")
        print(f"{self.name}'s discard ({self.discard})")
        if len(self.discard) >= 4:
            self.active = False
            print(f"{self.name} has been eliminated!")
