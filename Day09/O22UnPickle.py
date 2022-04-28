
import pickle

PFR  = open("PlayersPickle", "rb")                  # rb = read and binary

plyr = pickle.load(PFR)

for ky, info in plyr.items():
    print(ky)
    print("-----")
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

PFR.close()

