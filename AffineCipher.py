

from pycipher import Affine
import string

print("\t(1)  Encrypt\n\t(2)  Decrypt")
mode=input("Mode : ")

if( mode == '1'):
	a=int(input("a : "))
	b=int(input("b : "))
	plain=input("Plain Text : ")
	cipher=''
	for letter in plain:
		if letter not in string.ascii_letters:
			cipher += letter
		else:
			cipher += Affine(a,b).encipher(letter)
	print("Cipher Text : ", cipher)

if( mode == '2'):
	a=int(input("a : "))
	b=int(input("b : "))
	decipher=input("Cipher Text : ")
	plain=''
	for letter in decipher:
		if letter not in string.ascii_letters:
			plain += letter
		else:
			plain += Affine(a,b).decipher(letter)
	print("Plain Text : ", plain)
