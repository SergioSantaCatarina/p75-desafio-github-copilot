# solicitar dois numeros ao usuario
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
# solicitar a operação matematica a ser efetuada com os numeros informados, até que a operação informada seja == "q" para sair
while True:
    operacao = input("Digite a operacao matematica (+, -, *, /) ou 'q' para sair: ")
    if operacao == 'q':
        break
    elif operacao == '+':
        print(f"Resultado: {num1 + num2}")
    elif operacao == '-':
        print(f"Resultado: {abs(num1 - num2)}")
    elif operacao == '*':
        print(f"Resultado: {num1 * num2}")
    elif operacao == '/':
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Erro: Divisão por zero!")
    else:
        print("Operação inválida!")