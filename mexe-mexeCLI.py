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
                    if self.encontrar_combinacao_valida(carta_verificar):
                        print("A carta pode ser adicionada.")
                    else:
                        print("A carta não pode ser adicionada.")
                else:
                    print("Número de carta inválido.")
            else:
                print("Formato de entrada inválido.")
        else:
            print("Não há cartas na mesa.")

    def resetar_mesa(self):
        self.cartas_na_mesa = []  # Limpa todas as cartas da mesa
        self.atualizar_mesa()  # Atualiza a exibição da mesa
        print("Mesa resetada.")

    def atualizar_mesa(self):
        # Exibe a sequência de cartas na mesa
        print("Cartas na mesa:")
        for carta in self.cartas_na_mesa:
            print(f"{carta.numero}{carta.naipe}")

    def encontrar_combinacao_valida(self, nova_carta):
        # Adiciona a nova carta temporariamente para verificar se pode formar uma combinação válida
        self.cartas_na_mesa.append(nova_carta)

        # Agrupa as cartas na mesa por número e naipe
        agrupamentos = {}
        for carta in self.cartas_na_mesa:
            chave = (carta.numero, carta.naipe)
            if chave in agrupamentos:
                agrupamentos[chave].append(carta)
            else:
                agrupamentos[chave] = [carta]

        # Verifica se todas as cartas podem ser agrupadas em grupos válidos
        for cartas_grupo in agrupamentos.values():
            if len(cartas_grupo) < 3:
                continue
            # Verifica se é uma sequência do mesmo naipe
            numeros = sorted([self.valor_carta(carta) for carta in cartas_grupo])
            sequencia = True
            for i in range(1, len(numeros)):
                if numeros[i] != numeros[i - 1] + 1:
                    sequencia = False
                    break
            if not sequencia:
                # Verifica se é uma trinca com naipes diferentes
                numeros = [self.valor_carta(carta) for carta in cartas_grupo]
                if len(set(numeros)) != 1:
                    self.cartas_na_mesa.remove(nova_carta)
                    return False
            # Se a opção de mostrar combinações estiver ativada, imprime a primeira combinação válida encontrada
        # Remove a nova carta adicionada temporariamente
        self.cartas_na_mesa.remove(nova_carta)
        return True

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
        elif comando.startswith("verify"):
            carta_str = input("Digite a carta a ser verificada (formato: número naipe): ")
            jogo.verificar_carta(carta_str)
        elif comando == "reset":
            jogo.resetar_mesa()
        else:
            print("Comando inválido. Tente novamente.")
