from Player import Player
import random

class PacifistPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def play_card(self):
        if not self.hand:
            self.active = False
            return
        # Always flowers first
        flowers = [c for c in self.hand if c.kind == "flower"]
        skulls = [c for c in self.hand if c.kind == "skull"]

        card = skulls[0] if skulls else flowers[0]
        self.hand.remove(card)
        self.pile.append(card)

    def time_to_bid(self):
        # Pacifist: avoids bidding, plays peacefully.
        if len(self.pile) >= 3 and random.random() < 0.1:
            return "bid"
        return "place"

    def choose_bid(self, current_bid, max_possible):
        max_bid = max(0, len(self.pile) - 1)
        if current_bid >= max_bid:
            return None
        return current_bid + 1

    def reveal_cards(self, game, to_reveal, revealed):
        # Reveal flowers first, then others
        while self.pile and len(revealed) < to_reveal:
            card = self.pile.pop()
            revealed.append((self, card))
            print(f"{self.name} reveals their own {card.kind}")
            if card.kind == "skull":
                return False
        others = [p for p in game.players if p != self and p.active and p.pile]
        while len(revealed) < to_reveal and others:
            target = random.choice(others)
            card = target.pile.pop()
            revealed.append((target, card))
            print(f"{self.name} reveals {target.name}'s {card.kind}")
            if card.kind == "skull":
                return False
            if not target.pile:
                others.remove(target)
        return True, revealed
