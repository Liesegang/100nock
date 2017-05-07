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

s = "difficult sentence"

r1 = cipher(s)
r2 = cipher(r1)

print(r1)
print(r2)