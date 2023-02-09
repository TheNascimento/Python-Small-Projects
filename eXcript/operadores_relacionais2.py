__author__ = 'Tiago Luiz'
# Continuação de exemplos de operadores relacionais.

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um outro número: "))

if(numero1==numero2): # Operador de igualdade.
    print("Os dois números são iguais.")
if(numero1!=numero2): # Operador de diferença.
    print("Os dois números são diferentes.")
if(numero1<numero2): # Operador de menor que.
    print("O número %d é menor que %d." %(numero1, numero2))
if(numero1>numero2): # Operador de maior que.
    print("O número %d é maior que %d." %(numero1, numero2))
if(numero1>=numero2): # Operador maior ou igual que.
    print("O número %d é maior ou igual que %d." %(numero1, numero2))
if(numero1<=numero2): # Operador menor ou igual que.
    print("O número %d é menor ou igual que %d." %(numero1, numero2))