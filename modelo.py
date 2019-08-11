class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

vingadores = Filme("vingadores - guerra infinita", 2019, 2)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - '
      f'Duração: {vingadores.duracao} horas - Likes: {vingadores.likes}')


twd = Serie("the walking dead", 2010, 10)
twd.dar_like()
twd.dar_like()
print(f'Nome: {twd.nome} - Ano: {twd.ano} - '
      f'Temporadas: {twd.temporadas} - Likes: {twd.likes}')
