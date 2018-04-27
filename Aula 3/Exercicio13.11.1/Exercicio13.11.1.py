# Reads the ent.txt file and writes out.txt with the lines reversed

ent = open("ent.txt", "r")
# Creates a list of the file lines
list = ent.readlines()
ent.close()

# Invert list
size = len(list)
inverted_list = []
for i in range(size):
    inverted_list.append(list[size-i-1])

out = open("out.txt", "w")
# Write lines backwards
for line in inverted_list:
    out.write(line)
out.close()
print("The file has been successfully created")
