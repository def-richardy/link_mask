import gdshortener
from termcolor import colored
import os

shortness_link = gdshortener.ISGDShortener()

def banner(msg):
	print('-' * 50)
	print(f'{msg.upper():^45}')
	print('-' * 50)
	print('\n')

def line():
	print('-' * 50)


print("""
                                                  
                                                  
                                                  
                                                  
                                                  
                   .^!?JJJJ?!^.                   
                 ^5#@@@@@@@@@@#5^                 
               .Y@@@@@@@@@@@@@@@@Y.               
               Y@@@@@@@@@@@@@@@@@@Y               
               G@@@@@@@@@@@@@@@@@@G               
               Y@@@@@@@@@@@@@@@@@@Y               
               ^@@5!!?P#@@#P?!!P@&^               
               ~@&:    ~@@~    :&@~               
               !@@#Y?JP#GG#PJ?Y#@@!               
                ~7JB@@@# .#@@@BJ7~                
                   ^&@@@BB@@@&:                   
                    ^7?JYYJ?7:                    
                                                  
                                                  
                                                  
""")

while True:
	banner('link mask')
	user_option = int(input("""
[ 1 ] - Mascarar link
[ 2 ] - Sobre 

Escolha [1 ou 2]: """))
	if (user_option == 1):
		print('\nEscolha um domínio (inclua "https://www.site.com")\nExemplo: https://www.google-rewards.com\n')
		link = input('Qual link deseja mascarar?: ')
		mask = input('Digite o domínio para mascarar o link: ')
		short_link = shortness_link.shorten(link)[0]
		masked_link = mask + '@' + short_link[8:]
		print('Seu link está pronto.\n')
		print(colored(f'{masked_link}', 'green'))
		print('\n')
		line()
		
	elif (user_option == 2):
		os.system('clear' or 'cls')
		print("""
Criador: @def_richardy (instagram)
Ferramenta usada: is.gd (Url Short)""")
		break

input('Digite [ENTER] para sair: ')

		