## Created By Ujikstark

#!/usr/bin/env python3
import hashlib
from termcolor import colored
import hashing

def decode():
	with open(file_pw, "r") as f:
		for item in f:		 			
			if decode_word in item:		
				print(colored(f"\n[+]Found --> {item}","green"))
					

choice = input("Encode or Decode : ")

		
if choice == 'Encode':
	hashing.word_hash = input("Word Do you wanna Hash : ")
	print("""1. md5\n2. sha1\n3. sha224\n4. sha256\n5. sha384\n6. sha512""")
	hash_type = int(input("Choose one : "))
		
	if hash_type == 1:
		hashing.hash_md5()	
	elif hash_type == 2:
		hashing.hash_sha1()
	elif hash_type == 3:
		hashing.hash_sha224()	
	elif hash_type == 4:
		hashing.hash_sha256()
	elif hash_type == 5:
		hashing.hash_sha384()
	elif hash_type == 6:
		hashing.hash_sha512()				
	else:
		print("ERROR!!")	

elif choice == 'Decode':
	decode_word = input("Garbage Word : ")
	file_pw = input("File Name for Password : ")
	decode()			

else:
	print("ERROR!!")
			
		
	
