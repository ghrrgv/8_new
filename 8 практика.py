from itertools import *

cnt = 0

for i in permutations('МАСЛО', r = 5):
    if i[0] != 'С' and 'МО' not in ''.join(i):
        cnt += 1
print(cnt)123