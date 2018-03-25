# Tolga AKKAPULU
# /tolgaakkapulu

# -*- coding:utf-8 -*-


print("""
##############################  Bio-Cryptography  #################################
#----------------------------- DNA Encryption Key --------------------------------#
# 'A':'CGA','B':'CCA','C':'GTT','D':'TTG','E':'GGC','F':'GGT','G':'TTT','H':'CGC' #
# 'I':'ATG','J':'AGT','K':'AAG','L':'TGC','M':'TCC','N':'TCT','O':'GGA','P':'GTG' #
# 'Q':'AAC','R':'TCA','S':'ACG','T':'TTC','U':'CTG','V':'CCT','W':'CCG','X':'CTA' #
# 'Y':'AAA','Z':'CTT','_':'ATA',',':'TCG','.':'GAT',':':'GCT','0':'ACT','1':'ACC' #
# '2':'TAG','3':'GAC','4':'GAG','5':'AGA','6':'TTA','7':'ACA','8':'AGG','9':'GCG' #
#---------------------------------------------------------------------------------#
#                  Tolga AKKAPULU  |  Github : /tolgaakkapulu                     #
###################################################################################""")

print("\n---------------------------------")

table={'A':'CGA','B':'CCA','C':'GTT','D':'TTG',
'E':'GGC','F':'GGT','G':'TTT','H':'CGC',
'I':'ATG','J':'AGT','K':'AAG','L':'TGC',
'M':'TCC','N':'TCT','O':'GGA','P':'GTG',
'Q':'AAC','R':'TCA','S':'ACG','T':'TTC',
'U':'CTG','V':'CCT','W':'CCG','X':'CTA',
'Y':'AAA','Z':'CTT','_':'ATA',',':'TCG',
'.':'GAT',':':'GCT','0':'ACT','1':'ACC',
'2':'TAG','3':'GAC','4':'GAG','5':'AGA',
'6':'TTA','7':'ACA','8':'AGG','9':'GCG',
'CGA':'A','CCA':'B','GTT':'C','TTG':'D',
'GGC':'E','GGT':'F','TTT':'G','CGC':'H',
'ATG':'I','AGT':'J','AAG':'K','TGC':'L',
'TCC':'M','TCT':'N','GGA':'O','GTG':'P',
'AAC':'Q','TCA':'R','ACG':'S','TTC':'T',
'CTG':'U','CCT':'V','CCG':'W','CTA':'X',
'AAA':'Y','CTT':'Z','ATA':'_','TCG':',',
'GAT':'.','GCT':':','ACT':'0','ACC':'1',
'TAG':'2','GAC':'3','GAG':'4','AGA':'5',
'TTA':'6','ACA':'7','AGG':'8','GCG':'9'}

def bio_enc(message):
	cipher = ''
	for letter in message:
		if(letter == '{' or letter == '}' or letter == ' '):
			cipher += letter
		else:
			cipher += table[letter]
	return cipher

def bio_dec(message):
	decipher = ''
	i=0
	count=1
	string = ''
	for letter in message:
		if(letter != ' '):
			string += letter
			i += 1
		if(i==3):
			decipher += table[string]
			string = ''
			i=0
		if(letter == ' '):
			decipher += ' '
			string = ''
			i=0
		if(letter == '{' or letter == '}'):
			decipher += letter
			string = ''
			i=0
		count += 1
	return decipher
 
def main():
	while True:
		try:
			print("  (1)  Encrypt\t  (2)  Decrypt")
			print("---------------------------------")
			mode=input("Mode (1 or 2) : ")

			if(mode == '1'):
				message = input("Plain Text    : ")
				print("Cipher Text   :", bio_enc(message.upper()))
				print("\n---------------------------------")

			if(mode == '2'):     
				message = input("Cipher Text   : ")
				print("Plain Text    :", bio_dec(message.upper()))
				print("\n---------------------------------")

			if( mode != '1' and mode != '2' ):
				print("\nIncorrect choice...\n")
				print("---------------------------------")

		except KeyError:
			print("\nInvalid input...")
			print("\n---------------------------------")
		except KeyboardInterrupt:
			print("\n\nGood bye...")
			break
		except EOFError:
			print("\n\nGood bye...")
			break
 
if __name__ == '__main__':
	main()
