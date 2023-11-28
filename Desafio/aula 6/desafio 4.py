cidade = input('Digite o nome da cidade: ')
cidade = cidade.lower()
sep = cidade.split()
div = (sep[0:4])
santo = 'santo' in div
print(santo)