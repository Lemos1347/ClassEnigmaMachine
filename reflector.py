class Reflector:
    """
    Representa o refletor na Enigma machine.
    O refletor realiza uma substituição fixa e envia o sinal de volta pelos rotores.
    """

    def __init__(self, wiring: list[int]):
        self.wiring = wiring

    def reflect(self, char_pos: int) -> int:
        """Realize a substituição pelo refletor."""
        return self.wiring[char_pos]
