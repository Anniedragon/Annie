#lab 13, task 1
N = int(input("Введите число, большее 0 "))
while N == 0 :
  print("Число не должно быть равно 0")
  N = int(input("Введите число, большее 0 "))
M = []
for i in range(1, 2*N+1, 2) :
  M.append(i)
print(M)
