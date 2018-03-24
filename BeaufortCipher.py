# Tolga AKKAPULU
# /tolgaakkapulu

# -*- coding:utf-8 -*-

from pycipher import Beaufort

print("""
############################## Beaufort Cipher ###################################
#   The Beaufort cipher, created by Sir Francis Beaufort, is a polyalphabetic    # 
#    substitution cipher that is similar to the Vigenère cipher, except that     #
#            it enciphers characters in a slightly different manner.             #
#--------------------------------------------------------------------------------#
#                    Tolga AKKAPULU  |  Github : /tolgaakkapulu                  #
##################################################################################""")
print(" ________________________________________________________________________________")
print("|                                                                                |")
print("| Alphabet : |a|b|c|d|e|f|g|h|i|j|k |l |m |n |o |p |q |r |s |t |u |v |w |x |y |z |")
print("| Number   : |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|")
print("|________________________________________________________________________________|\n")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+ Encryption => Cipher Text = Key - Plain Text  mod(26)                          +")
print("+ Decryption => Plain Text  = Key - Cipher Text mod(26)                          +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("\n---------------------------------")

def beaufortCipher(key,message):
	cipher = ''
	for letter in message:
		if(letter != ' '):
			cipher += Beaufort(key).encipher(letter)		
		else:
			cipher += ' '
	return cipher

def beaufortDecipher(key,message):
	decipher = ''
	for letter in message:
		if(letter != ' '):
			decipher += Beaufort(key).decipher(letter)
		else:
			decipher += ' '
	return decipher

def main():
	while True:
		try:
			print("  (1)  Encrypt\t  (2)  Decrypt")
			print("---------------------------------")
			mode=input("Mode (1 or 2) : ")
	
			if( mode == '1' ):
				message = input("Plain Text    : ")
				key = input("Key           : ")
				cipher = beaufortCipher(key,message)
				print("Cipher Text   :",cipher)
				print("\n---------------------------------")
						
			if( mode == '2' ):
				message = input("Cipher Text   : ")
				key = input("Key           : ")
				decipher = beaufortDecipher(key,message)
				print("Plain Text    :",decipher)
				print("\n---------------------------------")

			if( mode != '1' and mode != '2' ):
				print("\nIncorrect choice...\n")
				print("---------------------------------")

		except KeyboardInterrupt:
			print("\n\nGood bye...")
			break
		except EOFError:
			print("\n\nGood bye...")
			break

if __name__ == '__main__':
	main()
