import json
from string import ascii_lowercase
class Rotor:
    def __init__(self, mapping, offset = 0):
        # set initial offset
        self.rotations = 1
        self.mapping = mapping
        self.initial_offset = offset
        self.reset()
        # for encryption
        self.forward_mapping = dict(zip(self.alphabet, mapping.lower()))
        # for decryption
        self.reverse_mapping = dict(zip(mapping.lower(), self.alphabet))
    def reset(self):
        self.alphabet = ascii_lowercase
        self.rotate(self.initial_offset)
        self.rotations = 1
    def rotate(self, turns=1):
        self.alphabet = self.alphabet[turns:] + self.alphabet[:turns]
        self.rotations += turns
    def encrypt(self, character):
        self.forward_mapping = dict(zip(self.alphabet, self.mapping.lower()))
        return self.forward_mapping[character]

    def decrypt(self, character):
        self.reverse_mapping = dict(zip(self.mapping.lower(), self.alphabet))
        return self.reverse_mapping[character]
class Reflector:
    def __init__(self, mapping):
        self.mapping = dict(zip(list(ascii_lowercase), mapping[::-1]))
        for x in self.mapping:
            y = self.mapping[x]
            if x != self.mapping[y]:
                raise ValueError("Mapping for {0} and {1} is invalid".format(x, y))
    def reflect(self, character):
        return self.mapping[character]
# class enigma:
    # def __init__(self, alpha, beta, gamma):
mirror = Reflector('abcdefghijklmnopqrstuvwxyz')
print(mirror.reflect('s'))

alpha = Rotor('DMTWSILRUYQNKFEJCAZBPGXOHV', 1)
beta = Rotor('HQZGPJTMOBLNCIFDYAWVEUSRKX', 2)
gamma = Rotor('UQNTLSZFMREHDPXKIBVYGJCWOA', 3)
message = 'attack'
listmsg = list(message)
print(listmsg)
encoded = ''

for char in listmsg:

    buffer = str(alpha.encrypt(char))
    print(buffer)
    alpha.rotate(1)
    # check if alpha has rotated 1 full revolution
    if (alpha.rotations % 26) == 0:
        beta.rotate(1) # rotate beta
    buffer = str(beta.encrypt(buffer)) 
    print(buffer)
    # # check if beta has rotated 1 full revolution
    # if (beta.rotations % 26) == 0:
    #    gamma.rotate(1) # rotate gamma
    # buffer = str(gamma.encrypt(buffer))
    # print(buffer)
    # reflector
    buffer = mirror.reflect(buffer)
    # route it back the rotors
    # buffer = str(gamma.encrypt(buffer))
    buffer = str(beta.decrypt(buffer))
    buffer = str(alpha.decrypt(buffer))
    encoded += buffer
print('Encoded message: ' + encoded)    

alpha.reset()
beta.reset()
gamma.reset()
decoded = ''
# decrypt
for char in encoded:
#    decoded += str(alpha.decrypt(mirror.reflect(char)))
#    print(decoded)
#    alpha.rotate(1)
        

    buffer = str(alpha.decrypt(char))
    print(buffer)
    alpha.rotate(1)
    # check if alpha has rotated 1 full revolution
    if (alpha.rotations % 26) == 0:
        beta.rotate(1) # rotate beta
    buffer = str(beta.decrypt(buffer)) 
    print(buffer)
    # # check if beta has rotated 1 full revolution
    # if (beta.rotations % 26) == 0:
    #     gamma.rotate(1) # rotate gamma
    # buffer = str(gamma.decrypt(buffer))
    # print(buffer)
    # reflector
    buffer = mirror.reflect(buffer)
    # route it back the rotors
    # buffer = str(gamma.decrypt(buffer))
    buffer = str(beta.encrypt(buffer))
    buffer = str(alpha.encrypt(buffer))
    decoded += buffer
print('Decoded message: ' + decoded)