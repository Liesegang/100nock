# 09

import random

print("# 09")

def typoglycemia(s):
	r = []
	for w in s.split(" "):
		if len(w) > 4:
			t = list(w[1:])
			random.shuffle(t)
			r.append("".join([w[0]] + t))
		else:
			r.append(w)
	return " ".join(r)

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

r = typoglycemia(s)

print(r)