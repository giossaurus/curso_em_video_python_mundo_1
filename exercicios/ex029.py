v = int(input('Em qual velocidade o carro se encontra? '))
print ('O carro se encontra em {} km/h'.format(v))
m = (7 * (v - 80))
if v >= 80:
    print('Você ultrapassou o limite de velocidade e foi multado!')
    print('A multa será de R$ {}'.format(m))
else:
    print('Continue dirigindo com segurança e tenha uma boa viagem!')
print('---FIM---')