nome=str(input('digite seu nome completo: ')).strip()
nome=nome.split()
print('muito prazer {}'.format(nome[0]))
print( 'seu primeiro nome é: {}'.format(nome[0]))
print( 'seu ultimo nome é: {}'.format(nome[len(nome)-1]))
#print('A Ultima letra A esta na posiçao {}'.format( nome.upper().rfind('A')+1))