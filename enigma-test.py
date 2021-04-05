from string import ascii_lowercase
alphabet = ascii_lowercase
class Rotor:
    def __init__(self, mapping, window = 'a'):
        self.mapping = mapping
        self.reset()
        self.alphabet = alphabet
        self.forward_mapping = dict(zip(self.mapping,self.alphabet))
        self.reverse_mapping = dict(zip(self.alphabet,self.mapping))
        self.rotations = 0
    def reset(self):
        self.window
        self.alphabet = ascii_lowercase
        self.rotate(self.initial_offset) # change this line
        self.rotations = 0
    def rotate(self, turns=1):
        self.alphabet = self.alphabet[turns:] + self.alphabet[:turns]
        self.rotations += turns
    def forward(self, char):
        return self.forward_mapping[char]
    def backward(self, char):
        return self.reverse_mapping[char]
    



class Reflector:
    def __init__(self, mapping):
        self.mapping = dict(zip(list(ascii_lowercase), mapping[::-1]))
        for x in self.mapping:
            y = self.mapping[x]
            if x != self.mapping[y]:
                raise ValueError("Mapping for {0} and {1} is invalid".format(x, y))
    def reflect(self, character):
        return self.mapping[character]