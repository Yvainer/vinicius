frase = input('Digite uma frase: ')
frase = frase.lower()
quantasvezes = frase.count('a')
primeiro = frase.find('a')
final = frase.rfind('a')

print('A letra A aparece {} vezes'.format(quantasvezes))
print('A letra A aparece primeiro no {} caractere'.format(primeiro))
print('A letra A aparece pela última vez no {} caractere'.format(final))
