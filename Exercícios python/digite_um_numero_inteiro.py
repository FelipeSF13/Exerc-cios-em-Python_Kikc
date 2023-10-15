# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é positivo
if numero < 1:
    print("Por favor, digite um número inteiro positivo.")
else:
    print(f"Números ímpares de 1 até {numero}:")
    for i in range(1, numero + 1, 2):
        print(i)
