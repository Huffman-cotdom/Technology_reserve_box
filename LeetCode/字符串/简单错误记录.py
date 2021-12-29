import sys
from collections import defaultdict

data = map(lambda x: x.split('\\')[-1], sys.stdin.readlines())

errors = defaultdict(int)
result = list()

for d in data:
    name, line = d.strip().split()
    error = ' '.join([name[-16:], line])
    errors[error] += 1
    if errors[error] == 1:
        result.append(error)

for r in result[-8:]:
    print(r, errors[r])
