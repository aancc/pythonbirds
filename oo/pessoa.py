class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    augusto = Pessoa(nome = 'Augusto')
    darlla = Pessoa(augusto, nome = 'Darlla')
    print(Pessoa.cumprimentar(darlla))
    print(id(darlla))
    print(darlla.cumprimentar())
    print(darlla.nome)
    print(darlla.idade)
    for filho in darlla.filhos:
        print(filho.nome)
    darlla.sobrenome = 'Régis'
    del darlla.filhos
    darlla.olhos = 1
    del darlla.olhos
    print(darlla.sobrenome)
    print(darlla.__dict__)
    print(augusto.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(darlla.olhos)
    print(augusto.olhos)
    print(id(Pessoa.olhos), id(darlla.olhos), id(augusto.olhos))


