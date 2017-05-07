# 18

print("# 18")

import s2_lib as s2

contents = []

with open(s2.title) as source:
	contents = source.readlines()

contents.sort(key=lambda x: float(x.split("\t")[2]))

for line in contents:
	print(line, end="")

com = "sort {} --key=3,3 --numeric-sort".format(s2.title)
s2.exec_command(com)