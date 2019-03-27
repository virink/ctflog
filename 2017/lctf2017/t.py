import re

pattern = re.compile(r'^(xdsec)((?:###|*))$', re.I)
sss = 'xdsec'
print(pattern.search(sss))
