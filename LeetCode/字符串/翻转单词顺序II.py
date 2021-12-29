s = "the sky is blue"
s = ' '.join([i for i in s.split() if i][::-1])
res = ''
for i in s.split():
    res += (i[::-1] + ' ')
print(res)
