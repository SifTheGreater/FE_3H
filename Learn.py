def create1k():
    si = ""
    for ii in range(1024):
        si += '*'
    return si


def create1m():
    si = ""
    xi = create1k()
    for ii in range(1024):
        si += xi
    return si


def create1g():
    si = ""
    xi = create1m()
    for ii in range(1024):
        si += xi
    return si


print("begin")
s = ""
x = create1g()
for i in range(1024):
    s += x
    print(str(i) + "g ok")
    print(str(len(s)) + ' bytes')
