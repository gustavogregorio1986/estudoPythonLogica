pessoas = [

   {'nome':'luana', 'email':'luana@gmail.com', 'sexo': 'f', 'cpf': '1234567890'},
   {'nome':'eduardo', 'email':'eduardo@gmail.com', 'sexo': 'm', 'cpf': '0987654321'},
   {'nome':'marcos', 'email':'marcos@gmail.com', 'sexo': 'm', 'cpf': '67812345098'},
   {'nome':'mateus', 'email':'matheus@gmail.com', 'sexo': 'm', 'cpf': '8907612345'},
]

for pessoa in pessoas:
    nome = pessoa['nome']
    email = pessoa['email']
    sexo = pessoa['sexo']
    cpf = pessoa['cpf']
    print(f'nomew: {nome}, email: {email}, sexo: {sexo}, cpf: {cpf}')