

import re
st = "26/12/1998"
# Backtraking - recall a regular expression - it also expects the data to be the same
res = re.search(r'([0-2][1-9]|[1-3][0-1])(/|-)(0[1-9]|1[0-2])(\2)([1-9][0-9]{3})', st)
if res:
    print(res.group(0))
    print("Match found....")
else:
    print('Match not found......')