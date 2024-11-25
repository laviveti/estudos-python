# idade = 0
# altura = 0.0
# nome = ''

# idade = int(input('Informe sua idade: '))
# altura = float(input('informe sua altura: '))
# nome = input('Informe seu nome: ')

# print(f'Os dos informados foram:\nIdade: {idade}\nAltura: {altura}\nNome: {nome}')  

# Desafio:
userId = int(input('Informe seu ID: '))
name = input('Informe seu nome: ')
wage = float(input('Informe seu salário: '))
# isBrazilian = bool(input('Nacionalidade brasileira?: '))
isBrazilian = input('Nacionalidade brasileira?: ').lower() == 'sim'

print(f'Os dados informados foram:\nID: {userId}\nNome: {name}\nSalário: {wage}\nBrasileiro: {isBrazilian}')
