
class Player:

    def __init__(self):             # constructor
        print("Player Initialized....")

    def get_runs(self):
        print("runs scored......")

    def __del__(self):
        print("Player deleted.....")


sachin = Player()
sourav = Player()
print("-" * 40)

sachin.__init__()
print("-" * 40)
sachin.get_runs()
sourav.get_runs()
print("-" * 40)
del sachin
print("-" * 40)

# sachin.get_runs()

