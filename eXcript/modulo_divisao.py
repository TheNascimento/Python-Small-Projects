__author__ = 'Tiago Luiz'
# Exemplos do uso do módulo de divisão (resto da divisão).
"""
print(4%2)
print(100%5)
print(90000%100==0)
"""

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

divisao = num1/num2
resto = num1%num2

print("\n %.2f dividido por %.2f é igual a %.2f." %(num1, num2, divisao))
print("O resto da divisão de %.2f por %.2f é igual a %.2f." %(num1, num2, resto))