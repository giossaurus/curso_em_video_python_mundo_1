s = float(input('Digite o salário atual do funcionário:' ))
a1 = (s * 0.10) + s
a2 = (s * 0.15) + s
if s <= 1250.00:
    print('O salário do funcionário com 15% de aumento, será de R${:.2f}'.format(a2))
else:
    print('O salário do funcionário com 10% de aumento, será de R${:.2f}'.format(a1))
