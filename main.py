from enigma_machine import EnigmaMachine
from reflector import Reflector
from rotor import Rotor

# Rotor I:  EKMFLGDQVZNTOWYHXUSPAIBRCJ  (Notch: Q)
ROTOR_I: tuple[list[int], int] = (
    [ord(c) - ord("A") for c in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"],
    ord("Q") - ord("A"),
)

# Rotor II: AJDKSIRUXBLHWTMCQGZNPYFVOE  (Notch: E)
ROTOR_II: tuple[list[int], int] = (
    [ord(c) - ord("A") for c in "AJDKSIRUXBLHWTMCQGZNPYFVOE"],
    ord("E") - ord("A"),
)

# Rotor III: BDFHJLCPRTXVZNYEIWGAKMUSQO  (Notch: V)
ROTOR_III: tuple[list[int], int] = (
    [ord(c) - ord("A") for c in "BDFHJLCPRTXVZNYEIWGAKMUSQO"],
    ord("V") - ord("A"),
)

# Rotor IV: ESOVPZJAYQUIRHXLNFTGKDCMWB  (Notch: J)
ROTOR_IV: tuple[list[int], int] = (
    [ord(c) - ord("A") for c in "ESOVPZJAYQUIRHXLNFTGKDCMWB"],
    ord("J") - ord("A"),
)

# Rotor V: VZBRGITYUPSDNHLXAWMJQOFECK  (Notch: Z)
ROTOR_V: tuple[list[int], int] = (
    [ord(c) - ord("A") for c in "VZBRGITYUPSDNHLXAWMJQOFECK"],
    ord("Z") - ord("A"),
)


# Reflector A
# Input:   ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Output:  EJMZALYXVBWFCRQUONTSPIKHGD
REFLECTOR_A: list[int] = [ord(c) - ord("A") for c in "EJMZALYXVBWFCRQUONTSPIKHGD"]

# Reflector B
# Input:   ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Output:  YRUHQSLDPXNGOKMIEBFZCWVJAT
REFLECTOR_B: list[int] = [ord(c) - ord("A") for c in "YRUHQSLDPXNGOKMIEBFZCWVJAT"]

# Reflector C
# Input:   ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Output:  FVPJIAOYEDRZXWGCTKUQSBNMHL
REFLECTOR_C: list[int] = [ord(c) - ord("A") for c in "FVPJIAOYEDRZXWGCTKUQSBNMHL"]


def create_enigma_machine_I(plugboard_pairs: str = "") -> EnigmaMachine:
    """
    Crie uma Enigma machine com configurações da machine I de rotores.

    Argumentos:
        plugboard_pairs (str): String opcional especificando as conexões do plugboard.
            Por exemplo: 'AB CD EF' conecta A a B, C a D e E a F.
    """
    rotors = [Rotor(*ROTOR_I), Rotor(*ROTOR_II), Rotor(*ROTOR_III)]
    reflector = Reflector(REFLECTOR_B)
    return EnigmaMachine(rotors, reflector, plugboard_pairs)


if __name__ == "__main__":
    while True:
        print(
            """                                                           
                                 @@@@@@@@@@@@@@@@@                              
                        .@@@@@@                      @@@@@                      
                  .=@@@-                                    @@@@                
              .@@@              @@@  @@@@@@@@@@  @@@@=          .@@@-            
          .@@@          @@@@@  .@@@  @@@    .@@@.@@@.@@@@@@          .@@        
        @@          .@@@  .@@@  @@@  @@@        .@@@  @@.@@@@            @@      
    .@@        .@@@:.@@@  .@@@  @@@  @@@        .@@@  @@  @@#  @@@@@@      .@@  
  .@@       .@@@@    @@@  .@@@  @@@  @@@        .@@@  @@  @@= =@@  .@@        .@@
.@@         @@      .@@@  .@@@  @@@  @@@        .@@@  @@  @@  @@    @@          .@@
 .@         @@@@@@  .@@@  .@@@  @@@  @@@.@@@@@@@.@@@  @@  @@  @@  .@@@         .@@
  .@@       @@@      @@@  .@@@  @@@  @@@    .@@@.@@@  @@  @@  @@@@@@@@        .@@
    .@      @@@@+    @@@   +@@  @@@  @@@    .@@@.@@@  @@  @@  @@  .@@@      .@@  
      .@@      .@@@@.@@@   +@@  @@@  @@@    .@@@.@@@  @@  @@  @@          .@@    
          @@        .@@@   +@@  @@@  @@@    .@@@.@@@  @@.+@@            @@      
            .@@@           +@@  @@@  @@@@   =@@@.@@@.@@@            @@@          
                .-@@@                  @@@@@@@                @@@@              
                      .@@@@@                          .%@@@@@                    
                               @@@@@@@@@@@@@@@@@@@@@@       

                === Bem-vindo ao Simulador de Enigma Machine! 🕵️ ===                                                                               
    """
        )

        # Configuração do plugboard
        print(
            "Insira as conexões do plugboard (pares de letras, separados por espaço, máximo de 10 pares)"
        )
        print("Exemplo: AB CD EF (A conecta com B, C com D, E com F)")
        print("Pressione Enter para não usar conexões no plugboard")
        plugboard = input("Plugboard: ").strip()

        try:
            enigma_machine_I = create_enigma_machine_I(plugboard)

            # Configuração da posição inicial dos rotores ("private key")
            while True:
                positions = (
                    input(
                        "\nInsira as posições iniciais dos rotores (3 letras, por exemplo, AAA): "
                    )
                    .strip()
                    .upper()
                )
                if len(positions) == 3 and positions.isalpha():
                    break
                print("Por favor, insira exatamente 3 letras.")

            # Configurção dos rings
            while True:
                ring_settings = (
                    input(
                        "\nInsira as configurações dos anéis (3 letras, por exemplo, AAA): "
                    )
                    .strip()
                    .upper()
                )
                if len(ring_settings) == 3 and ring_settings.isalpha():
                    break
                print("Por favor, insira exatamente 3 letras.")

            # Configuração da máquina
            enigma_machine_I.set_positions(positions)
            enigma_machine_I.set_ring_settings(ring_settings)

            message = input("\nInsira a mensagem para codificar/decodificar: ").strip()

            result = enigma_machine_I.encode(message)

            print("\nResultado:", result)

            while True:
                same_settings = (
                    input(
                        "\nVocê quer codificar outra mensagem com as mesmas configurações? (y/n): "
                    )
                    .strip()
                    .lower()
                )
                if same_settings in ["y", "n"]:
                    break

            if same_settings == "y":
                while True:
                    enigma_machine_I.set_positions(positions)

                    message = input(
                        "\nInsira a mensagem para codificar/decodificar: "
                    ).strip()

                    result = enigma_machine_I.encode(message)

                    print("\nResultado:", result)

                    continue_same = (
                        input(
                            "\nVocê quer codificar outra mensagem com as mesmas configurações? (y/n): "
                        )
                        .strip()
                        .lower()
                    )
                    if continue_same != "y":
                        break

            restart = (
                input("\nVocê quer recomeçar com novas configurações? (y/n): ")
                .strip()
                .lower()
            )
            if restart != "y":
                print("\nObrigado por usar o Simulador da Enigma Machine! 🙌")
                break

        except ValueError as e:
            print(f"\nError: {e}")
            print("Please try again.")
