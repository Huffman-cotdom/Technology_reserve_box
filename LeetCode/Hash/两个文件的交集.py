# def inter(list1, list2):
#     dict1 = {}
#     for item in list1:
#         if item not in dict1:
#             dict1[item] = 1
#         else:
#             dict1[item] += 1

#     dict2 = {}
#     for item in list2:
#         if item not in dict2:
#             dict2[item] = 1
#         else:
#             dict2[item] += 1

#     dict3 = {}
#     for key in dict1.keys():
#         if key in dict2:
#             dict3[key] = max(dict1[key], dict2[key])

#     return dict3


# if __name__ == '__main__':
#     list1, list2 = [], []
#     with open('/Users/senna/Documents/WorkSpace/LeetCode/Hash/file_1.txt', 'r') as f:
#         for line in f.readlines():
#             data = line.strip('\n')
#             list1.append(data)
#     with open('/Users/senna/Documents/WorkSpace/LeetCode/Hash/file_2.txt', 'r') as f:
#         for line in f.readlines():
#             data = line.strip('\n')
#             list2.append(data)
#     print(list1, list2)
#     res = inter(list1, list2)
#     print(res)


def inner(list1, list2):
    dict1 = {}
    dict2 = {}
    dict3 = {}
    for item in list1:
        if item not in dict1:
            dict1[item] = 1
        else:
            dict1[item] += 1
    for item in list2:
        if item not in dict2:
            dict2[item] = 1
        else:
            dict2[item] += 1
    for key in dict1.keys():
        if key in dict2:
            dict3[key] = min(dict1[key], dict2[key])
    list_ = []
    for key in dict3.keys():
        for _ in range(dict3[key]):
            list_.append(key)
    return list_


if __name__ == '__main__':
    list1 = []
    list2 = []
    with open('Hash/file_1.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip('\n')
            list1.append(data)
    with open('Hash/file_2.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip('\n')
            list2.append(data)
    print(list1, list2)
    res = inner(list1, list2)
    print("ans:", res)
    with open('Hash/file_3.txt', 'a') as f:
        for s in res:
            f.write(s + '\n')
