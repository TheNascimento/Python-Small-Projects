# -*- coding: utf-8 -*- 
__author__ = 'Tiago Luiz'
__date__ = '19/08/2014'
__version__ = '1.0'
# Programa simples apenas para a mostragem do número informado pelo 
# usuário.

repetir = True
while(repetir):
	num = raw_input("Informe qualquer número que você quiser.\n R: ")
	
	try:
		num = float(num)
	except:
		print("Você informou um valor errado!\n")
		
	if(type(num) == float):
		print("\nO número informado foi: %.2f" %(num))
		repetir = False
		
