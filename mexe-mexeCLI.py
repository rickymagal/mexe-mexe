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
            else:
                carta_numero = nova_carta_str[0]
                naipes = nova_carta_str[1:]
                for naipe in naipes:
                    nova_carta = Carta(carta_numero, naipe)
                    self.cartas_na_mesa.append(nova_carta)
        self.atualizar_mesa()  # Atualiza a exibição da mesa

    def verificar_carta(self, carta_verificar_str, show_combinacao=False):
        if self.cartas_na_mesa:
            carta_verificar_str = carta_verificar_str.replace(" ", "")
            if carta_verificar_str.strip():  # Verifica se a string não está vazia ou somente com espaços em branco
                numero = carta_verificar_str[:-1]
                naipe = carta_verificar_str[-1]
                if numero.isdigit() or numero in {'J', 'Q', 'K', 'A'}:
                    carta_verificar = Carta(numero, naipe)
                    if self.encontrar_combinacao_valida(carta_verificar, show_combinacao):
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

    def encontrar_combinacao_valida(self, nova_carta, show_combinacao=False):
        # Adiciona a nova carta temporariamente para verificar se pode formar uma combinação válida
        self.cartas_na_mesa.append(nova_carta)

        # Ordena as cartas na mesa por valor
        self.cartas_na_mesa.sort(key=lambda x: self.valor_carta(x))

        # Encontra os grupos de naipes diferentes e as sequências válidas
        naipes_diferentes_validos = []
        grupo_atual = []

        for carta in self.cartas_na_mesa:
            if not grupo_atual:
                grupo_atual.append(carta)
            else:
                if carta.numero == grupo_atual[0].numero:
                    if carta.naipe != grupo_atual[0].naipe:
                        grupo_atual.append(carta)
                    else:
                        if len(set([carta.naipe for carta in grupo_atual])) >= 3:
                            naipes_diferentes_validos.append(grupo_atual)
                        grupo_atual = [carta]
                else:
                    if len(set([carta.naipe for carta in grupo_atual])) >= 3:
                        naipes_diferentes_validos.append(grupo_atual)
                    grupo_atual = [carta]

        if len(set([carta.naipe for carta in grupo_atual])) >= 3:
            naipes_diferentes_validos.append(grupo_atual)

        sequencias_validas = []
        grupo_atual = []

        for carta in self.cartas_na_mesa:
            if not grupo_atual:
                grupo_atual.append(carta)
            else:
                if carta.naipe == grupo_atual[-1].naipe:
                    if self.valor_carta(carta) == self.valor_carta(grupo_atual[-1]) + 1 \
                            or (self.valor_carta(carta) == 2 and self.valor_carta(grupo_atual[-1]) == 13) \
                            or (self.valor_carta(carta) == 14 and self.valor_carta(grupo_atual[-1]) == 2):
                        grupo_atual.append(carta)
                    else:
                        if len(grupo_atual) >= 3:
                            sequencias_validas.append(grupo_atual)
                        grupo_atual = [carta]
                else:
                    if len(grupo_atual) >= 3:
                        sequencias_validas.append(grupo_atual)
                    grupo_atual = [carta]

        if len(grupo_atual) >= 3:
            sequencias_validas.append(grupo_atual)

        # Verifica se há uma combinação válida
        combinacao_valida = self.verificar_combinacao_valida(naipes_diferentes_validos, sequencias_validas)

        # Se a flag show_combinacao for verdadeira, imprime uma combinação válida
        if show_combinacao and combinacao_valida:
            print("Combinação válida encontrada:")
            for grupo in naipes_diferentes_validos + sequencias_validas:
                print("Grupo:")
                for carta in grupo:
                    print(f"{carta.numero}{carta.naipe}")
        elif show_combinacao:
            print("Não há combinação válida.")

        # Remove a nova carta adicionada temporariamente
        self.cartas_na_mesa.remove(nova_carta)

        return combinacao_valida

    def verificar_combinacao_valida(self, naipes_diferentes_validos, sequencias_validas):
        # Verifica se todas as cartas da mesa estão em exatamente um grupo
        cartas_agrupadas = set()
        for grupo in naipes_diferentes_validos + sequencias_validas:
            for carta in grupo:
                if carta in cartas_agrupadas:
                    return False
                cartas_agrupadas.add(carta)

        # Se todas as cartas estiverem em exatamente um grupo, a combinação é válida
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
            show_combinacao = "-s" in comando
            carta_str = input("Digite a carta a ser verificada (formato: número naipe): ")
            jogo.verificar_carta(carta_str, show_combinacao)
        elif comando == "reset":
            jogo.resetar_mesa()
        else:
            print("Comando inválido. Tente novamente.")
