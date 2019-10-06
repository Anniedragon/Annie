#lab 12, task 1
def PowerA3(A, B) :
  return A**B
St = float(input("Введите 3 "))
while (St != 3) :
  print("Введите число 3!")
  St = float(input("Введите 3 "))
  Res = 0
for i in range(1, 6) :
  Ch = float(input("Введите число "))
  Res = PowerA3(Ch, St)
  print(Res)

