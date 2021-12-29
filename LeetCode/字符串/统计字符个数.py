while True:
    try:
        in_str = input()
        c_num, space_num, digit_num, other_num = 0, 0, 0, 0
        for x in in_str:
            if x.isalpha():
                c_num = c_num + 1
            elif x == " ":
                space_num = space_num + 1
            elif x.isdigit():
                digit_num = digit_num + 1
            else:
                other_num = other_num + 1
        print(c_num)
        print(space_num)
        print(digit_num)
        print(other_num)
    except:
        break
