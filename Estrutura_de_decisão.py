#------------------------#----------------------------#
print('-' * 35)
print("Testando o comando IF \n(Digite um número menor de 18): ")
valor = int(input("Qual é a sua idade? "))
if valor < 18:
    print("Você ainda não pode dirigir!")
print('-' * 35)
#----------------------------#-----------------------#
print("Testando o comando IF..ELSE \n(Digite um número menor de 18): ")
valor = int(input("Qual é a sua idade? "))
if valor < 18:
    print("Você ainda não pode dirigir!")
else:
    print("Você pode dirigir! ")
print('-' * 35)
#----------------------------#-----------------------#
print("Testando o comando IF..ELIF..ELSE \n(Se..Senão Se..Senão)")
valor = int(input("Qual é a sua idade? "))
if valor < 6:
    print("Que fofura! ")
elif valor < 18:
    print("Você ainda não pode dirigir! ")
elif valor > 60:
    print("Você está na melhor idade! ")
else:
    print("Você pode dirigir! ")
print('-' * 35)
#----------------------------#-----------------------#
