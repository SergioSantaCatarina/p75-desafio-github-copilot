# receber um número inteiro verificar se ele é par ou ímpar. Repetir a operação até que o usuário digite zero.
while True: 
    numero = int(input("Digite um número inteiro (ou 0 para sair): "))
    if numero == 0:
        print("Encerrando o programa.")
        break
    elif numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")    