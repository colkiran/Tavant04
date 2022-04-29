
import os

# get the current working directory
print(os.getcwd())

# change the path to day09
os.chdir("C:\Training\PycharmProjects\Tavant04\Day09")
print(os.getcwd())

print("-" * 40)
# extract all files and folder from day09
files = os.listdir()

for file in files:
    if file.endswith(".py"):
        print(file, " : ", os.path.getsize(file), "bytes")


print("-" * 40)
print(os.cpu_count())