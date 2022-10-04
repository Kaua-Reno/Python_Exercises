frases = str(input("Digite uma frase para checar se é palíndromo: "))

# lista de caracteres para desconsiderar (opcional)
remover = (" ", ",", ".", "!", "-")
 
# guardar palavra original
frase_original = frases
# transformar caracteres em minusculos
frase = frases.lower()
# remover caracteres indesejados
for caractere in remover:
    frase = frase.replace(caractere, "")
# testar se a string e igual lendo pelos dois sentidos
if frase == frase[::-1]:
    print (frase_original + " e palindromo")
else:
    print (frase_original + " nao e palindromo")