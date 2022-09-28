#Funcionalidade do break no comando for

num = 0
 
for num in range(10):
    if num == 5:
        break    # interrompe o laço
 
    print('Número: ' + str(num))
 
print('Fora do Laço')