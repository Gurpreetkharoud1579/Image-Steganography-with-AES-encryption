from PIL import Image
import bitarray
import base64
from Crypto.Random import get_random_bytes

from Crypto.Cipher import AES
from Crypto.Hash import SHA3_256

password = input('Enter password: ')

hash_obj= SHA3_256.new(password.encode('utf-8'))
key=hash_obj.digest()
BS=16
BS=16

def encrypt(raw):
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    raw = base64.b64encode(pad(raw).encode('utf8'))
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key,AES.MODE_CFB,iv)
    return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf8')

message = (input('Type your secret message :'))
#Convert the message into a array of bits
message=encrypt(message)
message=str(message)

ba = bitarray.bitarray()
ba.frombytes(message.encode('utf-8'))
bit_array = [int(i) for i in ba]



length=len(bit_array)
ba = bitarray.bitarray()
message=str(length)+message
ba.frombytes(message.encode('utf-8'))
bit_array = [int(i) for i in ba]





#Duplicate the original picture
im = Image.open("abc.png")
im.save("encoded.png")

im = Image.open("encoded.png")
width, height = im.size
pixels = im.load()

i = 0
for x in range(0,width):
    r,g,b = pixels[x,0]
    #Default values in case no bit has to be modified
    new_bit_red_pixel = r
    new_bit_green_pixel = g
    new_bit_blue_pixel = b
    if i>len(bit_array):
        break
    if i<len(bit_array):
        #Red pixel
        r_bit = bin(r)[2:]
        if (len(r_bit) < 8):
         r_bit = "0" * (8 - len(r_bit)) + r_bit
        r_new_last_bit =  bit_array[i]
        new_bit_red_pixel = int(r_bit[:-4]+str(r_new_last_bit)+r_bit[5:],2)
        i += 1
        pixels[x, 0] = (new_bit_red_pixel, new_bit_green_pixel, new_bit_blue_pixel)
        r, g, b = pixels[x, 0]

    if i<len(bit_array):
        #Red pixel
        r_bit = bin(r)[2:]
        if (len(r_bit) < 8):
         r_bit = "0" * (8 - len(r_bit)) + r_bit
        r_new_last_bit =  bit_array[i]
        new_bit_red_pixel = int(r_bit[:-3]+str(r_new_last_bit)+r_bit[6:],2)
        i += 1
        pixels[x, 0] = (new_bit_red_pixel, new_bit_green_pixel, new_bit_blue_pixel)
        r, g, b = pixels[x, 0]



    if i<len(bit_array):
        #Green pixel
        g_bit = bin(g)[2:]
        if (len(g_bit) < 8):
            g_bit = "0" * (8 - len(g_bit)) + g_bit
        g_new_last_bit =  bit_array[i]
        new_bit_green_pixel = int(g_bit[:-4]+str(g_new_last_bit)+g_bit[5:],2)
        i += 1
        pixels[x, 0] = (new_bit_red_pixel, new_bit_green_pixel, new_bit_blue_pixel)
        r, g, b = pixels[x, 0]

    if i<len(bit_array):
        #Green pixel
        g_bit = bin(g)[2:]
        if (len(g_bit) < 8):
            g_bit = "0" * (8 - len(g_bit)) + g_bit
        g_new_last_bit =  bit_array[i]
        new_bit_green_pixel = int(g_bit[:-3]+str(g_new_last_bit)+g_bit[6:],2)
        i += 1
        pixels[x, 0] = (new_bit_red_pixel, new_bit_green_pixel, new_bit_blue_pixel)
        r, g, b = pixels[x, 0]

    if i<len(bit_array):
        #Blue pixel
        b_bit = bin(b)[2:]
        if (len(b_bit) < 8):
            b_bit = "0" * (8 - len(b_bit)) + b_bit
        b_new_last_bit =  bit_array[i]
        new_bit_blue_pixel = int(b_bit[:-4]+str(b_new_last_bit)+b_bit[5:],2)
        i += 1
        pixels[x, 0] = (new_bit_red_pixel, new_bit_green_pixel, new_bit_blue_pixel)
        r, g, b = pixels[x, 0]

    if i<len(bit_array):
        #Blue pixel
        b_bit = bin(b)[2:]
        if (len(b_bit) < 8):
            b_bit = "0" * (8 - len(b_bit)) + b_bit
        b_new_last_bit =  bit_array[i]
        new_bit_blue_pixel = int(b_bit[:-3]+str(b_new_last_bit)+b_bit[6:],2)
        i += 1
        pixels[x, 0] = (new_bit_red_pixel, new_bit_green_pixel, new_bit_blue_pixel)
        r, g, b = pixels[x, 0]


im.save('encoded.png')
print('Encoding Successful')

