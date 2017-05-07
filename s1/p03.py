# 03

print("# 03")

r = []
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
for w in s.split(" "):
	r.append(len(w.strip(",.")))

print(*r)