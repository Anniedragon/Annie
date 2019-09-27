#lab 5, task 1
B = float(input("Введите количество байтов в файле "))
Kb = B / 1000
print("Количество килобайтов в этом файле равно",Kb)

#lab 5, task 2
A = float(input("Введите отрезок А "))
B = float(input("Введите отрезок В, который меньше А "))
while True :
  if A < B or A == B :
    B = float(input("Введите отрезок В, который меньше А "))
  else :
    break
k = int(A / B)
print("Целое количество отрезков В в А равно", k)

#lab 5, task 3
A = float(input("Введите отрезок А "))
B = float(input("Введите отрезок В, который меньше А "))
while True :
  if A < B or A == B :
    B = float(input("Введите отрезок В, который меньше А "))
  else :
    break
k = int(A / B)
ost = A - k * B
print("Остаток отрезка А равен", ost)

#lab 5, task 4
A = int(input("Введите двузначное число "))
while True :
  if A < 10 or A > 99 :
    print("Это не двузначное число")
    A = int(input("Введите двузначное число "))
  else :
    break
ed = A % 10
des = A // 10
print("Новое число:", ed * 10 + des)

#lab 5, task 5
A = int(input("Введите трехзначное число "))
while True :
  if A < 100 or A > 999 :
    print("Это не трехзначное число")
    A = int(input("Введите трехзначное число "))
  else :
    break
S = str(A)
temp = S[0]
s1 = S[0]
s2 = S[1]
s3 = S[2]
S = s3 + s2 + s1
print("Новое число:",S)
