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
        """Define as posições iniciais de todos os rotores."""
        for rotor, pos in zip(self.rotors, positions):
            rotor.position = ord(pos.upper()) - ord("A")

    def set_ring_settings(self, settings: str):
        """Define as configurações dos anéis para todos os rotores."""
        for rotor, setting in zip(self.rotors, settings):
            rotor.ring_setting = ord(setting.upper()) - ord("A")

    def _rotate_rotors(self):
        """Gerencia a rotação dos rotores, incluindo o mecanismo de duplo avanço."""
        # Verifica se o rotor do meio está na posição de entalhe
        if len(self.rotors) >= 2 and self.rotors[1].position == self.rotors[1].notch:
            # Os rotores do meio e da esquerda giram
            self.rotors[1].rotate()
            self.rotors[0].rotate()
        # Verifica se o rotor da direita está na posição de entalhe
        elif (
            len(self.rotors) >= 2 and self.rotors[-1].position == self.rotors[-1].notch
        ):
            # O rotor do meio gira
            self.rotors[1].rotate()

        # O rotor da direita sempre gira
        self.rotors[-1].rotate()

    def encode_char(self, char: str) -> str:
        """
        Codifica um único caractere através da Máquina Enigma.
        O caminho do sinal é:
        1. Através do plugboard (se houver conexões configuradas)
        2. Através dos rotores da direita para a esquerda
        3. Através do refletor
        4. De volta pelos rotores da esquerda para a direita
        5. Novamente através do plugboard
        """
        if not char.isalpha():
            return char

        # Converte para maiúscula para consistência
        char = char.upper()

        # Primeira passagem pelo plugboard
        char = self.plugboard.forward(char)

        # Converte o caractere para posição (0-25)
        char_pos = ord(char) - ord("A")

        # Gira os rotores antes da codificação
        self._rotate_rotors()

        # Passagem direta pelos rotores (da direita para a esquerda)
        for rotor in reversed(self.rotors):
            char_pos = rotor.forward(char_pos)

        # Através do refletor
        char_pos = self.reflector.reflect(char_pos)

        # Passagem inversa pelos rotores (da esquerda para a direita)
        for rotor in self.rotors:
            char_pos = rotor.backward(char_pos)

        # Converte a posição de volta para caractere
        char = chr(char_pos + ord("A"))

        # Segunda passagem pelo plugboard
        return self.plugboard.forward(char)

    def encode(self, text: str) -> str:
        """Codifica uma string através da Máquina Enigma"""
        return "".join(self.encode_char(c) for c in text)
