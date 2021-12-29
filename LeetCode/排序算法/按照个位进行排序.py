from collections import defaultdict

my_dict = defaultdict(list)
sort_num = []
nums = [1, 2, 5, -12, 22, 11, 55, -101, 42, 8, 7, 32]

for i in nums:

    my_dict[str(i)[-1]].append(i)

for i in range(10):
    if str(i) in my_dict.keys():
        sort_num.append(my_dict[str(i)])
for i in range(len(sort_num)):
    for j in range(len(sort_num[i])):
        print(sort_num[i][j])
