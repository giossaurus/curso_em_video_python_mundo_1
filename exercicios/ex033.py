a = int(input('Diga um número: '))
b = int(input('Diga outro número: '))
c = int(input('Diga mais um número: '))
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = a
if c < a and c < b:
    menor = c

if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = a
if c > a and c > b:
    maior = c

print('O menor número foi {}'.format(menor))
print('O maior número foi {}'.format(maior))