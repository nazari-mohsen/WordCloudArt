from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from Crypto.PublicKey.RSA import  importKey
from Crypto.Cipher import PKCS1_OAEP
# from cloud.settings import public_key, private_key

private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAwyAW3JTgYZQ/fczuND1EII7qSxDVCv/8FDyJe/OlpkoTepIz\nKgdW1ku9z3nZaUtZv1xk42SHG/OLc5prXMreiGjv8IO/cQ2CiZTWcZCW3PgkC8F+\n4RXShx52+5XQhqgvQyC4XEh/0ZGu11slJ6crQBugUcozYirYUVF3e5kipGXRzpLu\nk9I0pHHUidlplLiD7dC/cEpwoQw/ACNHEw3K4W9a0SxwqLwI/BYNHRTA0ee8pF85\nAT0p6CQod4Aihu9/zCrD0EhDVduHOccHsIylJ9moJWu7URGLjPMiiAdt1xpUt8oo\nD9sr4+FJjw76+ZIoONQYAzGL1JBJqwTB5eE7fwIDAQABAoIBADR3z/3vYGiMuwfi\nT5knckbI9zJJK+hBzjBI2PVGHmBZIeS/JFfkUlLcWgVMsAvysYbV2uEUWopHElP7\nDWyNton6oa5MVvGY3uWM6p7t8MspRFQO60WuHwarR/Y9oi1bUx4bUceqzQf2wwtw\nnEyN1IDwDMuBchCvEazIGbdYBasrp6y3vZc7Q47QZ9PgfjoS7EU1MesL26iOoSgU\ntwOqdJkEUgjwj5wIwj7oyggH5d29GjCm0DPHYn6Ht48W5612siqChl+ZZIpvBOFc\nyIuY8mjsWjHtNstuF/iUINOVqHA0zIvPvMoAxHPT6dHuFb+vSAyxK8tHFbbuNk7E\ndfmVwIECgYEA3oFAvdBNh+WGhPl8/ffEP5dgAo8xwqFJSdUM+vXia2Fd/yavU0zR\nQd5Rf+ikXyNzVMPJ2u0X1NJ6oypII1eFIaRtSzBjPFa5/iQcb9vpcFyIpsrpaI41\nJDhCXpzRuwaW9NuArkgG/czYcp0Ks1zT7pksTNPA5vHOWtIkT5eRqP8CgYEA4H+z\nlriYnbHeB/qE0XA1jZKyyir54xEnP4kfGWb+2CV8kq7JjBMF6s5vm0MgbzJd1P/h\nr8TvzdkLswj6rqZr65fez+SeEZizeaqDgoV7C+rdcTTdLa+86SmPCQb/+k2jFT3W\nkuiZxKF0tPRqP6Pu9ZoWpCq2mTEAGsbaLLT57YECgYB8gxP5pFFelOC8FOkPLdFS\nTKFbjUopQhxDBsgmv+YedPQmzj0afkgzdfdhfoxM+QeXDaEts7O8UrRyDj0kGdvU\nQbEvfDpsD5QxVX/cUNHHIOEPhUksSzgNtrXdQCBVapCbISJXZNMUv8b4DE1qpa2r\nPWf+7hhqpDH3vNS4/XZzfQKBgAbL1uP5MqWTfOVA8ERm4Tgn+MGmC2qUWlvSCt75\n/z0L5XmLUQ6shMFW/on0vkaff7ezB2IK1DenGnOREgW3hAzdzCD/Csn9lXFZeCG7\naL4zngCPWSLI7y8f0vSzAYzSTN2Xwacw43bQbHgN7il/DPzibU0K/fwlP5uP6Yrw\n76ABAoGAIEG4MQZVa18ebQamC7RrJ5wqWN9MtnkHqoq/mhrDyJ7eNlsviF4VYQDE\nMRbO2PUQkWQZmggiDZ7zhLAUnNQuWzjv7HRxHDwEAUCiYm5oEZNaOeQhALXuEgtH\neOBhUZhCdQvAC0C25YHIjSzuJ9x5Ls3ddWNcB60Wyj2xhRLnxsY=\n-----END RSA PRIVATE KEY-----'
public_key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwyAW3JTgYZQ/fczuND1E\nII7qSxDVCv/8FDyJe/OlpkoTepIzKgdW1ku9z3nZaUtZv1xk42SHG/OLc5prXMre\niGjv8IO/cQ2CiZTWcZCW3PgkC8F+4RXShx52+5XQhqgvQyC4XEh/0ZGu11slJ6cr\nQBugUcozYirYUVF3e5kipGXRzpLuk9I0pHHUidlplLiD7dC/cEpwoQw/ACNHEw3K\n4W9a0SxwqLwI/BYNHRTA0ee8pF85AT0p6CQod4Aihu9/zCrD0EhDVduHOccHsIyl\nJ9moJWu7URGLjPMiiAdt1xpUt8ooD9sr4+FJjw76+ZIoONQYAzGL1JBJqwTB5eE7\nfwIDAQAB\n-----END PUBLIC KEY-----'


def Encrypt(message):
    publickey = importKey(public_key)
    encryptor = PKCS1_OAEP.new(publickey)
    encrypted = encryptor.encrypt(message.encode('utf-8'))
    return encrypted

def Decrypt(encrypted):
    key = importKey(private_key)
    decryptor = PKCS1_OAEP.new(key)
    decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))
    message = decrypted.decode()

    return message



# --------------- follow line enter in view ------------------
"""from .decrypte import Encrypt, Decrypt
from rest_framework.parsers import BaseParser
from rest_framework.decorators import api_view, permission_classes, parser_classes
class PlainTextParser(BaseParser):
    
    #Plain text parser.
    
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        
        #Simply return a string representing the body of the request.
       
        return stream.read()

@api_view(['POST'])
@permission_classes((AllowAny, ))
@parser_classes((PlainTextParser,))
def CreateUserAPIView(request):
    import base64
    # print(request.data)
    message = {"status": "Error"}
    # message = {"status": "ok"}
    # strm = "encrypt this message"
    # mn = Encrypt(strm)
    # print(mn)
    # encodebase64 = base64.b64encode(mn)
    # mn = b'du5QRBBygzUYWjSO9gPUOT3835AeaM+QXbqhBFqeBI99UFu4rz4KpU7kpieLC/lN4YCAF2yqvCQ5577YMUOEoz8n6YPWFanJjhWdeIAhHeiGVxyuJUrwJ6UMUod6V8kLPrno3Xu4eClPTaEhRxc/XU6X0O494oKVd3RSRPdl4UXjE+IN47YwVClVOtARg5QcXcQdm7f9gUZ3zB49/u6m/x9F3mEpEbE1TLwda2UXV9oabcfUxf9K4nPvoVbXFK27w7oT4bk3uErS4McrbPCSHiiwlc1pxMpR5g4hCJtIsuE6+umu17Yu/bMVrfOMr538CmvCzCpRjjw4LMdrENX5Mw=='
    # mn = request.data
    # decodebase64 = base64.b64decode(mn)
    # print(encodebase64)
    # print(decodebase64)
    # de = Decrypt(decodebase64)
    # de1 = Decrypt(request.data)
    # print(de)
    # print(de1)
    print(request.data)
    return Response(status=status.HTTP_200_OK)
    """
