#código para ver se um ano é bissexto

ano = int( input( "Ano: " ) )

bissexto = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

print("É bissexto: ", bissexto)

