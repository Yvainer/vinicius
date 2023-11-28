#teste de strip, replace
curso = '    Programação em python    '
print(len(curso.strip()))
curso = curso.strip()

#assim nao muda:
curso.replace('python','java')
#assim muda:
curso = curso.replace('python','java')
print(curso)

print(curso.find('java'))