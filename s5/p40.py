# 40

print("# 40")

import s5_lib as s5

class Morph:
    def __init__(self, surface, base, pos, pos2):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos2 = pos2
    def __str__(self):
    	return "表層形: {},\t基本形: {},\t品詞: {},\t品詞細分類1: {}".format(self.surface, self.base, self.pos, self.pos2)


def morphs_in_line():
	with open(s5.source) as source:
		r = []
		for line in source:
			if line[0:2] == '* ':
				continue
			elif line == 'EOS\n':
				yield r
				r = []
			else:
				word = line.split('\t')
				prop = word[1].split(',')
				r.append(Morph(word[0], prop[6],prop[0], prop[1]))

r = []

for morphs in morphs_in_line():
	r.append(morphs)

for morph in r[3]:
	print(str(morph))