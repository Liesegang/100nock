# 06

print("# 06")

def ngram(s,n):
	r = []
	for i in range(0, len(s) - n + 1):
		r.append(s[i:i+n])
	return r

s1 = "paraparaparadise"
s2 = "paragraph"

X = set(ngram(s1, 2))
Y = set(ngram(s2, 2))

print("和集合:", X | Y)
print("積集合:", X & Y)
print("差集合:", X - Y)