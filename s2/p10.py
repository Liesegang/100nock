# 10

print("# 10")

import s2_lib as s2

r = 0

with open(s2.title) as source:
	for line in source:
		r += 1

print(r)

s2.exec_command("wc {}".format(s2.title))