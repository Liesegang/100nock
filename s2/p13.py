# 13

print("# 13")

import s2_lib as s2

output_name = "r13.txt"

with open("col1.txt") as source1:
	with open("col2.txt") as source2:
		with open(output_name, "w") as output:
			for col1, col2 in zip(source1, source2):
				output.write(col1.strip() + "\t" + col2)

s2.show_file(output_name)

com = "paste col1.txt col2.txt"
s2.exec_command(com)