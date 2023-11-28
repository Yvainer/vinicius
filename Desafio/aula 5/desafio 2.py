from math import sqrt
CO =float(input('Qual o comprimento do cateto oposto? '))
CA =float(input('Qual o comprimento do cateto adjacente? '))
raiz = CO**2+ CA**2
H = sqrt(raiz)
print('O comprimento da hipotenusa vale {}!'.format((H)))