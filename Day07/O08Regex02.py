
import re

lno = "LCNO-KAR-73-2010-9999"

res = re.search(r'LCNO-(KAR|KER|TND|APN|TEL|MAH|GOA)-([0-6][1-9]|[1-7][0-3])-'
                r'([2-9][0-9]{3})-((?!0000)[0-9]{4})$', lno)

if res:
    print("Match found")
    print(res.group(0))
else:
    print("match not found")