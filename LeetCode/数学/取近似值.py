num = float(input())
num = num * 10
remainder = num % 10
if remainder >= 5:
    print(int(num / 10) + 1)
else:
    print(int(num / 10))
