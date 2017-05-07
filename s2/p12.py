# 12

print("# 12")

import s2_lib as s2

file1_name = "col1.txt"
file2_name = "col2.txt"

with open(s2.title) as source:
	with open(file1_name, "w") as f1:
		with open(file2_name, "w") as f2:
			for line in source:
				cols = line.split("\t")
				f1.write(cols[0] + "\n")
				f2.write(cols[1] + "\n")

s2.show_file("col1.txt")
s2.show_file("col2.txt")

com1 = "cut -f1 {}".format(s2.title)
s2.exec_command(com1)

com2 = "cut -f2 {}".format(s2.title)
s2.exec_command(com2)