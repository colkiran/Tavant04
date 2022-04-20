
print("items".center(40, "-"))
emp = {
    'emp1' :{'name': 'Jack', 'age': 28, 'desig': 'BDE', 'dept': 'MKT', 'sal': 85000},
    'emp2' :{'name': 'Jane', 'age': 26, 'desig': 'SD', 'dept': 'IT', 'sal': 65000},
    'emp3' :{'name': 'steve', 'age': 32, 'desig': 'MGR', 'dept':'Finance', 'sal': 120000}
}

print(f"emp :{emp}")
print("-" * 40)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" * 40)
for ky, info in emp.items():
    print(ky)
    print("-----")
    for k, v in info.items():
        print(k, "=>", v)
    print()

print("update".center(40, "-"))

emp1 = {'name': 'Jack', 'age': 28, 'desig': 'BDE', 'dept': 'MKT'}
emp2 = {'name': 'Jane', 'age': 26, 'desig': 'SD', 'sal': 65000}
print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

emp1.update(emp2)
print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("clear".center(40, "-"))
emp1 = {'name': 'Jack', 'age': 28, 'desig': 'BDE', 'dept': 'MKT'}
print(f"emp1 :{emp1}")

emp1.clear()
print(f"emp1 :{emp1}")
