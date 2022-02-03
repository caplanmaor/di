# Create a python program that encrypts and decrypts messages with ceasar cypher, 
# the user entries the program, and then the program asks him if he wants to encrypt or decrypt, 
# and then execute encryption/decryption on a given message and a given shift.
text = input("type the text you want to encrypt: ")
shift = input("choose your shift for exmaple -3 or +1: ")
cypher_text = ""
for letter in text:
    cypher_text += chr(ord(letter) + int(shift))
print(cypher_text)
shift = input("now lets decrypt your message, choose the opposite shift (if you encrypted with -1 choose +1): ")
text = cypher_text
cypher_text = ""
for letter in text:
    cypher_text += chr(ord(letter) + int(shift))
print(cypher_text)