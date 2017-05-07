# 00

print("# 00")

r = ""
s = "stressed"
r = s[::-1]
print(r)


# 01

print("# 01")

r = ""
s = "パタトクカシー"
r = s[::2]
print(r)


# 02

print("# 02")

r = ""
s1 = "パトカー"
s2 = "タクシー"
for a,b in zip(s1,s2):
	r += a + b
print(r)


# 03

print("# 03")

r = []
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
for w in s.split(" "):
	r.append(len(w.strip(",.")))
print(*r)


# 04

print("# 04")

r = {}
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
for i, w in enumerate(s.split(" ")):
	if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
		r[w[0:1]] = i
	else:
		r[w[0:2]] = i
print(r)


# 05

print("# 05")

def ngram(s,n):
	r = []
	for i in range(0, len(s) - n + 1):
		r.append(s[i:i+n])
	return r

s = "I am an NLPer"
r1 = []
r2 = []

r1 = ngram(s, 2)
r2 = ngram(s.split(" "), 2)
print(r1)
print(r2)


# 06

print("# 06")

s1 = "paraparaparadise"
s2 = "paragraph"

X = set(ngram(s1, 2))
Y = set(ngram(s2, 2))

print("和集合:", X | Y)
print("積集合:", X & Y)
print("差集合:", X - Y)


# 07

print("# 07")

def template(x, y, z):
	return "{}時の{}は{}".format(x, y, z)

print(template(x=12, y="気温", z=22.4))


# 08

print("# 08")

def cipher(s):
	r = []
	for a in s:
		if a.isalnum():
			r.append(chr(219 - ord(a)))
		else:
			r.append(a)
	return "".join(r)

r = cipher("difficult sentence")
print(r)
print(cipher(r))


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
print(typoglycemia(s))

