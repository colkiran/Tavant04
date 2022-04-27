
import re

st = "good blood bad blood"

# recalling the second grouping, and the data also should be the same

res = re.search(r'(\w+)\s(\w+)\s(\w+)\s(\2)', st)

if res:
    print("Match Found.....")
    print(res.group(0))
    print(res.group(1))
    print(res.group(2))
    print(res.group(3))
    print(res.group(4))
else:
    print("Match not Found.....")
