qd=int(input('Quantos dias alugados?'))
qk=int(input('Quantos Km rodados?'))
vp=(60*qd)+(0.15*qk)
print('O valor total a pagar é de R${:.2f}'.format(vp))