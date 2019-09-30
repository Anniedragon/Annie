#lab 10, task 1
Stoim = float(input("Введите стоимость 1 кг конфет "))
N = 10
for i in range(1, N) :
  print("Стоимость",(i/10),"кг конфет равна:",round((Stoim*(i/10)),3))
  
#lab 10, task 2
N = int(input("Введите число "))
pr = 1
for i in range(1, N+1) :
 pr = pr * (1 + (i/10))
print(pr)
