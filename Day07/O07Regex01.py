"""
compile', 'copyreg', 'enum', 'error', 'escape', 'findall', 'finditer', 'fullmatch',
'functools', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub',
'subn', 'template'
"""
import re

# print(dir(re))
# st = "hello world"
# res = re.match(r'^hello', st)
# res = re.search(r'world$', st)
# res = re.search(r'b.t', st)
# res = re.search(r'ba*t', st)                    # * is applicable only for a
# res = re.search(r'ba?t', st)
# res = re.search(r'ba+t', st)
# res = re.search(r'ba{3}t', st)
# res = re.search(r'ba{3,}t', st)
# res = re.search(r'ba{3,8}t', st)
# res = re.search(r'b[a-zA-Z0-9]t', st)
# res = re.search(r'b[aeiou]t', st)
# res = re.search(r'b[^aeiou]t', st)
# res = re.search(r'b(oa|es)t', st)


st = "samplepy"

res = re.search(r'\.py$', st)

if res:
    print("Match found")
    print(f"res :{res}")
    print(res.group(0))                     # string that matched the regulax expression
else:
    print("match not found")