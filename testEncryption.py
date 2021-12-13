import sys
#from Crypto.PublicKey import RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import urllib.parse
import base64
from os import path

def encrypt(message, public_key_pem_path):
    public_key_path = 'c:\\temp\\public_key_test.pem'
    public_key = RSA.importKey(open(public_key_path, 'r').read())
    
    #create an RSA object using the public key 
    rsa_object = PKCS1_v1_5.new(public_key)
    cipher_text = rsa_object.encrypt(message.encode())
    #cipher_text = base64.b64encode(cipher_text)
    return cipher_text
def decrypt(message, private_key_pem_path):
    private_key_path = 'c:\\temp\\private_key_test.pem'
    private_key = RSA.importKey(open(private_key_path, 'r').read())
    rsa_object = PKCS1_v1_5.new(private_key)
    print("starting decrypt.")
    print("received messages as {} ... {}".format(type(message), message))
    #encrypt_byte = base64.b64decode(message.encode())
    #encrypt_byte = base64.b64decode(message.decode())
    #print ("encrypt_byte is : {} .... {} ... {}".format(type(encrypt_byte), len(encrypt_byte), encrypt_byte))
    #decipher_text = rsa_object.decrypt(message, "error")
    #decipher_text = base64.b64encode(decipher_text)
    encrypt_byte = message
    #the length of the cipher string can't be bigger than
    # the key size / 8
    allowed_length = 256
    my_length = len(encrypt_byte)
    if my_length < 256:
        decipher_text = rsa_object.decrypt(encrypt_byte, "failure")
    else:
        offset = 0
        res = []
        while my_length - offset > 0:
            if my_length - offset > allowed_length:
                res.append(rsa_object.decrypt(encrypt_byte[offset: offset + allowed_length], 'failure'))
            else:
                res.append(rsa_object.decrypt(encrypt_byte[offset:], 'failure'))
            offset += allowed_length
        decrypt_byte = b''.join(res)
    decipher_text = decrypt_byte.decode()
    return decipher_text
def generate_keys(key_size):
    key_pair = RSA.generate(2048)
    with open("c:\\temp\\private_key_test.pem", "wb") as f:
        f.write(key_pair.exportKey('PEM'))
        f.close()
    
    pubkey = key_pair.publickey()
    
    with open("c:\\temp\\public_key_test.pem", "wb") as f:
        f.write(pubkey.exportKey('OpenSSH'))
        f.close()
    
if __name__== '__main__':
    key_size = 1024
    generate_keys(key_size)
    print("-----------------RSA ENCRYPTION-------------------")
    plain_text = input("enter the plain text to encrypt :")
    print()
    cipher_text = encrypt(plain_text, "nothing")
    print("Cipher Text is: {}".format(cipher_text))
    print()
    plain_text = decrypt(cipher_text, "nothing")
    print("Plain Text is :{}".format(plain_text))
    