# Tolga AKKAPULU
# /tolgaakkapulu

# -*- coding:utf-8 -*-

print("""
############################### Caesar Cipher ####################################
#          Caesar cipher is a type of substitution cipher in which each          #
#       letter in the plaintext is replaced by a letter some fixed number        #
#                        of positions down the alphabet.                         #
#--------------------------------------------------------------------------------#
#                    Tolga AKKAPULU  |  Github : /tolgaakkapulu                  #
##################################################################################""")
print(" ________________________________________________________________________________")
print("|                                                                                |")
print("| Alphabet : |a|b|c|d|e|f|g|h|i|j|k |l |m |n |o |p |q |r |s |t |u |v |w |x |y |z |")
print("| Number   : |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|")
print("|________________________________________________________________________________|\n")

print("++++++++++++++++++++++++++++++++++++++")
print("+    E(p) => c = p + key  mod(26)    +")
print("+    D(c) => p = c - key  mod(26)    +")
print("++++++++++++++++++++++++++++++++++++++")

print("\n---------------------------------")

L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def cipher(key,plaintext):
	ciphertext = ""
	for c in plaintext.upper():
	    if c.isalpha():
	        ciphertext += I2L[ (L2I[c] + int(key))%26 ]
	    else: 
	        ciphertext += c
	return ciphertext

def decipher(key,ciphertext):
	plaintext = ""
	for c in ciphertext.upper():
	    if c.isalpha(): 
	        plaintext += I2L[ (L2I[c] - int(key))%26 ]
	    else: 
	        plaintext += c
	return plaintext

def main():
	while True:
		try:
			print("  (1)  Encrypt\t  (2)  Decrypt")
			print("---------------------------------")
			mode=input("Mode (1 or 2)  : ")
	
			if( mode == '1' ):
				plaintext = input("Plain Text     : ")
				key = input("Key (Rotation) : ")
				cipherText = cipher(key,plaintext)
				print("Cipher Text    :",cipherText)
				print("\n---------------------------------")
						
			if( mode == '2' ):
				ciphertext = input("Cipher Text    : ")
				key = input("Key (Rotation) : ")
				plainText = decipher(key,ciphertext)
				print("Plain Text     :",plainText)
				print("\n---------------------------------")

			if( mode != '1' and mode != '2' ):
				print("\nIncorrect choice...\n")
				print("---------------------------------")
		except ValueError:
			print("\nInvalid key value...")
			print("\n---------------------------------")
		except KeyboardInterrupt:
			print("\n\nGood bye...")
			break
		except EOFError:
			print("\n\nGood bye...")
			break

if __name__ == '__main__':
	main()
