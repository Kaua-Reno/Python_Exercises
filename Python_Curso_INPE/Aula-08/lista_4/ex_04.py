palavras = str(input("Digite uma palavra para checar se é palíndromo: "))


# guardar palavra original
palavra_original = palavras
# transformar caracteres em minusculos
palavra = palavras.lower()
# remover espacos
palavra = palavra.replace(" ", "")
# testar se a string e igual lendo pelos dois sentidos
if palavra == palavra[::-1]:
    print (palavra_original + " e palindromo")
else:
    print (palavra_original + " nao e palindromo")