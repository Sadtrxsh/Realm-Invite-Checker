import random
import string
import time
import sys
from colorama import Fore, Style, init
init()
f = open('realm_codes.txt', 'a')
print(Fore.RED + Style.BRIGHT, """ 

	░░░░░░░░▄██████▄
	░░░░░░░█▀▀▀██▀▀▀▄
	░░░░░░░█▄▄▄██▄▄▄█ U HAVE BEEN ABDUCTED BY
	░░░░░░░▀█████████
	░░░░░░░░▀███▄███▀░░ THE AYYLIEN
	░░░░░░░░░▀████▀░░░░░
	░░░░░░░▄████████▄░░░░ POST AYY LMAO 
	░░░░░░████████████░░░░ OR GET PROBERED
            ================================
                 Made by SADTRASH#1337
             https://github.com/sadtrxsh
            ================================
                          
""", Fore.WHITE + Style.NORMAL)
          
print ('')
time.sleep(1)
print('How Many realms you want made?')
print ('')
time.sleep(1)
amount = int(input(">"))
print ('')
time.sleep(1)
print ('Generating')
print ('')
time.sleep(2)
print ('')

fix = 1
while fix <= amount:
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=10))
    realm_url = "https://realms.gg/"
    f.write( code + '\n')
    realm_code = realm_url + code
    print('Code: ' + realm_code)
    fix += 1
time.sleep(2)
print ('')
print ('Now go greifing...')
