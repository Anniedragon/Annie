#lab 8, task 1
A = int(input("Введите число A "))
B = int(input("Введите число B "))
if A > B :
  B = A
  print("Новые значения А и В",A,B)
elif B > A :
  A = B
  print("Новые значения А и В",A,B)
else :
  A = 0
  B = 0
  print("Новые значения А и В",A,B)

#lab 8, task 2
A = int(input("Введите число A "))
B = int(input("Введите число B "))
C = int(input("Введите число С "))
if (A < B < C) or (A < C < B) :
  print(B + C)
elif (C < B < A) or (C < A < B) : 
  print(A + B)
elif (B < A < C) or (B < C < A) :
  print(A + C)

#lab 8, task 3
A = int(input("Введите число A "))
B = int(input("Введите число B "))
C = int(input("Введите число С "))
if abs(A - B) < abs(A - C) :
  print("Точка В расположена ближе. Расстояние до точки А:",abs(A-B))
else :
  print("Точка C расположена ближе. Расстояние до точки А:",abs(A-C))

#lab 8, task 4
X = float(input("Введите координату Х "))
Y = float(input("Введите координату Y "))
while True :
  if X == 0 :
    print("Х не должен быть равен 0")
    X = float(input("Введите число "))
  elif Y == 0 :
    print("Y не должен быть равен 0")
    Y = float(input("Введите число "))
  else :
    break
if (X > 0) and (Y > 0) :
  print("Точка лежит в 1ой координатной четверти")
if (X < 0) and (Y > 0) :
  print("Точка лежит в 2ой координатной четверти")
if (X < 0) and (Y < 0) :
  print("Точка лежит в 3ьей координатной четверти")
if (X > 0) and (Y < 0) :
  print("Точка лежит в 4ой координатной четверти")

#lab 8, task 5
A = int(input("Введите число "))
s1 = "- положительное "
s2 = "- отрицательное "
if A > 0 :
  if A % 2 == 0 :
   s1 = s1 + "чётное число"
   print(A, s1)
  else :
   s1 = s1 + "нечётное число"
   print(A, s1)
elif A < 0 :
  if A % 2 == 0 :
    s2 = s2 + "чётное число"
    print(A, s2)
  else :
    s2 = s2 + "нечётное число"
    print(A, s2)
else :
  print(A,"- нулевое число")

#lab 8, task 6
A = int(input("Введите число от 1 до 999 "))
while (A < 1) or (A > 999) :
  print("Число не соответствует диапазону")
  A = int(input("Введите число от 1 до 999 "))
s1 = "- двузначное "
s2 = "- трёхзначное "
if (A >= 1) and (A < 10) :
  if A % 2 == 0 :
    print(A,"- чётное число")
  else :
   print(A,"- нечётное число")
elif (A > 9) and (A < 100) :
  if A % 2 == 0 :
    s1 = s1 + "чётное число"
    print(A, s1)
  else :
    s1 = s1 + "нечётное число"
    print(A, s1)
else :
  if A % 2 == 0 :
    s2 = s2 + "чётное число"
    print(A, s2)
  else :
    s2 = s2 + "нечётное число"
    print(A, s2)
