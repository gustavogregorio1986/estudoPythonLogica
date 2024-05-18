idades = {'Ana': 25, 'João':34, 'Marcos':36, 'Luiz':45}

maior = 0
menor = 999

for nome, idade in idades.items():
  if(idade >= maior):  
    print(f'{nome} tem {idade} anos.')
  else:
    print(f'{nome} tem {idade} anos.')