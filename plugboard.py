class Plugboard:
    """
    Representa o plugboard da máquina Enigma.
    O plugboard permite que pares de letras sejam trocados antes e depois da criptografia principal dos rotores.
    """

    def __init__(self, pairs: str = ""):
        """
        Inicialize o plugboard com pares de letras a serem trocados.
        Argumentos:
            pairs (str): String contendo os pares de letras a serem conectados.
                    Por exemplo, 'AB CD' significa que A é trocado por B, e C por D.

        """
        self.mapping: dict[str, str] = {}
        # Remove any whitespace and convert to uppercase
        pairs = "".join(pairs.upper().split())

        # Create bidirectional mapping for each pair
        for i in range(0, len(pairs), 2):
            if i + 1 < len(pairs):
                a, b = pairs[i], pairs[i + 1]
                if a in self.mapping or b in self.mapping:
                    raise ValueError(
                        f"Configuração inválida do plugboard: Letra {a} ou {b} já está conectada"
                    )
                self.mapping[a] = b
                self.mapping[b] = a

    def forward(self, char: str) -> str:
        """
        Transforme um caractere através do plugboard.
        A transformação é recíproca - funciona da mesma forma em ambas as direções.
        """
        return self.mapping.get(char, char)
