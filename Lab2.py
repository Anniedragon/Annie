#lab 2, task 1
x1 = int(input("Введите координату х1 "))
y1 = int(input("Введите координату y1 "))
x2 = int(input("Введите координату х2 "))
y2 = int(input("Введите координату y2 "))
print("Длина отрезка равна",((x2 - x1)**2 + (y2 - y1)**2)**0.5)

#lab 2, task 2
a = int(input("Введите число для точки А "))
b = int(input("Введите число для точки В "))
c = int(input("Введите число для точки С "))
d1 = 0
d2 = 0
if (a > c) and (b > c) :
  d1 = abs(a - c)
  d2 = abs(b - c)
else :
 d1 = abs(c - a)
 d2 = abs(c - b)
print("AC =",d1," , ","BC =",d2," , ","Сумма ВС и АС равна",d1+d2)

#lab 2, task 3
a = int(input("Введите число для точки А "))
b = int(input("Введите число для точки B "))
c = int(input("Введите число для точки C, причем А < C < B или В < C < A "))
d1 = 0
d2 = 0
while True :
  if (a < c < b) or (b > c > a) :
    break
  else :
    c = int(input("Введите число для точки C, причем А < C < B или В < C < A "))
d1 = abs(a - c)
d2 = abs(b - c)
print("AC =",d1," , ","BC =",d2," , ","Произведение ВС и АС равно",d1*d2)

#lab2, task 4
x1 = int(input("Введите координату х точки "))
y1 = int(input("Введите координату y точки "))
x2 = int(input("Введите координату х другой точки "))
y2 = int(input("Введите координату y другой точки "))
d1 = 0
d2 = 0
d1 = x2 - x1 
d2 = y2 - y1
print("Периметр прямоугольника равен",2*(d1 + d2))
print("Площадь прямоугольника равна",d1 * d2)

#lab 2, task 5 
import math
x1 = int(input("Введите координату х для 1ой вершины треугольника "))
y1 = int(input("Введите координату y для 1ой вершины треугольника "))
x2 = int(input("Введите координату х для 2ой вершины треугольника "))
y2 = int(input("Введите координату y для 2ой вершины треугольника "))
x3 = int(input("Введите координату х для 3ьей вершины треугольника "))
y3 = int(input("Введите координату y для 3ьей вершины треугольника "))
s1 = 0
s2 = 0
s3 = 0
p = 0
s1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
s2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
s3 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
p = (s1 + s2 + s3) / 2
print("Периметр треугольника равен", s1 + s2 + s3)
print("Площадь треугольника равна", p * math.sqrt((p - s1) * (p - s2) * (p - s3)))
