while True:
    try:
        word = input().upper()
        s = input()
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 字母表
        n_word = ''  # 融入加密词后的新字母表
        res = ''
        for i in word:
            if i not in n_word:
                n_word += i
        for i in alpha:
            if i not in n_word and len(n_word) <= 26:
                n_word += i
        for i in s:
            if i in alpha:
                res += n_word[alpha.index(i)]
            else:
                res += n_word[alpha.index(i.upper())].lower()
        print(res)
    except:
        break
