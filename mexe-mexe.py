import tkinter as tk

class Carta:
    def __init__(self, numero, naipe):
        self.numero = numero
        self.naipe = naipe

class JogoCartas:
    def __init__(self, root):
        self.cartas_na_mesa = []  # Inicialmente, não há cartas na mesa

        # Configuração da janela principal
        root.title("Mexe-mexe")
        root.geometry("400x400")

        # Rótulo
        self.label = tk.Label(root, text="Adicione cartas à mesa:")
        self.label.pack()

        # Entrada para adicionar carta
        self.entry = tk.Entry(root)
        self.entry.pack()

        # Botão para adicionar carta
        self.botao_adicionar = tk.Button(root, text="Adicionar Carta", command=self.adicionar_carta)
        self.botao_adicionar.pack()

        # Botão para verificar a carta
        self.botao_verificar = tk.Button(root, text="Verificar Carta", command=self.verificar_carta)
        self.botao_verificar.pack()

        # Botão para redefinir a mesa
        self.botao_reset = tk.Button(root, text="Resetar Mesa", command=self.resetar_mesa)
        self.botao_reset.pack()

        # Rótulo para mostrar o resultado
        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.pack()

        # Widget de texto para exibir a mesa
        self.mesa_texto = tk.Text(root)
        self.mesa_texto.pack()

    def adicionar_carta(self):
        nova_carta_str = self.entry.get()
        if nova_carta_str.strip():  # Verifica se a string não está vazia ou somente com espaços em branco
            numero, naipe = nova_carta_str.split()
            nova_carta = Carta(numero, naipe)
            self.cartas_na_mesa.append(nova_carta)
            self.entry.delete(0, tk.END)  # Limpa a entrada
            self.atualizar_mesa()  # Atualiza a exibição da mesa

    def verificar_carta(self):
        if self.cartas_na_mesa:
            carta_verificar_str = self.entry.get()
            if carta_verificar_str.strip():  # Verifica se a string não está vazia ou somente com espaços em branco
                numero, naipe = carta_verificar_str.split()
                carta_verificar = Carta(numero, naipe)
                if self.verifica_carta_adicionada(self.cartas_na_mesa, carta_verificar):
                    self.resultado_label.config(text="A carta pode ser adicionada.")
                else:
                    self.resultado_label.config(text="A carta não pode ser adicionada.")

    def resetar_mesa(self):
        self.cartas_na_mesa = []  # Limpa todas as cartas da mesa
        self.atualizar_mesa()  # Atualiza a exibição da mesa
        self.resultado_label.config(text="Mesa resetada.")

    def atualizar_mesa(self):
        # Limpa o widget de texto e exibe a sequência de cartas na mesa
        self.mesa_texto.delete(1.0, tk.END)
        for carta in self.cartas_na_mesa:
            self.mesa_texto.insert(tk.END, f"{carta.numero}{carta.naipe}\n")

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
        elif numero in {'J', 'Q', 'K', 'A'}:
            return 10  # Valor fixo para cartas J, Q, K e A
        else:
            return 0  # Valor padrão para outros casos


if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoCartas(root)
    root.mainloop()
