from des import Cipher as DES, random_key, random_message

des = DES(random_key())
message = random_message()
ciphertext = des.encrypt(message)
plaintext = des.decrypt(ciphertext)
print(plaintext == message)  # should be True