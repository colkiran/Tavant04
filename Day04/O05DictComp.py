
players = {
    'sachin': [290, 350, 410, 320, 450],
    'sehwag': [180, 480, 450, 430, 400],
    'sourav': [190, 330, 300, 275, 250],
    'rahul': [340, 235, 390, 302, 150],
    'yuvraj': [120, 290, 185, 150, 200],
    'laxman': [175, 259, 375, 199, 140]
}
print(f"players: {players}")

print("-" * 40)

print(players['sachin'])

print(sum(players['sachin']))

plyr_scr = {k for k in players}
print(f"plyr_scr :{plyr_scr}")

plyr_scr = {k: v for (k, v) in players.items()}
print(f"ply_scr :{plyr_scr}")

plyr_scr = {k: sum(v) for (k, v) in players.items()}
print(f"ply_scr :{plyr_scr}")

plyr_scr = {k: (lambda score: sum(score) / len(score))(v)
                    for k, v in players.items()}
print(f"plyr_scr :{plyr_scr}")

print("-" * 40)

ply1 = [score for score in players.values()]
print(ply1)

print("-" * 40)

ply1 = [scr for score in players.values() for scr in score]
print(f"ply1 :{ply1}")

print("-" * 40)
ply1 = [scr for score in players.values() for scr in score if scr >= 200]
print(f"ply1 :{ply1}")

print("-" * 40)
ply2 = [str(scr) for score in players.values() for scr in score if scr >= 200]
print(f"ply2 :{ply2}")

grt200 = {name: [scr for scr in score if scr >= 200]
                for name, score in players.items()}
print(f"grt200 :{grt200}")
