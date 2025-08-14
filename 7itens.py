# Classe 1 - Livro
class Livro:
    def __init__(self, titulo, autor, paginas):
        # Guardando as infos básicas do livro
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.paginas_lidas = 0

    def ler(self, paginas):
        # Vai somando as páginas lidas
        self.paginas_lidas += paginas
        if self.paginas_lidas > self.paginas:
            self.paginas_lidas = self.paginas
        print(f"Você leu até a página {self.paginas_lidas}.")

    def progresso(self):
        # Calcula quantos % já foi
        porcento = (self.paginas_lidas / self.paginas) * 100
        print(f"Já leu {porcento:.1f}% do livro.")


# Classe 2 - Celular
class Celular:
    def __init__(self, marca, modelo, bateria=100):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria

    def fazer_chamada(self, minutos):
        # Gasta 1% de bateria por minuto (bem bruto mesmo)
        self.bateria -= minutos
        if self.bateria < 0:
            self.bateria = 0
        print(f"Chamada de {minutos} min. Bateria: {self.bateria}%.")

    def carregar(self, carga):
        self.bateria += carga
        if self.bateria > 100:
            self.bateria = 100
        print(f"Carregou até {self.bateria}%.")


# Classe 3 - Cachorro
class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self.nome}: au au!")

    def comer(self, comida):
        print(f"{self.nome} está comendo {comida}.")


# Classe 4 - Bicicleta
class Bicicleta:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
        self.velocidade = 0

    def pedalar(self, incremento):
        self.velocidade += incremento
        print(f"Tá a {self.velocidade} km/h.")

    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"Agora tá a {self.velocidade} km/h.")


# Classe 5 - Televisão
class Televisao:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho
        self.ligada = False
        self.canal = 1

    def ligar(self):
        self.ligada = True
        print("Ligou a TV.")

    def mudar_canal(self, canal):
        if self.ligada:
            self.canal = canal
            print(f"Canal {canal} colocado.")
        else:
            print("Não dá pra mudar, tá desligada.")


# Classe 6 - Fogão
class Fogao:
    def __init__(self, bocas):
        self.bocas = bocas
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print("Fogão ligado.")

    def cozinhar(self, prato):
        if self.ligado:
            print(f"Cozinhando {prato}...")
        else:
            print("Tá desligado, não cozinha nada.")


# Classe 7 - Relógio
class Relogio:
    def __init__(self, marca, horas=0, minutos=0):
        self.marca = marca
        self.horas = horas
        self.minutos = minutos

    def ajustar_hora(self, horas, minutos):
        self.horas = horas % 24
        self.minutos = minutos % 60
        print(f"Hora ajustada: {self.horas:02d}:{self.minutos:02d}")

    def mostrar_hora(self):
        print(f"{self.horas:02d}:{self.minutos:02d}")


# Testando tudo rapidinho
livro1 = Livro("O Hobbit", "J.R.R. Tolkien", 310)
livro1.ler(45)
livro1.progresso()

cel1 = Celular("Samsung", "Galaxy S21")
cel1.fazer_chamada(12)
cel1.carregar(10)

dog1 = Cachorro("Rex", "Pitbull", 5)
dog1.latir()
dog1.comer("ração")

bike1 = Bicicleta("Caloi", "Vermelha")
bike1.pedalar(15)
bike1.frear(6)

tv1 = Televisao("LG", 50)
tv1.ligar()
tv1.mudar_canal(5)

fogao1 = Fogao(4)
fogao1.ligar()
fogao1.cozinhar("macarrão")

rel1 = Relogio("Casio")
rel1.ajustar_hora(14, 30)
rel1.mostrar_hora()