pessoas = [
    {'nome': 'João', 'idade': 20, 'sexo': 'm'},
    {'nome': 'Ana', 'idade': 17, 'sexo': 'f'},
    {'nome': 'Pedro', 'idade': 18, 'sexo': 'm'},
    {'nome': 'Maria', 'idade': 19, 'sexo': 'f'}
]

for pessoa in pessoas:
    nome = pessoa['nome']
    idade = pessoa['idade']
    sexo = pessoa['sexo']
    
    print(f'Nome: {nome}')
    if idade >= 18 and sexo == 'm':
        print('Pode se alistar')
    else:
        print('Não pode se alistar')
    print('') 