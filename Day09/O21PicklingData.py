
import pickle

ply1 = {'id': 'P35', 'Name': 'Sachin Tendulkar', 'Sport': 'Cricker', 'age': 39}
ply2 = {'id': 'P28', 'Name' : 'Mike Tyson', 'Sport': 'Football', 'age': 45}

print(f"ply1 :{ply1}")
print(f"ply2 :{ply2}")

players = {}
players['ply1'] = ply1
players['ply2'] = ply2

print(f"Players :{players}")
FP = open("PlayersPickle", "ab")            # append and binary
pickle.dump(players, FP)
FP.close()

