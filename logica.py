nome = input('Digite o nome: ')

try:
    idade = int(input('Digite a idade: '))
except ValueError:
    print("Por favor, insira um número válido para a idade.")
    exit()

sexo = input('Sexo (m/f): ').lower()

print(f'Nome: {nome}')  # Esta linha imprime o nome

if idade >= 18 and sexo == 'm':
    print('Pode se alistar')
else:
    print('Não pode se alistar')