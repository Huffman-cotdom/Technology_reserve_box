def getprime(n):
    i = 2
    while i * i <= n and n >= i:
        while n % i == 0:
            n //= i
            print(i, end=' ')
        i += 1
    if n - 1:
        print(n)


if __name__ == "__main__":
    num = int(input())
    getprime(num)
