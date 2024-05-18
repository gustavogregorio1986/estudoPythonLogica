nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))

if idade >= 18:
    print(f'O {nome} atigiu a maioridade com {idade}')
else:
    print(f'O {nome} não atigiu a maioridade com {idade}')