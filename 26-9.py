num1, num2 = map(int, input().split())

a = set(i for i in range(1, num1 + 1) if a % i == 0)
b = set(i for i in range(1, num2 + 1) if b % i == 0)

divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)