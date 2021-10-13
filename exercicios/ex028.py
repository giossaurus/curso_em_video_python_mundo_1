from random import randint
nprograma = randint(0,5)
print('Olá gafanhoto, estou pensando em um número de 0 a 5, que tal adivinhar o número que estou pensando?')
njogador = int(input('Qual número é?'))
if njogador == nprograma:
    print('Parabéns, você acertou!')
else:
    print('Que pena! Tente novamente.')