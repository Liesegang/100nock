# 41

print("# 41")

from s5_lib import Morph
import s5_lib as s5
from collections import defaultdict

class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
    def __str__(self):
        return "dst: {},\tsrcs: {},\t morphs:\n{}".format(self.dst, str(self.srcs), ",".join(['{' + str(m) + '}\n' for m in self.morphs]))
    def __repr__(self):
        return self.__str__()

def chunks_in_line():
    with open(s5.source) as source:
        c = []
        r = []
        srcs = defaultdict(list)
        key = -1
        dst = -1
        for line in source:
            if (line[0:2] == '* ' or line == 'EOS\n') and r:
                c.append(Chunk(r, dst, srcs[key]))
                r = []
            if line[0:2] == '* ':
                chunk_data = line.split(' ')
                key = int(chunk_data[1])
                dst = int(chunk_data[2][:-1])
                srcs[dst].append(key)
            elif line == 'EOS\n':
                yield c
                c = []
                srcs.clear()
            else:
                word = line.split('\t')
                prop = word[1].split(',')
                r.append(Morph(word[0], prop[6],prop[0], prop[1]))

r = []

for chunk in chunks_in_line():
    r.append(chunk)

print(str(r[3]))
