#lab 13, task 1
N = int(input("Введите число, большее 0 "))
while N <= 0 :
  print("Число не должно быть равно 0")
  N = int(input("Введите число, большее 0 "))
M = []
for i in range(1, 2*N+1, 2) :
  M.append(i)
print(M)

#lab 13, task 2
N = int(input("Введите к-во членов прогрессии, большее 1: "))
while N <= 1 :
  print("Условие не выполнено!")
  N = int(input("Введите к-во членов прогрессии, большее 1: "))
M = []
A = int(input("Введите 1ый член геом. прогрессии: "))
D = int(input("Введите знаменатель геом. прогрессии: "))
for i in range(N) :
  M.append(A * D**i)
print(M)

#lab 13, task 3 In progress
N = int(input("Введите число, большее 2 "))
M = []
A = int(input("Введите 1ый элемент списка "))
B = int(input("Введите 2oй элемент списка "))
while N <= 2 :
  print("Число не должно быть равно 0")
  N = int(input("Введите число, большее 0 "))
M.append(A)
M.append(B)
for i in range(N-2) :
 M.append(M[i] + M[i-1])
print(M)