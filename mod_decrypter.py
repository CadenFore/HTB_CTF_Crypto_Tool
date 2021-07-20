#before using you have to convert a hex string to a byte array, 
#this function then takes in that byte array as a string 
#and decrypts using modular multiplicitave inverse

class MapValue:

    def __init__(self, value, encrypt):
        self.value = value
        self.encrypt = encrypt
        self
    def getValue(self):
        return self.value
        
    def getEncrypt(self):
        return self.encrypt

#these values will change depending on the encryption used
def encrypted(value):
    return(123 * value + 18) % 256
    print(value)

map_table = []
for x in range(0,256):
    map_table.append(MapValue(x, encrypted(x)))

#byte array goes here, example input shown. 
byte_str = b'n\n\x93r\xecI\xa3\xf6\x93\x0e\xd8r?\x9d\xf6\xf6r\x0e\xd8\xd8\x9d\xc4\x93r"\xecr\x14\xd8\x9d\x1e\x0e5,\xe0\xaan\xc8+\xf6""{\xb7\x0e\x7f\xb75"I\xb7\xd8\x93\xc4\x93\xd8S\x9d\xec\x8f\xb7\x93]I\x0e\x7f\x9d"\xec\x89\xb7\xa3"\xec\x8f\xd8\x0e\x7f\x89!'

#result after decryption
res = ''

for item in byte_str:
    for x in map_table:
        if x.getEncrypt() == item:
          res += '{}'.format(chr(x.getValue()))
          print('Item: {}, Decrypted: {}'.format(item , x.getValue()))

#output example would show HTB(Flag found)
print(res)
