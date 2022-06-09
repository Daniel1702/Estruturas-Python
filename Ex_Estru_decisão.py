print('-' * 35)
print("Exercício 01 Estrutura de Decisão\n")
nota1 = float(input("Digite a 1ª nota do aluno: "))
nota2 = float(input("Digite a 2ª nota do aluno: "))

média = (nota1 + nota2)/2
print("Média = {}".format(média))
if média >=6:
  print("Aprovado!")
else:
  print("Reprovado!")
#-----------------------------#-------------------------#
print('-' * 35)
print("Exercício 02 Estrutura de Decisão\n")
nota1 = float(input("Digite a 1ª nota do aluno: "))
nota2 = float(input("Digite a 2ª nota do aluno: "))

média = (nota1 + nota2)/2
print("Média = {}".format(média))
if média > 6:
  print("Aprovado!")
elif média >= 4:
  print("Exame!")
else:
  print("Reprovado!")