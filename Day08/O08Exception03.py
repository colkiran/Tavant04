
class TooYoung(Exception):
    pass

class TooOld(Exception):
    pass

class TooTiny(Exception):
    pass

age = 16
try:
    if age <= 10:
        raise TooTiny("Too little guy to choose a leader....")
    elif age < 18:
        raise TooYoung("You are still young and cannot cast your vote.....")
    elif age > 100:
        raise TooOld("You are too old to choose the right leader.......")
    else:
        print("You can cast your valuable votes......")
except TooTiny as t:
    print(t)
except TooYoung as y:
    print(y)
except TooOld as o:
    print(o)

finally:

    print("completed the process of voting......")
