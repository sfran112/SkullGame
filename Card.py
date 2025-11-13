class Card:
    def __init__(self, kind: str):
        assert kind in ("flower", "skull")
        self.kind = kind

    def __repr__(self):
        return self.kind
