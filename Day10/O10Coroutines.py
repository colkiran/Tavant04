
def get_name(surname):
    print(f"surname is  {surname}")
    while True:
        name = yield
        print(f"received {name}")
        if surname in name:
            print(f"surname {surname} matched in {name}")

coObj = get_name("Pillai")
print(f"coObj :{coObj}")
coObj.__next__()

coObj.send("Virat Kholi")
coObj.send("Sachin Tendulkar")
coObj.send("Rahul Dravid")
coObj.send("Dhanraj Pillai")
