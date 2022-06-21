from random import randint


def cont_num(cpf):
    primeiro = cpf[0]
    cont = 0

    for num in cpf:
        if num == primeiro:
            cont += 1

    return cont


def mult_cpf(cont, poit, cpf):
    val = True
    soma = 0

    for y in range(0, poit):
        soma += cpf[y] * cont
        cont -= 1

    soma = soma * 10 % 11

    print(soma)
    print(cpf[poit])
    if soma == 10:
        soma = 0

    if soma == cpf[poit]:
        print(f'OK num = {soma} teste = {cpf[poit]} linha 30')

    else:
        print(f'Erro num = {soma} teste = {cpf[poit]}')
        val = False

    return val


def create_cpf(mascara=True):
    validacao = False
    cpf = []
    texto = ''

    while not validacao:

        # Cria uma lista de numeros aleatorios
        for n in range(0, 11):
            cpf.append(randint(0, 9))

        if cont_num(cpf) == 11:
            validacao = False

        print('primeiro teste')
        primeiroTeste= mult_cpf(10, 9, cpf)   # valida o primeiro numero apos (-)

        print('segundo teste')
        segundoTeste = mult_cpf(11, 10, cpf)  # valida o segundo numero apos (-)

        if primeiroTeste and segundoTeste:
            validacao = True

        else:
            validacao = False

        if not validacao:
            cpf = []

    if mascara:
        cont = 0
        for num in cpf:
            if cont == 3 or cont == 6:
                texto += '.'

            elif cont == 9:
                texto += '-'

            texto += f'{num}'
            cont += 1

    else:
        for num in cpf:
            texto += f'{num}'

    return texto


def create_rg():
    pass


print(create_cpf())
