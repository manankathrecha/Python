n = int(input())
score = map(int, input().split())
print(sorted(list(set(score)))[-2])