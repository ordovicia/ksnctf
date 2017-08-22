p = [70, 152, 195, 284, 475, 612, 791, 896, 810, 850, 737, 1332, 1469, 1120, 1470, 832, 1785, 2196, 1520, 1480, 1449];
flag = []

i = 0
for q in p:
    if i != 0:
        flag.append(chr(q // (i + 1)))
    else:
        flag.append(chr(q))
    i = i + 1

flag = ''.join(flag)
print(flag)
