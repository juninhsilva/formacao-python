'''

Desafio

Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.
Entrada

A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.
Saída

Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.
 
Exemplo de Entrada 	Exemplo de Saída

4
56234523485723854755454545478690 78690
5434554 543
1243 1243
54 64545454545454545454545454545454554
	

encaixa
nao encaixa
encaixa
nao encaixa

'''

''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
n = int(input())

''' 
TODO  Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se
"encaixa" ou "não encaixa" para cada uma das relações N vezes.
'''

while(N > 0):
    n-=1
    numeros = input().split();
    a = numeros[0]
    b = numeros[1]

    if a.endswith(B):
        print("encaixa")
    else:
        print("nao encaixa")

    