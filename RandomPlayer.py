import random
from Player import Player  # Import your new base Player class

class RandomPlayer(Player):
    def __init__(self, name):
        super().__init__(name)  # initializes hand, pile, discard, score, active

    def play_card(self):
        if not self.hand:
            self.active = False
            return
        card = random.choice(self.hand)
        self.hand.remove(card)
        self.pile.append(card)

    def time_to_bid(self):
        # Random decision: 70% place, 30% bid
            return random.choices(["place", "bid"], weights=[0.7, 0.3])[0]

    def choose_bid(self, current_bid, max_possible):
        # Random strategy: 50% chance to fold, 50% chance to raise by 1–2
        if random.random() < 0.5 or current_bid >= max_possible:
            return None
        return min(max_possible, current_bid + random.randint(1, 2))

    def reveal_cards(self, game, to_reveal, revealed):
        # Reveal cards from other players until a skull is found
        others = [p for p in game.players if p != self and p.active and p.pile]

        while len(revealed) < to_reveal and others:
            target = random.choice(others)
            card = target.pile.pop()
            revealed.append((target, card))
            print(f"{self.name} reveals {target.name}'s {card.kind}")

            if card.kind == "skull":
                return False  # round ends if skull is revealed

            if not target.pile:
                others.remove(target)

        return True, revealed
