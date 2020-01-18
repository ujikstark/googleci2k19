import hashlib
from termcolor import colored

def hash_md5():
	md5 = hashlib.md5()
	encode_md5 = hashlib.md5(str(word_hash).encode('utf-8'))
	result = encode_md5.hexdigest() 
	a = f'{result} = {word_hash}\n'
	print(colored(f'\n{a}', "green"))
	
	with open("ujik.txt", 'a') as f:
		f.write(a) 

def hash_sha1():
	sha1 = hashlib.sha1()
	encode_sha1 = hashlib.sha1(str(word_hash).encode('utf-8'))
	result = encode_sha1.hexdigest() 
	a = f'{result} = {word_hash}\n'
	print(colored(f'\n{a}', "green"))
	
	with open("ujik.txt", 'a') as f:
		f.write(a) 

def hash_sha224():
	sha224 = hashlib.sha224()
	encode_sha224 = hashlib.sha224(str(word_hash).encode('utf-8'))
	result = encode_sha224.hexdigest() 
	a = f'{result} = {word_hash}\n'
	print(colored(f'\n{a}', "green"))
	
	with open("ujik.txt", 'a') as f:
		f.write(a) 
	
def hash_sha256():
	sha256 = hashlib.sha256()
	encode_sha256 = hashlib.sha256(str(word_hash).encode('utf-8'))
	result = encode_sha256.hexdigest() 
	a = f'{result} = {word_hash}\n'
	print(colored(f'\n{a}', "green"))
	
	with open("ujik.txt", 'a') as f:
		f.write(a) 
	
	
def hash_sha384():
	sha384 = hashlib.sha384()
	encode_sha384 = hashlib.sha384(str(word_hash).encode('utf-8'))
	result = encode_sha384.hexdigest() 
	a = f'{result} = {word_hash}\n'
	print(colored(f'\n{a}', "green"))
	
	with open("ujik.txt", 'a') as f:
		f.write(a) 
	

def hash_sha512():
	sha512 = hashlib.sha512()
	encode_sha512 = hashlib.sha512(str(word_hash).encode('utf-8'))
	a = f'{result} = {word_hash}\n'
	print(colored(f'\n{a}', "green"))
	
	with open("ujik.txt", 'a') as f:
		f.write(a) 
