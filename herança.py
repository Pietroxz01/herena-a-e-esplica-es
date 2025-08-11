class Publicacao:
    def __init__(self, titulo, autor, editora):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora

    def display_details(self):
        print(f"{self.__class__.__name__}: '{self.titulo}', autor(a): {self.autor}, editora: {self.editora}")

class Livro(Publicacao):
    pass
    
class Jornal(Publicacao):
    pass

class Revista(Publicacao):
    pass

livro = Livro("Livro Ciencias", "Cem09", "Brasil")
livro.display_details()

jornal = Jornal("Polêmica Trump", "Globo", "Brasil")
jornal.display_details()

revista = Revista("Quarteto Fantastisco", "Marvel", "Brasil")
revista.display_details()