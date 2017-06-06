# 42

print('# 42')

import p41

def show_dependency(sentence):
    for chunk in sentence:
        if chunk.dst != -1:
            print(str(chunk), '\t', str(sentence[chunk.dst]))

for sentence in p41.chunks_in_line():
    show_dependency(sentence)

