nome = input('Digite seu nome completo: ')
nomesep = nome.lower().split()
pri = nomesep[0]
ult = nomesep[-1]
print('Nome completo: {}'.format(nome.title()))
print('Nome completo: {}'.format(pri.title()))
print('Nome completo: {}'.format(ult.title()))