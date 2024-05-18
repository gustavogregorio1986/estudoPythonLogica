numeros = []

while True:
    entrada = input('Digite um número (ou "sair" para terminar): ')
    
    if entrada.lower() == 'sair':
        break

    try:
        numero = float(entrada)  3
        numeros.append(numero)
    except ValueError:
        print("Por favor, insira um número válido.")

print("Números digitados:", numeros)