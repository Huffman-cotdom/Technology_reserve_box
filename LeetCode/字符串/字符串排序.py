num = int(input())
in_list = [input() for _ in range(num)]
in_list_s = []
in_list_s = sorted(in_list)
for x in in_list_s:
    print(x)
