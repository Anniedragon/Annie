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
 




 



