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