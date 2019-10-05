#lab 11, task 1
A = int(input("Введите число А "))
B = int(input("Введите число В, большее, чем А "))
while (A > B) or (A == B) :
  print("Условие не выполнено!")
  B = int(input("Введите число В, большее, чем А "))
for i in range(A, B+1) :
  for j in range(1, i+1) :
    if j == i:
     print(i)
    else :
     print(i, end = " ")

#lab 11, task 2
A = int(input("Введите число А "))
B = int(input("Введите число, большее А "))
k = 0
while (A > B) or (A == B) :
  print("Условие не выполнено ")
  B = int(input("Введите число, большее А "))
for i in range(1,B+1,A) :
  k += 1
if B == k * A :
  Ost = B - k * A
else :
  Ost = B - (k - 1) * A
print(Ost)

#lab 11, task 3
N = int(input("Введите число, большее 1 "))
while N <= 1 :
  N = int(input("Введите число, большее 1 "))
K = 0
S = 0
while S <= N :
  S += K
  K += 1
print(K,",","Сумма равна:",S)

#lab 11, task 4
S = 1000
S1 = 1100
K = 0
P = float(input("Введите процент, 0 < P < 25 "))
while (P < 0) or (P > 25) :
  print("Недопустимое значение!")
  P = float(input("Введите процент, 0 < P < 25 "))
while S <= S1 :
  S = S * (1 + (P / 100))
  K += 1
print("Итоговый размер вклада:",S)
print("Количество месяцев:",K)

#lab 11, task 5
A = int(input("Введите число "))
B = int(input("Введите число "))
while A != B :
  if A > B :
    A = A - B
  else :
    B = B - A
print(A)
