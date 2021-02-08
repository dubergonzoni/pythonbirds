class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    caio = Pessoa(nome = 'Caio', idade = 0)
    eduardo = Pessoa(caio, nome = 'Eduardo')
    print(Pessoa.cumprimentar(eduardo))
    print(id(eduardo))
    print(eduardo.cumprimentar())
    print(eduardo.nome)
    print(eduardo.idade)
    for filho in eduardo.filhos:
        print(filho.nome)
    eduardo.sobrenome = 'Bergonzoni Junqueira'
    eduardo.olhos = 3
    del eduardo.olhos
    print(eduardo.__dict__)
    print(caio.__dict__)
    Pessoa.olhos = 4
    print(Pessoa.olhos)
    print(eduardo.olhos)
    print(caio.olhos)
    print(id(Pessoa.olhos), id(eduardo.olhos), id(caio.olhos))
