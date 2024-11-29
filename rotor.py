class Rotor:
    """
    Representa um único rotor na Enigma machine.
    Cada rotor realiza a substituição de caracteres e pode girar para alterar seu mapeamento.
    """

    def __init__(self, wiring: list[int], notch: int):
        # The wiring defines the substitution pattern
        self.wiring = wiring
        # The notch position triggers the rotation of the next rotor
        self.notch = notch
        # Position defines the rotational position of the rotor (0-25)
        self.position: int = 0
        # Ring setting affects how the wiring aligns with the position
        self.ring_setting: int = 0

    def forward(self, char_pos: int) -> int:
        """Realize a substituição direta (da direita para a esquerda) através do rotor."""
        shifted_pos = (char_pos + self.position - self.ring_setting) % 26
        substituted = self.wiring[shifted_pos]
        return (substituted - self.position + self.ring_setting) % 26

    def backward(self, char_pos: int) -> int:
        """Realize a substituição inversa (da esquerda para a direita) através do rotor."""
        shifted_pos = (char_pos + self.position - self.ring_setting) % 26
        substituted = self.wiring.index(shifted_pos)
        return (substituted - self.position + self.ring_setting) % 26

    def rotate(self) -> bool:
        """Gire o rotor uma posição."""
        self.position = (self.position + 1) % 26
        # Returns True if the rotor has reached its notch position
        return self.position == self.notch
