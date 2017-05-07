# 11

print("# 11")

import s2_lib as s2

output_name = "r11.txt"

with open(s2.title) as source:
	with open(output_name, mode="w") as output:
		for line in source:
			output.write(line.replace("\t", " "))

s2.show_file(output_name)

com1 = "sed -e 's/\t/ /g' {}".format(s2.title)
s2.exec_command(com1)

com2 = "cat {} | tr '\t' ' '".format(s2.title)
s2.exec_command(com2)

com3 = "expand -t 1 {}".format(s2.title)
s2.exec_command(com3)