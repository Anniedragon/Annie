#lab 9, task 1
Mes = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
Chis = ["первое", "второе", "третье", "четвёртое", "пятое", "шестое", "седьмое", "восьмое", "девятое", "десятое", "одиннадцатое", "двенадцатое", "тринадцатое", "четырнадцатое", "пятнадцатое", "шестнадцатое", "семнадцатое", "восемнадцатое", "девятнадцатое", "двадцатое", "двадцатое", "двадцать первое", "двадцать второе", "двадцать третье", "двадцать четвёртое", "двадцать пятое", "двадцать шестое", "двадцать седьмое", "двадцать восьмое", "двадцать девятое", "тридцатое", "тридцать первое"]
M = int(input("Введите номер месяца "))
Ch = int(input("Введите номер дня месяца "))
s1 = Chis[Ch - 1] + " " + Mes[M - 1]
print(s1)

#lab 9, task 2
C = str(input("Введите исходное направление робота (С, З, Ю, В) "))
N =  int(input("Введите команду для робота (0, 1 или -1) "))
while (C != "С") and (C != "З") and (C != "Ю") and (C != "В") :
  print("Неприемлемое направление!")
  C = str(input("Введите исходное направление робота (С, З, Ю, В) "))
while (N != 1) and (N != 0) and (N != -1) :
  print("Неприемлемая команда!")
  N =  int(input("Введите команду для робота (0, 1 или -1)"))
if C == "С" :
  if N == 0 :
    print("С(север)")
  elif N == 1 :
    print("З(запад)")
  else :
    print("В(восток)")
if C == "З" :
  if N == 0 :
    print("З(запад)")
  elif N == 1 :
    print("Ю(юг)")
  else :
    print("С(север)")
if C == "Ю" :
  if N == 0 :
    print("Ю(юг)")
  elif N == 1 :
    print("В(восток)")
  else :
   print("З(запад)")
if C == "В" :
  if N == 0 :
    print("В(восток)")
  elif N == 1 :
    print("С(север)")
  else :
    print("Ю(юг)")

#lab 9, task 3
num = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать", "двадцать", "двадцать одно", "двадцать два", "двадцать три", "двадцать четыре", "двадцать пять", "двадцать шесть", "двадцать семь", "двадцать восемь", "двадцать девять", "тридцать", "тридцать одно", "тридцать два", "тридцать три", "тридцать четыре", "тридцать пять", "тридцать шесть", "тридцать семь", "тридцать восемь", "тридцать девять", "сорок"]
A = int(input("Введите число от 10 до 40 "))
while (A < 10) or (A > 40) :
  print("Число не соотвествует промежутку!")
  A = int(input("Введите число от 10 до 40 "))
if ((A >= 10) and (A <= 20)) or ((A >= 25) and (A <= 30)) or ((A >= 35) and (A <= 40)) :
  S = num[A - 10] + " " + "учебных заданий"
elif (A == 21) or (A == 31) :
  S = num[A - 10] + " " + "учебное задание"
else :
  S = num[A - 10] + " " + "учебных задания"
print(S) 

#lab 9, task 4
ed = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
des = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
des1 = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
sot = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
S = ""
s1 = ""
s2 = ""
s3 = ""
A = int(input("Введите число от 100 до 999: "))
while (A < 100) or (A > 999) :
  print("Число не входит в указанный диапазон!")
  A = int(input("Введите число от 100 до 999: "))
if (A >= 111) and (A <= 119) :
  S = "сто" + " " + des1[(A % 10) - 1]
if not((A >= 111) and (A <= 119)) :
  if A % 10 != 0 :
    s1 = ed[(A % 10) - 1]
  if ((A // 10) % 10) != 0 :
    s2 = des[((A // 10) % 10) - 1] + " "
  s3 = sot[(A // 100) - 1] + " "
  S = s3 + s2 + s1
print(S)

#lab 9, task 5
col = ["зелёной", "красной", "жёлтой", "белой", "чёрной"]
col1 =["зелёного", "красного", "жёлтого", "белого", "чёрного"]
anim = ["крысы", "коровы", "тигра", "зайца", "дракона", "змеи", "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"]
year = int(input("Введите номер года "))
C = abs(1984 - year)
while C > 60 :
 C = C - 60
k = int(C / 12)
PodC = C - k * 12
k1 = C / 12 
if k != k1 :
 ch = k + 1 
else :
  ch = k
if (PodC != 3) and (PodC != 4) and (PodC != 5) :
 s = str(year) + " - " + col[ch - 1] + " " + anim[PodC - 1]
else :
 s = str(year) + " - " + col1[ch - 1] + " " + anim[PodC - 1]
print(s)

