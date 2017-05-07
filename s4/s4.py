import collections
import matplotlib.pyplot as plt


# 30

print("# 30")

def parse_line():
    with open("neko.txt.mecab") as f:
        r = []
        for line in f:
            if line == "EOS\n":
                yield r
                r = []
            else:
                c = line.split("\t")
                c_res = c[1].split(",")

                item = {
                    'surface': c[0],
                    'base': c_res[6],
                    'pos': c_res[0],
                    'pos2': c_res[1],
                }
                r.append(item)

lines = parse_line()

data = []

for l in lines:
    data.append(l)

# 31

print("# 31")

r = []

for l in data:
    for w in l:
        if w['pos'] == '動詞':
            r.append(w['surface'])

# 32

print("# 32")

s = []

for l in data:
    for w in l:
        if w['pos'] == '動詞':
            s.append(w['base'])


# 33

print("# 33")

r_33 = []

for l in data:
    for w in l:
        if w['pos'] == '名詞' and w['pos2'] == 'サ変接続':
            r_33.append(w['surface'])

# 34

print("# 34")

r_34 = []

for l in data:
    if len(l) > 2:
        for i in range(0, len(l) - 2):
            if l[i]['pos'] == '名詞' and l[i+1]['surface'] == 'の' and l[i+2]['pos'] == '名詞':
                r_34.append(l[i]['surface'] + 'の' + l[i+2]['surface'])


# 35

print("# 35")

r_35 = []

for l in data:
    list_of_num = []
    for w in l:
        if w['pos'] == '名詞':
            list_of_num.append(w['surface'])
        else:
            if len(list_of_num) >= 2:
                r_35.append(list_of_num)
                list_of_num = []
            else:
                list_of_num = []
    else:
        if len(list_of_num) >= 2:
            r_35.append(list_of_num)


# 36

print("# 36")

r_36 = collections.Counter()

for l in data:
    r_36.update([w['base'] for w in l])

r_36 = r_36.most_common()


# 37

print("# 37")

print([i[0] for i in r_36[0:10]])

plt.bar([i for i in range(0, 10)], [i[1] for i in r_36[0:10]], tick_label=[i[0] for i in r_36[0:10]], align='center')
plt.grid(True)

plt.show()


# 38

print("# 38")

plt.hist([i[1] for i in r_36], bins=50, range=(0,50))

plt.show()


# 39

print("# 39")

x = [i for i in range(1, len(r_36) + 1)]
y = [i[1] for i in r_36]

plt.scatter(x, y)
plt.xscale('log')
plt.yscale('log')

plt.show()












