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
