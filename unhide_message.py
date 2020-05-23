import bitarray
from PIL import Image
import base64
from Crypto import Random
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Hash import SHA3_256

password = input('Enter password: ')

hash_obj= SHA3_256.new(password.encode('utf-8'))
key=hash_obj.digest()
BS=16

def decrypt(enc):
    unpad = lambda s: s[:-ord(s[-1:])]

    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return unpad(base64.b64decode(cipher.decrypt(enc[AES.block_size:])).decode('utf8'))

image = Image.open("encoded.png")

extracted = ''

pixels = image.load()
# Iterate over pixels of the first row
for x in range(0, image.width):
    r, g, b = pixels[x, 0]
    r_bit = bin(r)[2:]
    if (len(r_bit) < 8):
        r_bit = "0" * (8 - len(r_bit)) + r_bit
    g_bit = bin(g)[2:]

    if (len(g_bit) < 8):
        g_bit = "0" * (8 - len(g_bit)) + g_bit
    b_bit = bin(b)[2:]
    if (len(b_bit) < 8):
        b_bit = "0" * (8 - len(b_bit)) + b_bit
    # Store LSB of each color of each pixel

    extracted += r_bit[-4]
    extracted += r_bit[-3]
    extracted += g_bit[-4]
    extracted += g_bit[-3]
    extracted += b_bit[-4]
    extracted += b_bit[-3]

chars = []
z = int(len(extracted) / 8)
length=''
answer = ''
flag=0
start=0
for i in range(z):
    byte = extracted[i * 8:(i + 1) * 8]
    aaa = int(''.join([str(bit) for bit in byte]), 2)
    if flag==0:
        if chr(aaa).isalpha():
            length=int(answer)
            flag=1;
            start=i
            break
    answer += chr(aaa)

ba = bitarray.bitarray()
ba.frombytes(str(length).encode('utf-8'))
bit_array = [int(i) for i in ba]
bits=len(bit_array)
strlength=len(str(length))
for i in range(bits,bits+length,8):
    byte = extracted[i:i+8]
    aaa = int(''.join([str(bit) for bit in byte]), 2)
    answer += chr(aaa)



ans=extracted[bits: bits+length]

encyptedMessage=answer[strlength:]
decryptedMessage=decrypt(encyptedMessage)
print('Secret Message is '+decryptedMessage)
