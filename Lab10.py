#lab 10, task 1
Stoim = float(input("Введите стоимость 1 кг конфет "))
N = 10
for i in range(1, N) :
  print("Стоимость",(i/10),"кг конфет равна:",round((Stoim*(i/10)),3))
