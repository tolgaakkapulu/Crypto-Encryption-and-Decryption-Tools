# Tolga AKKAPULU
# /tolgaakkapulu

# -*- coding:utf-8 -*-

print("""
############################ Atbash ##################################
#   Atbash is a monoalphabetic substitution cipher originally used   #
#   to encrypt the Hebrew alphabet.It can be modified for use with   #
#      any known writing system with a standard collating order.     #
#--------------------------------------------------------------------#
#            Tolga AKKAPULU  |  Github : /tolgaakkapulu              #
######################################################################""")
print(" _____________________________________________________________")
print("| Lookup Table                                                |")
print("|    |a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|    |")
print("|    |z|y|x|w|v|u|t|s|r|q|p|o|n|m|l|k|j|i|h|g|f|e|d|c|b|a|    |")
print("|_____________________________________________________________|")

print("\n---------------------------------")

lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}
 
def atbash(message):
	cipher = ''
	for letter in message:
		if(letter != ' '):
			cipher += lookup_table[letter]
		else:
			cipher += ' '
	return cipher
 
def main():
	while True:
		try:
			print("  (1)  Encrypt\t  (2)  Decrypt")
			print("---------------------------------")
			mode=input("Mode (1 or 2)     : ")
			if(mode == '1'):
				message = input("Encrypt message   : ")
				print("Encrypted Message :", atbash(message.upper()))
				print("\n---------------------------------")
			if(mode == '2'):     
				message = input("Decrypt message   : ")
				print("Decrypted Message :", atbash(message.upper()))
				print("\n---------------------------------")
			if(mode != '1' and mode != '2'):
				print("\nIncorrect choice...\n")
				print("---------------------------------")

		except KeyError:
			print("\nInvalid message...\n")
			print("---------------------------------")
		except ValueError:
			print("\nInvalid value...")
		except KeyboardInterrupt:
			print("\n\nGood bye...")
			break
		except EOFError:
			print("\n\nGood bye...")
			break
 
if __name__ == '__main__':
	main()
