# 14

print("# 14")

import sys
import s2_lib as s2

if len(sys.argv) > 1:
	N = int(sys.argv[1])
else:
	N = 10

with open(s2.title) as source:
	for i in range(0, N):
		print(source.readline(), end="")

com = "head -n {} {}".format(str(N), s2.title)
s2.exec_command(com)
