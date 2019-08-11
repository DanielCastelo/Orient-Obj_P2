class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0


    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} minutos - {self.likes} likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} likes'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas


    def __len__(self):
        return len(self._programas)


vingadores = Filme("vingadores: ultimato", 2019, 180)
twd = Serie("the walking dead", 2010, 10)
rei = Filme('o rei leao', 1994, 90)
tbbt = Serie('the big bang theory', 2007, 12)

vingadores.dar_like()
vingadores.dar_like()
rei.dar_like()
rei.dar_like()
rei.dar_like()
twd.dar_like()
twd.dar_like()
twd.dar_like()
tbbt.dar_like()
tbbt.dar_like()

filmes_e_series = [vingadores, twd, tbbt, rei]
lista_fds = Playlist('Weekend', filmes_e_series)


print(f'Tamanho do playlist: {len(lista_fds.listagem)}')

print(f'O Rei Leão está na lista: {rei in lista_fds}')

for programa in lista_fds:
    print(programa)
