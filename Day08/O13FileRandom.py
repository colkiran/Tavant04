
FL = open("data.txt", "rb")                 # read and binary

pos = FL.tell()

print(f"Position :{pos}")

pos = FL.seek(250, 0)

print(f"Position :{pos}")

FL.read(35)

pos = FL.tell()

print(f"Position :{pos}")

pos = FL.seek(100, 1)

print(f"Position :{pos}")

pos = FL.seek(100, 2)

print(f"Position :{pos}")

pos= FL.seek(-368, 2)

print(f"Position :{pos}")

FL.close()