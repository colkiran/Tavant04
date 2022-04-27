
import re

# res = re.search(r'\w+', st)
# res = re.search(r'\W+', st)
# res = re.search(r'\s+', st)
# res = re.search(r'\S+', st)
# res = re.search(r'\d+', st)
# res = re.search(r'\D+', st)
# res = re.search(r'(\bc\w+)', st, re.I)
# res = re.search(r'(\Bc\w+)', st, re.I)
# res = re.search(r'(\Athe)', st)
# res = re.search(r'(dog\Z)', st)

st = "the quick brown fox jumps over the lazy dog"

res = re.search(r'(dog\Z)', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found.....")

