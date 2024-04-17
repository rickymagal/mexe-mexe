class Carta:
    def __init__(self, numero, naipe):
        self.numero = numero
        self.naipe = naipe

class JogoCartas:
    def __init__(self):
        self.cartas_na_mesa = []  # Inicialmente, não há cartas na mesa

    def adicionar_carta(self, nova_carta_str):
        if nova_carta_str.strip():  # Verifica se a string não está vazia ou somente com espaços em branco
            # Verifica se o formato é uma sequência de 3 ou mais cartas seguidas de um naipe
            if nova_carta_str[0] == "(" and nova_carta_str[-2] == ")":
                cartas_naipe = nova_carta_str[1:-2].split()
                naipes = nova_carta_str[-1]
                for carta_numero in cartas_naipe:
                    for naipe in naipes:
                        nova_carta = Carta(carta_numero, naipe)
                    self.cartas_na_mesa.append(nova_carta)
                    # Verifica se o formato é uma carta seguida de 3 ou 4 naipes diferentes
            else:
                carta_numero = nova_carta_str[0]
                naipes = nova_carta_str[1:]
                for naipe in naipes:
                    nova_carta = Carta(carta_numero, naipe)
                    self.cartas_na_mesa.append(nova_carta)
        self.atualizar_mesa()  # Atualiza a exibição da mesa

    def verificar_carta(self, carta_verificar_str):
        if self.cartas_na_mesa:
            carta_verificar_str = carta_verificar_str.replace(" ", "")
            if carta_verificar_str.strip():  # Verifica se a string não está vazia ou somente com espaços em branco
                numero = carta_verificar_str[:-1]
                naipe = carta_verificar_str[-1]
                if numero.isdigit() or numero in {'J', 'Q', 'K', 'A'}:
                    carta_verificar = Carta(numero, naipe)
                    if self.verifica_carta_adicionada(self.cartas_na_mesa, carta_verificar):
                        print("A carta pode ser adicionada.")
                    else:
                        print("A carta não pode ser adicionada.")
                else:
                    print("Número de carta inválido.")
            else:
                print("Formato de entrada inválido.")


    def resetar_mesa(self):
        self.cartas_na_mesa = []  # Limpa todas as cartas da mesa
        self.atualizar_mesa()  # Atualiza a exibição da mesa
        print("Mesa resetada.")

    def atualizar_mesa(self):
        # Exibe a sequência de cartas na mesa
        print("Cartas na mesa:")
        for carta in self.cartas_na_mesa:
            print(f"{carta.numero}{carta.naipe}")

    def verifica_carta_adicionada(self, cartas_na_mesa, nova_carta):
        # Faça uma cópia temporária da mesa de cartas
        temp_mesa = cartas_na_mesa.copy()

        # Adicione a nova carta à cópia temporária
        temp_mesa.append(nova_carta)

        # Função para encontrar sequências do mesmo naipe
        def encontra_sequencias_mesmo_naipe(cartas):
            cartas.sort(key=lambda x: (self.valor_carta(x), x.naipe))
            valor_anterior = None
            naipe_anterior = None
            sequencia = 0
            for carta in cartas:
                if valor_anterior is not None and carta.naipe == naipe_anterior:
                    if self.valor_carta(carta) == self.valor_carta(valor_anterior) + 1:
                        sequencia += 1
                        if sequencia >= 2:
                            return True
                    else:
                        sequencia = 0
                else:
                    sequencia = 0
                valor_anterior = carta
                naipe_anterior = carta.naipe
            return False

        # Função para encontrar grupos de mesma numeração, mas de naipes diferentes
        def encontra_grupos_mesma_numeracao(cartas):
            grupos = {}
            for carta in cartas:
                valor = carta.numero
                if valor in grupos:
                    grupos[valor].append(carta.naipe)
                else:
                    grupos[valor] = [carta.naipe]
            for naipes in grupos.values():
                if len(naipes) >= 3:
                    return True
            return False

        return encontra_sequencias_mesmo_naipe(temp_mesa) or encontra_grupos_mesma_numeracao(temp_mesa)

    def valor_carta(self, carta):
        numero = carta.numero
        if numero.isdigit() or (numero == "10"):
            return int(numero)
        elif numero == 'J':
            return 11
        elif numero == 'Q':
            return 12
        elif numero == 'K':
            return 13
        elif numero == 'A':
            return 14
        else:
            return 0  # Valor padrão para outros casos
        
if __name__ == "__main__":
    jogo = JogoCartas()
    while True:
        comando = input("Digite o comando (add, verify, reset): ").strip().lower()
        if comando == "add":
            nova_carta_str = input("Digite a carta a ser adicionada (formato: número naipe): ")
            jogo.adicionar_carta(nova_carta_str)
        elif comando == "verify":
            carta_str = input("Digite a carta a ser verificada (formato: número naipe): ")
            jogo.verificar_carta(carta_str)
        elif comando == "reset":
            jogo.resetar_mesa()
        else:
            print("Comando inválido. Tente novamente.")
