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

#byte array goes here
byte_str = 

#result after decryption
res = ''

for item in byte_str:
    for x in map_table:
        if x.getEncrypt() == item:
          res += '{}'.format(chr(x.getValue()))
          print('Item: {}, Decrypted: {}'.format(item , x.getValue()))


print(res)