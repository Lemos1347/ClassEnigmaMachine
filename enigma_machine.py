from plugboard import Plugboard
from reflector import Reflector
from rotor import Rotor


class EnigmaMachine:
    """
    Representa a máquina Enigma completa, contendo múltiplos rotores, um refletor e um plugboard.
    """

    def __init__(
        self, rotors: list[Rotor], reflector: Reflector, plugboard_pairs: str = ""
    ):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = Plugboard(plugboard_pairs)

    def set_positions(self, positions: str):
        """Defina as posições iniciais de todos os rotores."""
        for rotor, pos in zip(self.rotors, positions):
            rotor.position = ord(pos.upper()) - ord("A")

    def set_ring_settings(self, settings: str):
        """Defina as configurações dos anéis para todos os rotores."""
        for rotor, setting in zip(self.rotors, settings):
            rotor.ring_setting = ord(setting.upper()) - ord("A")

    def _rotate_rotors(self):
        """Gerencie a rotação dos rotores, incluindo o mecanismo de duplo avanço."""
        # Check if middle rotor is at notch position
        if len(self.rotors) >= 2 and self.rotors[1].position == self.rotors[1].notch:
            # Middle and left rotors both step
            self.rotors[1].rotate()
            self.rotors[0].rotate()
        # Check if right rotor is at notch position
        elif (
            len(self.rotors) >= 2 and self.rotors[-1].position == self.rotors[-1].notch
        ):
            # Middle rotor steps
            self.rotors[1].rotate()

        # Right rotor always rotates
        self.rotors[-1].rotate()

    def encode_char(self, char: str) -> str:
        """
        Codifique um único caractere através da Enigma Machine.
        O caminho do sinal é:
        1. Através do plugboard (se houver conexões configuradas)
        2. Através dos rotores da direita para a esquerda
        3. Através do refletor
        4. De volta pelos rotores da esquerda para a direita
        5. Novamente através do plugboard
        """
        if not char.isalpha():
            return char

        # Convert to uppercase for consistency
        char = char.upper()

        # First pass through the plugboard
        char = self.plugboard.forward(char)

        # Convert character to position (0-25)
        char_pos = ord(char) - ord("A")

        # Rotate rotors before encoding
        self._rotate_rotors()

        # Forward pass through rotors (right to left)
        for rotor in reversed(self.rotors):
            char_pos = rotor.forward(char_pos)

        # Through the reflector
        char_pos = self.reflector.reflect(char_pos)

        # Backward pass through rotors (left to right)
        for rotor in self.rotors:
            char_pos = rotor.backward(char_pos)

        # Convert position back to character
        char = chr(char_pos + ord("A"))

        # Second pass through the plugboard
        return self.plugboard.forward(char)

    def encode(self, text: str) -> str:
        """Codifique uma string através da Enigma Machine"""
        return "".join(self.encode_char(c) for c in text)
