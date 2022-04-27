
import re

st = "the quick brown fox jumps over the lazy dog"

res = re.search(r'(\bj\w+)', st)

if res:
    print("Match Found.....")
    # point out the starting point where the regex started matching the string
    print(f"Rejected String :{st[:res.start()]}")
    print(f"Matched String  :{res.group(0)}")
    print(f"Yet to Checked  :{st[res.end():]}")
else:
    print("Match not Found......")
