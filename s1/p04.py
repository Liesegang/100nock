# 04

print("# 04")

r = {}
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

for i, w in enumerate(s.split(" ")):
	if i + 1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
		r[w[0:1]] = i
	else:
		r[w[0:2]] = i

print(r)