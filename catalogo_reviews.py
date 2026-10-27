#Avaliacao:o que o usúario escreve sobre uma obra
class Avaliacao:
    def __init__(self, autor, nota, comentario = ""):
        if not 0 <= nota <= 10:
            raise ValueError("A nota deve estar entre 0 e 10.")
        self.autor = autor
        self.nota = nota
        self.comentario = comentario

    def __str__(self):
        texto = f"{self.autor}: {self.nota}/10%"
        if self.comentario:
            texto += f' - "{self.comentario}"'
        return texto

#obra: classe base. Outras classes herdam dela 

class Obra:
    tipo = "Obra" #atributo de classe: cada subclasse sobredescreve

    def __init__(self, titulo, ano, genero):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.avaliacoes = []

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def media(self):
        if not self.avaliacoes:
            return 0.0
        total = sum(a.nota for a in self.avaliacoes)
        return total / len(self.avaliacoes)

    def detalhes(self):
        #informaçaoes especificas de cada tipo, as subclasses sobredescrevem
        return ""

    def __str__(self):
        base = f"[{self.tipo}] {self.titulo} ({self.ano}) - {self.genero}"
        extra = self.detalhes()
        if extra:
            base += f" | {extra}"
        return f"{base} | média: {self.media():.1f} ({len(self.avaliacoes)} avaliações)"

class Filme(Obra):
    tipo = "Filme"

    def __init__(self, titulo, ano, genero, duracao_min):
        super().__init__(titulo, ano, genero)
        self.duracao_min = duracao_min


    def detalhes(self):
        return f"{self.duracao_min} min"


def main():
    avaliacao = Avaliacao("João Gabriel",10, "Otimo filme")
    print(avaliacao)

    obra = Obra("Homem aranha", 2026, "Ficlão Cientifica")
    print(obra)

    obra.adicionar_avaliacao(Avaliacao("Ana", 9))
    obra.adicionar_avaliacao(Avaliacao("Pedro", 7))
    print(obra)
    print("Média: ", obra.media())

filme = Filme("Matrix", 1999, "Ficção coentifica", 136)
filme.adicionar_avaliacao(Avaliacao("Carla", 10))
print(filme)

if __name__== "__main__":
    main()
