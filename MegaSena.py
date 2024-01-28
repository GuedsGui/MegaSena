import random


def numeros():
    numeros_mega_sena = random.sample(range(1, 100), 6)
    numeros_mega_sena.sort()

    return numeros_mega_sena


print('Bem vindo à MegaPython! Escolha seus números e boa sorte!')

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))
num4 = int(input('Quarto número: '))
num5 = int(input('Quinto número: '))
num6 = int(input('Sexto número: '))

if __name__ == '__main__':
    numeros_gerados = numeros()
    print(f'Números da MegaPython: {numeros_gerados}')
