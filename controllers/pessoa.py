from random import randint, choice


# Devolve o numero de vezes que o primeiro numero aparece
def cont_num(lista):
    primeiro = lista[0]
    cont = 0

    for num in lista:
        if num == primeiro:
            cont += 1

    return cont


# Calculo de verificação do cpf
def mult_cpf(cont, poit, lista):
    val = True
    soma = 0

    for y in range(0, poit):
        soma += lista[y] * cont
        cont -= 1

        soma = soma * 10 % 11

        if soma == 10:
            soma = 0

        if soma == lista[poit]:
            print(f'OK num = {soma} teste = {lista[poit]} linha 30')

        else:
            print(f'Erro num = {soma} teste = {lista[poit]}')
            val = False

        return val


# Cria um CPF valido
def create_cpf(mascara=True):
    validacao = False
    lista = []
    cpf = ''

    while not validacao:

        # Cria uma lista de numeros aleatorios
        for n in range(0, 11):
            lista.append(randint(0, 9))

        if cont_num(lista) == 11:
            validacao = False

        primeiroTeste = mult_cpf(10, 9, lista)  # valida o primeiro numero apos (-)
        segundoTeste = mult_cpf(11, 10, lista)  # valida o segundo numero apos (-)

        if primeiroTeste and segundoTeste:
            validacao = True

        else:
            validacao = False

        if not validacao:
            lista = []

    if mascara:
        cont = 0
        for num in lista:
            if cont == 3 or cont == 6:
                cpf += '.'

            elif cont == 9:
                cpf += '-'

            cpf += f'{num}'
            cont += 1


    else:
        for num in cpf:
            cpf += f'{num}'

    return cpf


def create_data():
    nc_data = f'{randint(1970, 2022)}_{randint(1, 31)}_{randint(1, 12)}'

    return nc_data


def read_document(document):
    with open(document, "r", encoding="utf-8") as file:
        all_text = file.read()
        words = list(map(str, all_text.split()))
        return choice(words)


def create_nome():
    nome = ''
    docs = ['nomef.txt', 'nomem.txt']
    nome += read_document(choice(docs))

    for n in range(0, randint(1, 2)):
        nome += " " + read_document("sobrenome.txt").replace("_", " ")
    return nome

