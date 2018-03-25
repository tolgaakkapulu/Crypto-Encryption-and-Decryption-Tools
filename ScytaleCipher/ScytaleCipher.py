# Tolga AKKAPULU
# /tolgaakkapulu

# -*- coding:utf-8 -*-

import math

print("""
############################### Scytale Cipher ###################################
#  In cryptography, a scytale is a tool used to perform a transposition cipher,  #
# consisting of a cylinder with a strip of parchment wound around it on which is #
#   written a message. The ancient Greeks, and the Spartans in particular, are   #
#     said to have used this cipher to communicate during military campaigns.    # 
#--------------------------------------------------------------------------------#
#                    Tolga AKKAPULU  |  Github : /tolgaakkapulu                  #
##################################################################################""")

print("\n---------------------------------")

def scytale_encrypt(plaintext, key):
	chars = [c.upper() for c in plaintext if c not in (' ',',','.','?','!',':',';',"'")]
	chunks = math.ceil(len(chars) / float(key))
	inters, i, j = [], 1, 1

	while i <= chunks:
		inters.append(tuple(chars[j - 1:(j + key) - 1]))
		i += 1
		j += key

	cipher, k = [], 0
	while k < key:
		l = 0
		while l < chunks:
			if k >= len(inters[l]):
				cipher.append('.')
			else:
				cipher.append(inters[l][k])
			l += 1
		k += 1

	return ''.join(cipher)


def scytale_decrypt(ciphertext, key):
	chars = [c for c in ciphertext]
	chunks = int(math.ceil(len(chars) / float(key)))
	inters, i, j = [], 1, 1

	while i <= key:
		inters.append(tuple(chars[j - 1:(j + chunks) -1]))
		i += 1
		j += chunks

	plain, k = [], 0
	while k < chunks:
		l = 0
		while l < len(inters):
			plain.append(inters[l][k])
			l += 1
		k += 1

	return ''.join(plain)

def main():
	while True:
		try:
			print("  (1)  Encrypt\t  (2)  Decrypt")
			print("---------------------------------")
			mode=input("Mode (1 or 2)               : ")
			
			if(mode == '1'):
				plaintext = input("Plain Text                  : ")
				band = int(input("Number of turns of the band : "))
				ciphertext = scytale_encrypt(plaintext, band)
				print("Cipher Text                 :",ciphertext)
				print("\n---------------------------------")

			if(mode == '2'):
				ciphertext = input("Cipher Text                 : ")
				band = int(input("Number of turns of the band : "))
				plaintext = scytale_decrypt(ciphertext, band)
				print("Plain Text                  :",plaintext)
				print("\n---------------------------------")

			if( mode != '1' and mode != '2' ):
				print("\nIncorrect choice...\n")
				print("---------------------------------")

		except ValueError:
			print("\nInvalid value...")
			print("\n---------------------------------")
		except KeyboardInterrupt:
			print("\n\nGood bye...")
			break
		except EOFError:
			print("\n\nGood bye...")
			break

if __name__ == '__main__':
	main()
