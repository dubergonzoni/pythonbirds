class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    caio = Pessoa(nome = 'Caio')
    eduardo = Pessoa(caio, nome = 'Eduardo')
    print(Pessoa.cumprimentar(eduardo))
    print(id(eduardo))
    print(eduardo.cumprimentar())
    print(eduardo.nome)
    print(eduardo.idade)
    for filho in eduardo.filhos:
        print(filho.nome)
    eduardo.sobrenome = 'Bergonzoni'
    print(eduardo.__dict__)
    print(caio.__dict__)