import urllib.request
import random
from colorama import Fore, Style, init


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
            ==================================
             	Made by SADTRASH#1337
                & Supergamer5465#9523
             https://github.com/sadtrxsh
             https://github.com/Supergamer5465
            ==================================
                          
""")  
print(Fore.GREEN + Style.BRIGHT, """YOUR CHANCES OF THIS WORKING IS 
the amount of possible codes is 6.2050608e+19

62 quintrillion 50 quadrillion 8 trillion 388 billion 552 million 823 thousand 
487 possible realm codes

THATS 3125 out of 32318025202371264 valid for under 6 million realm codes""")
x=0
def checkRealm(code):
    for x in range(0,100000000000000):
        try:
            r=urllib.request.urlopen(URL)
            sourcecode=r.readlines()
            baa=sourcecode[74]
            print(Fore.GREEN + Style.BRIGHT, baa)
            return true 
            break
        except:
            URL = f'https://open.minecraft.net/pocket/realms/invite/{code}'
            x=x+1
            print(Fore.RED + Style.BRIGHT, "valid URL not found, attempt "+str(x))
            
        
        
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
