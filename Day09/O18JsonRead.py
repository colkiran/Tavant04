
import json

JFR = open("books.json", "r")
jsonFile = json.load(JFR)

for book in jsonFile['books']:
    for k, v in book.items():
        print(k, "=>", v)
    print("-" * 40)

