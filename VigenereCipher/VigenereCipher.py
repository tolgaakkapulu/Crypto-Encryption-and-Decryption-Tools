# Tolga AKKAPULU
# /tolgaakkapulu

# -*- coding:utf-8 -*-

print("""
############################## Vigenère Cipher ###################################
#    The Vigenère cipher is a method of encrypting alphabetic text by using a    #
#  series of interwoven Caesar ciphers based on the letters of a keyword. It is  #
#                     a form of polyalphabetic substitution.                     # 
#--------------------------------------------------------------------------------#
#                    Tolga AKKAPULU  |  Github : /tolgaakkapulu                  #
##################################################################################""")
print(" ________________________________________________________________________________")
print("|                                                                                |")
print("| Alphabet : |a|b|c|d|e|f|g|h|i|j|k |l |m |n |o |p |q |r |s |t |u |v |w |x |y |z |")
print("| Number   : |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|")
print("|________________________________________________________________________________|\n")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+ Encryption => Cipher Text = Plain Text  + Key mod(26)                          +")
print("+ Decryption => Plain Text  = Cipher Text - Key mod(26)                          +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("\n---------------------------------")

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
	while True:
		try:
			print("  (1)  Encrypt\t  (2)  Decrypt")
			print("---------------------------------")
			mode=input("Mode (1 or 2) : ")
		
			if(mode == '1'):
				plaintext = input("Plain Text    : ")
				key = input("Key           : ")
				translated = encryptMessage(key, plaintext)
				print('Cipher Text   : %s' % (translated))
				print("\n---------------------------------")
			if(mode == '2'):
				ciphertext = input("Cipher Text   : ")
				key = input("Key           : ")
				translated = decryptMessage(key, ciphertext)
				print('Plain Text    : %s' % (translated))
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

def encryptMessage(key, message):
    	return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    	return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    	translated = [] 

    	keyIndex = 0
    	key = key.upper()

    	for symbol in message: 
    	    num = LETTERS.find(symbol.upper())
    	    if num != -1: 
    	        if mode == 'encrypt':
    	            num += LETTERS.find(key[keyIndex]) 
    	        elif mode == 'decrypt':
    	            num -= LETTERS.find(key[keyIndex]) 
	
    	        num %= len(LETTERS) 
	
    	        if symbol.isupper():
    	            translated.append(LETTERS[num])
    	        elif symbol.islower():
    	            translated.append(LETTERS[num].lower())
	
    	        keyIndex += 1 
    	        if keyIndex == len(key):
    	            keyIndex = 0
    	    else:
    	        translated.append(symbol)

    	return ''.join(translated)

if __name__ == '__main__':
	main()
