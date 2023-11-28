Alt =float(input('Qual a altura da sua parede?'))
Larg =float(input('Qual a largura da sua parede?'))
mt2 = Alt*Larg
Tinta = 2
Litros = mt2//Tinta
print('A área da sua parede é de {0}mt²'.format(mt2))
print('1 litro de tinta pinta 2 metros de sua parede, logo você precisará de {0} litros de tinta'.format(Litros))