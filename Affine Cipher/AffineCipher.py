# Tolga AKKAPULU
# /tolgaakkapulu

# -*- coding:utf-8 -*-

from pycipher import Affine
import string

print("")

print("""############################### Affine Cipher ####################################
#     Affine cipher is a type of monoalphabetic substitution cipher, wherein     #
#   each letter in an alphabet is mapped to its numeric equivalent, encrypted    #
#     using a simple mathematical function, and converted back to a letter.      #
#--------------------------------------------------------------------------------#
#                    Tolga AKKAPULU  |  Github : /tolgaakkapulu                  #
##################################################################################""")
print(" ________________________________________________________________________________")
print("|                                                                                |")
print("| Alphabet : |a|b|c|d|e|f|g|h|i|j|k |l |m |n |o |p |q |r |s |t |u |v |w |x |y |z |")
print("| Number   : |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|")
print("|________________________________________________________________________________|\n")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+ Key : (a,b)                                                                    +")
print("+ Encryption => E(p)= a*p + b    mod(m), a=[1,m] | b=[1,m], an=1 (mod m)         +")
print("+ Decryption => D(c)= n*(c - b)  mod(m)                                          +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("\n---------------------------------")
while True:
	try:		
		print("  (1)  Encrypt\t  (2)  Decrypt")
		print("---------------------------------")
		mode=input("Mode (1 or 2)       : ")
		
		if( mode == '1'):
			a=int(input("a (Value a for key) : "))
			if( a<1 or 26<a ):
				print("\nError for 'a'.\nEnter a value in the range [1,26]\n")
				continue
	
			b=int(input("b (Value b for key) : "))
			if( b<1 or 26<b ):
				print("\nError for 'b'.\nEnter a value in the range [1,26]\n")
				continue
			
			print("Key                 : (%d,%d)" %(a,b))
			plain=input("Plain Text          : ")
			cipher=''
			for letter in plain:
				if letter not in string.ascii_letters:
					cipher += letter
				else:
					cipher += Affine(a,b).encipher(letter)
			print("Cipher Text         :",cipher)
			print("---------------------------------")
		
		if( mode == '2'):
			a=int(input("a (Value a for key) : "))
			if( a<1 or 26<a ):
				print("\nError for 'a'.\nEnter a value in the range [1,26]\n")
				continue
	
			b=int(input("b (Value b for key) : "))
			if( b<1 or 26<b ):
				print("\nError for 'b'.\nEnter a value in the range [1,26]\n")
				continue
	
			print("Key                 : (%d,%d)" %(a,b))
			decipher=input("Cipher Text         : ")
			plain=''
			for letter in decipher:
				if letter not in string.ascii_letters:
					plain += letter
				else:
					plain += Affine(a,b).decipher(letter)
			print("Plain Text          :",plain)
			print("---------------------------------")
	
		if(mode != '1' and mode != '2'):
			print("\nIncorrect choice...\n")

	except AssertionError:
		print("\nInvalid value for a =",a,". No inverse exists (mod 26)")
	except ValueError:
		print("\nInvalid value...")
	except KeyboardInterrupt:
		print("\n\nGood bye...")
		break
	except EOFError:
		print("\n\nGood bye...")
		break
