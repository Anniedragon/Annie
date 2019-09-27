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
