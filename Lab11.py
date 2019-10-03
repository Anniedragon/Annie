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
