#try:

handle = open("fileName.txt", "w")
handle.write("This is the first row !\n")

handle.close()

# Edit the file use "a"
handle = open("fileName.txt", "a")
handle.write("And this is another row\n\n")
handle.write("A good try")
handle.close()

# Read file (default : read)
# Print file content
handle = open("fileName.txt")
file_content = handle.read()
print("File content:\n", file_content)
handle.close()

# Count number of rows
handle = open("fileName.txt")
count = 0
for i in handle:
    count += 1

handle.close()
print("This file includes ", count, " rows")

# read by lines
handle = open("fileName.txt")
read_content = handle.readlines()
handle.close()
# print second line
print(read_content[1])


#except IOError:
#print("Error: can\'t find or read data")
#else:
#handle = open("fileName.txt")
#handle.close()
#print("Just open a file for you, please try again")
