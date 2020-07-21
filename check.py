from colorama import Fore, Style, init
import requests
import urllib.request
import time
from bs4 import BeautifulSoup


init()
#SHUT THE FUCK UP ABOUT COLORAMA NOT WORKING, IT FUCKING WORKS OK!!!???
print(Fore.RED + Style.BRIGHT, """ 
	███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█ 
	████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█
	███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
	████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
	███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█ 
	████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█ 
	███▓▓▓▓▓▓▓╬╬▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
	████▓▓▓╬╬╬╬▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
	███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
	█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
	█████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██ 
	█████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██ 
	████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██ 
	████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██ 
	█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██ 
	█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███ 
	██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███ 
	███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████ 
	███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████ 
	████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████ 
	█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████ 
	██████████▓▓▓█▓▓▓╬▓██╬╬╬╬╬╬╬╬╬╬╬▓███████ 
	███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████ 
	██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████ 
	███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████
            ================================
             	Made by SADTRASH#1337
             https://github.com/sadtrxsh
            ================================
                          
""")  
#IF YOU DONT EAT MY ASS I WILL KILL YOU 

def checkRealm(code):

    URL = f'https://open.minecraft.net/pocket/realms/invite/{code}'
    RESPONSE = request.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
for one_a_tag in soup.findAll('var'):
	if line_count >= 75:
		return True
	else: 
		return False

line_count +=1

VALID_CODES_FILE   = "valid_realm_codes.txt"
INVALID_CODES_FILE = "invalid_realm_codes.txt"
CODES_FILE         = "realm_codes.txt"

validTokens_file   = open(VALID_CODES_FILE, 'a+')
invalidTokens_file = open(INVALID_CODES_FILE, 'a+')

with open(CODES_FILE , 'r') as codes_file:
    content = codes_file.readlines()
    codes = list(filter(None, list(map(lambda x: str.replace(x, "\n", ""), content)))) # deletes the useless shit

    for code in codes:
        status = checkRealm(code)
        if status is True:
            print(f'{Fore.GREEN + Style.BRIGHT} {code}', Fore.WHITE + Style.NORMAL)
            validTokens_file.write(code + "\n")
        else:
            print(f'{Fore.RED + Style.BRIGHT} {code}', Fore.WHITE + Style.NORMAL)
            invalidTokens_file.write(code + "\n")
print('Done, now go griefing.')
input() #the end
