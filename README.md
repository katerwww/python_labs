# __Лабораторная работа 1__
## задание 1
```
a = input()
b = int(input())
c = b + 1
print(f"Привет, {a}! Через год тебе будет {c}.")
```
![01](./images/lab01/lab01_ex01.png)
## задание 2
```
a = float(input())
b = float(input())
summ = a + b
avg = round((a + b)/2, 2)
print(f"sum={summ}; avg={avg}")
```
![02](./images/lab01/lab01_ex02.png)
## задание 3
```
price = float(input())
discount = float(input())
vat = float(input())

base = round(price * (1 - discount/100), 2)
vat_amount = round(base * (vat/100), 2)
total = round(base + vat_amount, 2)

print(f"База после скидки: {base} ₽")
print(f"НДС: {vat_amount} ₽")
print(f"Итого к оплате: {total} ₽")
```
![03](./images/lab01/lab01_ex03.png)
## задание 4
```
min = int(input())
hours = min//60
ost_min = min%60
print(f"{hours} : {ost_min:02d}")
```
![04](./images/lab01/lab01_ex04.png)
## задание 5
```
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
```
![05](./images/lab01/lab01_ex05.png)


# __Лабораторная работа 2__
## задание 1 
```
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        return ValueError
    return (min(nums), max(nums))
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([ ]))
print(min_max([1.5, 2, 2.0, -3.1]))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

def flatten(mat: list[list | tuple]) -> list:
    res = []
    for x in mat:
        if not isinstance(x, (list, tuple)):
            return ValueError
        res.extend(x)
    return res

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![01](./images/lab02/lab02_ex01.png)

## задание 2 
```
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    rv_l = len(mat[0])
    for rv in mat:
        if len(rv) != rv_l:
            return ValueError
    return [[mat[j][i] for j in range(len(mat))] for i in range(rv_l)]

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            return ValueError
    
    return [sum(row) for row in mat]
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            return ValueError
    
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(row_length)]

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![02](./images/lab02/lab02_ex02.png)

## задание 3 
```
def format_record(rec: tuple[str, str, float]) -> str:

    if not isinstance(rec[0], str) or not rec[0].strip():
        return ValueError
    if not isinstance(rec[1], str) or not rec[1].strip():
        return ValueError
    if not isinstance(rec[2], (float, int)):
        return TypeError
    
    fio = ' '.join(rec[0].strip().split())
    parts = fio.split()

    surname = parts[0]
    initials = ''.join(part[0].upper() + '.' for part in parts[1:]).strip()

    gpa = f"{rec[2]:.2f}"

    result = f"{surname} {initials}, гр. {rec[1].strip()}, GPA {gpa}"
    
    return result

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))

```
![03](./images/lab02/lab02_ex03.png)