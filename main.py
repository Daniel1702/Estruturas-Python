__author__ = 'Daniel de Andrade'

#----------------------Ex01-----10/06---------------------------#
from Funções import hello
hello()
#----------------------Ex02-----#----------------------------#
from Funções import maior
maior(4,7)
#----------------------Ex03-----#----------------------------#
from Funções import soma
#variável local recebendo valor -> total = 10#
total = 10
#chamada do módulo soma de Funções usando sua variável#
soma(3,5)
#impressão da variável local do programa principal#
print("Total principal = ",total)
#----------------------Ex04-----#----------------------------#
import Funções
s = Funções.soma3(3,5)
print('Soma = ',s)
j = Funções.calcula_juros(500,20)
print("O juros é = ",j)
#----------------------Ex05-----#----------------------------#
print("\nResposta do Exercício 01")
from Ex_Funções import linha
linha(50)
print("\nResposta do Exercício 02\n")

from Ex_Funções import imprime_lista
L = [3,6,8,9,10,9,8,4]
imprime_lista(L)

print('\n\n')
#Um módulo é um arquivo python onde você cria, e tem uma ação, finalidade, só vai funcionar se ele for invocado no main, são arquivos pequenos que tem determinadas funções para serem executadas se chamadas no main.#
#---------------------------09/06---------------------------#
'''import Estrutura_de_decisão
print(Estrutura_de_decisão)

import Ex_Estru_decisão
print(Ex_Estru_decisão)

import Estrutura_de_repetição
print(Estrutura_de_repetição)

import Ex_Estru_repetição
print(Ex_Estru_repetição)'''