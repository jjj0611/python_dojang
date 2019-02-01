words = input().split()

count_the = 0
for word in words:
    if word.strip(',.-') =='the':
        count_the += 1

print(count_the)