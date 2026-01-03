# solicitar ao usuário que insira notas, como números float, uma por vez, até o usuário digitar enter sem informar nada.
# calcular a média aritimetica das notas inseridas e exibir o resultado.
notas = []
while True:
    nota_str = input("Digite uma nota (ou pressione Enter para calcular a média): ")
    if nota_str == "":
        break
    try:
        nota = float(nota_str)
        notas.append(nota)
    except ValueError:
        print("Por favor, digite um número válido.")

if notas:
    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.") 