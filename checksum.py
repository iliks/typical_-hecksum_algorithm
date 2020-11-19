def enc(g,a,e):
    b = ''
    c = a
    r = len(g) - 1
    while len(a) > r:
        a2 = list(a)
        for i in range(len(g)):
            if a2[i] != g[i]:
                a2[i] = '1'
            else:
                a2[i] = '0'
        a = ''.join(a2)
        while a[0] == '0' and len(a) > 1:
            a = a[1:]
    a = '0' * (r - len(a)) + a
    c = c[:-r] + a
    e = '0' * (len(c)-len(e)) + e
    for i in range(len(c)):
        b = b + str((int(c[i]) + int(e[i])) % 2)
    return b


def check(b, g):
    while len(b) > len(g) -1 :
        b1 = list(b)
        for i in range(len(g)):
            if b1[i] != g[i]:
                b1[i] = '1'
            else:
                b1[i] = '0'
        b = ''.join(b1)
        while b[0] != '1':
            if len(b) <= 1:
                break
            b = b[1:]
    if b == '' or b == '0':
        s = 0
        return s
    s = 1
    return s


g = input("ВВедите вектор g(x): ")
k = int(input('Введите k: '))
e = input('Введите e: ')
l = input('Введите l: ')
r = len(g) - 1
m = [0]
a = []
b = []
s = []
print(len(l))
if len(l) <= k:
    m[0] = l
else:
    m[0] = l[:k]
    l = l[k:]
    while len(l) > k:
        m.append(l[:k])
        l = l[k:]
    m.append(l)
kks = '0' * r
for i in m:
    a.append(i + kks)
for i in a:
    b.append(enc(g, i, e))
for i in b:
    s.append(check(i, g))
for i in range(len(s)):
    if s[i] == 0:
        print('В части кода ', i + 1, ' ошибок не обнаружено')
    else:
        print('В части кода ', i + 1, ' ошибка обнаружена')
