name = input()
m = len(name.replace('  ', ''))
nam = name.strip().split()
n = []
for i in nam:
    a = i[0]
    n.append(a)
h = ''.join(n)
print(f"Инициалы: {h}.")
print(f"Длина (символов): {m}")