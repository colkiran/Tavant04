
import re

st = "the quick brown fox jumps over the lazy dog."

res = re.sub(r'f\w+','tiger', st)

print(f"res :{res}")
