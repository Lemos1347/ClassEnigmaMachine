class Rotor:
    """
    Representa um único rotor na máquina Enigma.
    Cada rotor realiza a substituição de caracteres e pode girar para alterar seu mapeamento.
    """

    def __init__(self, wiring: list[int], notch: int):
        # O cabeamento define o padrão de substituição
        self.wiring = wiring
        # A posição do entalhe aciona a rotação do próximo rotor
        self.notch = notch
        # A posição define a posição rotacional do rotor (0-25)
        self.position: int = 0
        # A configuração do anel afeta como o cabeamento se alinha com a posição
        self.ring_setting: int = 0

    def forward(self, char_pos: int) -> int:
        """Realiza a substituição direta (da direita para a esquerda) através do rotor."""
        shifted_pos = (char_pos + self.position - self.ring_setting) % 26
        substituted = self.wiring[shifted_pos]
        return (substituted - self.position + self.ring_setting) % 26

    def backward(self, char_pos: int) -> int:
        """Realiza a substituição inversa (da esquerda para a direita) através do rotor."""
        shifted_pos = (char_pos + self.position - self.ring_setting) % 26
        substituted = self.wiring.index(shifted_pos)
        return (substituted - self.position + self.ring_setting) % 26

    def rotate(self) -> bool:
        """Gira o rotor uma posição."""
        self.position = (self.position + 1) % 26
        # Retorna True se o rotor atingiu sua posição de entalhe
        return self.position == self.notch
