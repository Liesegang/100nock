# 15

print("# 15")

import sys
import s2_lib as s2

contents = ""
with open(s2.title) as source:
	contents = source.read().split("\n")

if len(sys.argv) > 1:
	N = int(sys.argv[1])
else:
	N = 10

line_number = len(contents)

for i in range(line_number - N - 1, line_number):
	print(contents[i])

com = "tail -n {} {}".format(str(N), s2.title)
s2.exec_command(com)