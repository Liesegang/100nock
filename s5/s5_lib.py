# s5_lib

source = "neko.txt.cabocha"

class Morph:
    def __init__(self, surface, base, pos, pos2):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos2 = pos2
    def __repr__(self):
    	return "表層形: {},\t基本形: {},\t品詞: {},\t品詞細分類1: {}".format(self.surface, self.base, self.pos, self.pos2)