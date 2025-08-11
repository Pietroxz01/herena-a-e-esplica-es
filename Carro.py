class Carro:
    """
    Classe que representa um carro com atributos e métodos
    para controla/r cor, marca e velocidade.
    """

    def __init__(self, cor, marca):
        """
        Método construtor: inicializa os atributos do carro.
        - cor: cor do carro
        - marca: marca do carro
        """
        self.cor = cor                # Armazena a cor do carro
        self.marca = marca            # Armazena a marca do carro
        self.velocidade = 0           # Velocidade inicial (km/h)

    def acelerar(self, incremento):
        """
        Aumenta a velocidade do carro.
        - incremento: valor a ser somado na velocidade
        """
        self.velocidade += incremento  # Soma o incremento à velocidade atual
        print(f"O carro acelerou. Velocidade atual: {self.velocidade} km/h")

    def frear(self, decremento):
        """
        Reduz a velocidade do carro.
        - decremento: valor a ser subtraído da velocidade
        """
        self.velocidade -= decremento  # Subtrai o decremento da velocidade
        if self.velocidade < 0:        # Impede que a velocidade fique negativa
            self.velocidade = 0
        print(f"O carro freiou. Velocidade atual: {self.velocidade} km/h")

    def exibir_dados(self):
        """
        Exibe as informações do carro:
        - Marca
        - Cor
        - Velocidade atual
        """
        print(f"Marca: {self.marca}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade atual: {self.velocidade} km/h")


# Exemplo de uso com Bugatti
carro1 = Carro("Azul", "Bugatti")  # Cria um carro azul da marca Bugatti

carro1.exibir_dados()  # Mostra os dados do carro
carro1.acelerar(415)   # Aumenta a velocidade em 415 km/h
carro1.frear(99)       # Reduz a velocidade em 99 km/h
carro1.frear(90)       # Reduz a velocidade em 90 km/h
