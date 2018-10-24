from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
public_key = key.publickey()

encrypted = public_key.encrypt('encrypt this message'.encode('utf-8'), 32)
decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

private_key = key.exportKey('PEM')
public_key1 = key.publickey().exportKey('PEM')
print(private_key)
print(public_key1)
print(decrypted.decode("utf-8"))
print(type(encrypted))