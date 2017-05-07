# 16

print("# 16")

import math
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

file_name = "r16_{}.txt"

for i in range(0, math.ceil(line_number / N)):
	with open(file_name.format(str(i)), mode="w") as output:
		for j in range(i * N, min((i + 1) * N, line_number)):
			output.write(contents[j] + "\n")

for i in range(0, math.ceil(line_number / N)):
	s2.show_file(file_name.format(str(i)))

com = "split -l {} {} r16m_".format(str(N), s2.title)
s2.exec_command(com)