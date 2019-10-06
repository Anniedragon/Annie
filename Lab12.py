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

#lab 12, task 2
def Sign(X) :
  if X > 0:
    print("1")
  elif X == 0 :
    print("0")
  else :
    print("-1")
X = float(input("Введите число "))
Sign(X)

#lab 12, task 3 Почему вывод функции крашится из-за "проверки на дурака"?
def RingS(R1, R2) :
  print(abs(round((3.14 * R1**2) - (3.14 * R2**2),3)))
for i in range(1, 4) :
 Rad1 = float(input("Введите 1ый радиус "))
 Rad2 = float(input("Введите 2ой радиуc "))
 #while (Rad1 < Rad2):
  #print("1ый радиус должен быть больше 2ого!")
  #Rad2 = float(input("Введите 2ой радиус ")
 RingS(Rad1, Rad2) 
 
#lab 12, task 4
def Quater(x, y) :
  if (x > 0) and (y > 0) :
    print("Точка расположена в 1ой координатной четверти")
  elif (x < 0) and (y > 0) :
    print("Точка расположена в 2ой координатной четверти")
  elif (x < 0) and (y < 0) :
    print("Точка расположена в 3ьей координатной четверти")
  else :
    print("Точка расположена в 4ой координатной четверти")
for i in range(1, 4) :
  X = float(input("Введите координату Х "))
  Y = float(input("Введите координату Y "))
  while True :
    if X == 0 :
      print("Координата Х не должна быть равна 0")
      X = float(input("Введите координату Х "))
    elif Y == 0 :
      print("Координата Y не должна быть равна 0")
      Y = float(input("Введите координату Y "))
    else :
      break
  Quater(X, Y)

#lab 12, task 5
def Fact2(N) :
 f1 = 1
 f2 = 1
 if N % 2 != 0 :
   for i in range(1, N+1, 2) :
     f1 *= i
   print(f1)
 else :
   for i in range(2, N+1, 2) :
     f2 *= i
   print(f2)
Ch = float(input("Введите число, не равное 0 "))
while Ch == 0 :
  print("число не должно равняться 0!")
  Ch = float(input("Введите число, не равное 0 "))
Ch = int(Ch)
Fact2(Ch)   
     
   



 



