
FL = open("EMP.csv", "r")

gen = {}
des = []
dep = []
sal = 0
for line in FL.readlines():

    g = line.split(",")[2]
    ds = line.split(",")[3]
    dp = line.split(",")[4]

    if g not in gen:
        gen[g] = 1
    else:
        gen[g] += 1

    if ds not in des:
        des.append(ds)

    if dp not in dep:
        dep.append(dp)

    sal += int(line.split(",")[5])

FL.close()

print(f"Gender :{gen}")
print(f"Designations :{des}")
print(f"Department :{dep}")
print(f"Salary :{sal}")