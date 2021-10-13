distviag = float(input('Qual a distância de sua viagem?' ))
if distviag <= 200:
    p = distviag * 0.50
    print('O valor da passagem de ônibus será de R$ {:.2f} para o trajeto informado.'.format(p))
else:
    pd = distviag * 0.45
    print('O valor da passagem de ônibus será de R$ {:.2f} para o trajeto informado.'.format(pd))
print('---FIM---')