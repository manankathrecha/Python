#Aim: The output order should correspond with the input order of appearance of the word.
from collections import Counter
N = int(input())
LIST = []
for i in range(N):
    LIST.append(input().strip())
COUNT = Counter(LIST)
print(len(COUNT))
print(*COUNT.values())
# D21CE167
# Manan Kathrecha