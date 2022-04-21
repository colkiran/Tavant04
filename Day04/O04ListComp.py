
fruits = [
    ('apple', 280),
    ('orange', 80),
    ('grapes', 120),
    ('pine', 65),
    ('watermelon', 90),
    ('gauva', 70),
    ('strawberry', 350)
]

prices = ["fruit" for fruit in fruits]
print(f"prices :{prices}")

prices = [fruit for fruit in fruits]
print(f"prices :{prices}")

prices = [fruit[0] for fruit in fruits]
print(f"prices :{prices}")

prices = [fruit[1] for fruit in fruits]
print(f"prices :{prices}")

prices = [fruit[1] * 0.9 for fruit in fruits]
print(f"prices :{prices}")

prices = [fruit[1] * 0.75 for fruit in fruits]
print(f"prices :{prices}")

prices = [(fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits
          if fruit[1] > 100]
print(f"prices :{prices}")

print("-" * 40)

sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

words = [word for word in sentence.split()]
print(f"words :{words}")

words = [word for word in sentence.split() if word != "the"]
print(f"words :{words}")

words = [(word, len(word)) for word in sentence.split() if word != "the"]
print(f"words :{words}")

print("-" * 40)

l = [35.7, 89.3, -25.9, 56.1, -63.5, -89.4, 92.8, -103,5]
print(f"l :{l}")

# print all positive numbers from the list
res = [n for n in l if n > 0]
print(f"res :{res}")

print("-" * 40)
squares = [i ** 2 for i in range(1, 11)]
print (f"squares :{squares}")

print("-" * 40)
plyrs = ['sachin', 'fedrer', 'messi', 'sindhu', 'tyson', 'jordan']
games = ['cricket', 'tennis', 'football', 'badmiton', 'boxing', 'basketball']

combine = [(plr, gm) for plr in plyrs for gm in games]
print(f"combination :{combine}")

print("-" * 40)
combine = list(zip(plyrs, games))
print(f"combination :{combine}")

