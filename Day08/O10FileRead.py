
FL = open("data.txt", "r")

# st = FL.read()               # will entire content of the file
# st = FL.read(1500)               # will read that specific number of bytes

# st = FL.readline()            # will read one line at a time
# st = FL.readline(450)            # can read what ever is there in the buffer (1 line or paragraph)
# st = FL.readlines()             # will read all the line in the file and store it in a list
# for line in FL.readlines():
#     print(line)

st = FL.readlines(865)
print(st)

FL.close()

