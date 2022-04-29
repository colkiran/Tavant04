
from datetime import datetime
import dateutils

dt = datetime.now()
print(f"dt :{dt}")

print("-" * 40)
print("Day :", dt.strftime("%a"))
print("Day :", dt.strftime("%A"))

print("-" * 40)
print("Month :", dt.strftime("%b"))
print("Month :", dt.strftime("%B"))



print("-" * 40)
print("Date :", dt.strftime("%d"))
print("Date :", dt.strftime("%D"))
print("Date :", dt.strftime("%x"))


print("-" * 40)
print("Year :", dt.strftime("%y"))
print("Year :", dt.strftime("%Y"))


print("-" * 40)
print("Time :", dt.strftime("%T"))
print("Time :", dt.strftime("%X"))


print("-" * 40)
dt1 = dt.strftime("%d-%m-%y")
print(f"dt1 :{dt1}")

print("-" * 40)
dt2 = dt.strftime("%d-%m-%Y")
print(f"dt2 :{dt2}")

print("-" * 40)
dt3 = "Friday, April 29, 2020"
print(f"dt3 :{dt3}")
print(type(dt3))

print("-" * 40)
dt4 = "31/10/2022"
print(f"dt4: {dt4}")
print(type(dt4))

print("-" * 40)
actdt1 = datetime.strptime(dt3, "%A, %B %d, %Y")
print(actdt1)


# dt4 = "31/10/2020"
print("-" * 40)
actdt2 = datetime.strptime(dt4, "%d/%m/%Y")
print(actdt2)

print("-" * 40)
print(f"actdt1 :{actdt1}")
print(f"actdt2 :{actdt2}")

print("-" * 40)
print("Difference :", actdt2 - actdt1)

print()
print("dateutils".center(40, "-"))

print("Difference in days :", dateutils.days(actdt2, actdt1))

print("Difference in weeks :", dateutils.weeks(actdt2, actdt1))

print("difference in months :", dateutils.months(actdt2, actdt1))

print("difference in years :", dateutils.years(actdt2, actdt1))
