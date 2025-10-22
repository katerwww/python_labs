name = input().strip()
nam = name.split()
m = len(''.join(nam))+2
n = []
for i in nam:
    a = i[0]
    n.append(a)
h = ''.join(n)
print(f"Инициалы: {h}.")
print(f"Длина (символов): {m}")