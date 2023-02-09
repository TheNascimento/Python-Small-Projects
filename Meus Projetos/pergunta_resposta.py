# -*- coding: utf-8 -*- 
__author__ = 'Tiago Luiz'
__date__ = '19/08/2014'
__version__ = '1.0'
"""
	Programa simples de pergunta a resposta baseado em um outro programa
	, originalmente criado usando a linguagem C/C++ por uma colega de 
	curso (Mônica Ribeiro).
"""

print("\t\t\t Programa de Pergunta e Resposta")

sair1 = 0
while(sair1 == 0): # Sintaxe do While no Python!
	# Correto uso do método .lower() abaixo. Obs: .upper() segue a mesma
	# fórmula.
	resposta = raw_input("\nEae, você curte RPG?\nR: ").lower() 
	
	
	if(resposta == "sim"):
		print("\nÉ nóis muleque!")
		sair1 = 1
	elif(resposta == "não" or resposta == "nao"):
		print("\nProblema é seu!")
		sair1 = 1
	elif(resposta == "o que é rpg?"):
		sair1 = 1
		# Solução para texto multi-linha usando print()
		print("\nRole-playing game, também conhecido como RPG em" 
			" português: 'jogo de interpretação de personagens', é um" 
			" tipo de jogo em que os jogadores assumem os papéis de" 
			" personagens e criam narrativas colaborativamente. O" 
			" progresso de um jogo se dá de acordo com um sistema de" 
			" regras predeterminado, dentro das quais os jogadores" 
			" podem improvisar livremente.\n")
		
		sair2 = 0
		while(sair2 == 0): # Sempre lembra de usar diferentes variáveis 
			#para diferentes loops!
			resposta = raw_input("Eae curtiu o que leu?\nR: ").lower()
			
			if(resposta == "sim"):
				print("\nIsso mesmo, procure saber mais...")
				sair2 = 1
			elif(resposta == "não" or resposta == "nao"):
				print("\nTenho certeza que nem leu depois da primeira" 
				" linha...")
				sair2 = 1
			else:
				print("\nVocê não respondeu minha pergunta.")
				
	else:
		print("Responda 'Sim' ou 'Não'.")
		
print("Desligando...")				


