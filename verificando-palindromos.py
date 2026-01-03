# solicitar uma palavra ao usuário e verificar se a palavra informada ís um palíndromo
def eh_palindromo(palavra):
    # Remover espaços e converter para minúsculas
    palavra = palavra.replace(" ", "").lower()
    # Verificar se a palavra é igual à sua reversa
    return palavra == palavra[::-1]
# Solicitar entrada do usuário
palavra_usuario = input("Digite uma palavra para verificar se é um palíndromo: ")
# Verificar e exibir o resultado
if eh_palindromo(palavra_usuario):
    print(f"A palavra '{palavra_usuario}' é um palíndromo.")
else:
    print(f"A palavra '{palavra_usuario}' não é um palíndromo.")
    