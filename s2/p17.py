# 17

print("# 17")

import s2_lib as s2

content = ""
r = ""
strings = set()

with open(s2.title) as source:
	for line in source:
		col1 = line.split("\t")[0]
		strings.add(col1 + "\n")

r = "".join(strings)

print(r)

com = "cut -f1 {} | sort | uniq".format(s2.title)
s2.exec_command(com)