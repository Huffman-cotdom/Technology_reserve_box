import math


def type_1(n_out, val):
    # (d+p)x(d+p)
    assert 1 <= val <= 10
    return n_out + val


def type_2(n_out, val):
    # (d*p)x(d*p)
    assert 2 <= val <= 3
    return n_out * val


def type_3(n_out, val):
    # s*p>=d
    assert 2 <= val <= 10
    return math.ceil(n_out / val)


K = int(input())
n_out = 1

for ii in range(K):
    type_key, type_val = list(map(int, input().strip().split()))

    if type_key == 1:
        n_out = type_1(n_out, type_val)
    if type_key == 2:
        n_out = type_2(n_out, type_val)
    if type_key == 3:
        n_out = type_3(n_out, type_val)

print(n_out)
