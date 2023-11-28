from math import sin, cos, tan, radians
ang =float(input('Qual o ângulo? '))

print('O Seno é {:.2f}'.format(sin(radians(ang))))
print('O Cosseno é {:.3f}'.format(cos(radians(ang))))
print('A tangente é {:.2f}'.format(tan(radians(ang))))