import random
from Player import Player  # Import your new base Player class

class DocilePlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def play_card(self):
        if not self.hand:
            self.active = False
            return
        # Play skull first if it exists, else flowers
        skulls = [c for c in self.hand if c.kind == "skull"]
        flowers = [c for c in self.hand if c.kind == "flower"]

        card = skulls[0] if skulls else flowers[0]
        self.hand.remove(card)
        self.pile.append(card)
    
    def time_to_bid(self):
        # Docile: prefers to place cards, rarely bids early.
        # 80% chance to place, 20% to bid — only if they’ve placed at least 2 cards.
        #We KNOW that they'll place skull first
        if len(self.pile) >= 2 and random.random() < 0.2:
            return "bid"
        return "place"


    def choose_bid(self, current_bid, max_possible):
        # Never bid more than pile_size - 1
        max_bid = max(0, len(self.pile) - 1)
        if current_bid >= max_bid:
            return None
        return current_bid + 1  # simple safe increment

    def reveal_cards(self, game, to_reveal, revealed):
        # Reveal own pile first, then other players randomly
        while self.pile and len(revealed) < to_reveal:
            card = self.pile.pop()
            revealed.append((self, card))
            print(f"{self.name} reveals their own {card.kind}")
            if card.kind == "skull":
                return False
        # then reveal other players randomly like RandomPlayer
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
