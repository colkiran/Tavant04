
class Player:                       # pascal casing

    def get_runs(self):             # self - this pointer
        # print(self.__class__)
        print("runs scored...")

sachin = Player()
sachin.get_runs()
print("-" * 40)

print(type(sachin))
print("-" * 40)
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))
