import math
num=int(input('Digite um ângulo: '))
sen=math.sin(math.radians(num))
cos=math.cos(math.radians(num))
tan=math.tan(math.radians(num))
print('O ângulo informado de {}, tem o seno {:.3f}, o cosseno {:.3f} e a tangente {:.3f}'.format(num, sen, cos, tan))
