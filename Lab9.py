#lab 9, task 5
year = int(input("Введите номер года "))
C = abs(1984 - year) #считаем остаток 
while C > 60 : # проверяем на полный цикл
 C = C - 60
k = int(C / 12) # считаем целое колисество подциклов с округлением в меньшую сторону
PodC = C - k * 12 # считаем, сколько дней осталось, после полных подциклов
k1 = C / 12 
if k != k1 :
 ch = k + 1 
else :
  ch = k
if ch == 1 :
  s = " год зелёной "
  if PodC == 1 :
    s = s + "крысы"
  elif PodC == 2 :
    s = s + "коровы"
  elif PodC == 3 :
    s = s[:10] + "ого " + "тигра"
  elif PodC == 4 :
    s = s[:10] + "ого " +  "зайца"
  elif PodC == 5 :
    s = s[:10] + "ого " + "дракона"
  elif PodC == 6 :
    s = s + "змеи"
  elif PodC == 7 :
    s = s + "лошади"
  elif PodC == 8 :
    s = s + "овцы"
  elif PodC == 9 :
    s = s + "обезьяны"
  elif PodC == 10:
    s = s + "курицы"
  elif PodC == 11:
    s = s + "собаки"
  elif PodC == 12:
    s = s + "свиньи"
if ch == 2 :
  s = " год красной "
  if PodC == 1 :
    s = s + "крысы"
  elif PodC == 2 :
    s = s + "коровы"
  elif PodC == 3 :
    s = s[:10] + "ого " + "тигра"
  elif PodC == 4 :
    s = s[:10] + "ого " + "зайца"
  elif PodC == 5 :
    s = s[:10] + "ого " + "дракона"
  elif PodC == 6 :
    s = s + "змеи"
  elif PodC == 7 :
    s = s + "лошади"
  elif PodC == 8 :
    s = s + "овцы"
  elif PodC == 9 :
    s = s + "обезьяны"
  elif PodC == 10:
    s = s + "курицы"
  elif PodC == 11:
    s = s + "собаки"
  elif PodC == 12:
    s = s + "свиньи"
if ch == 3 :
  s = " год жёлтой "
  if PodC == 1 :
    s = s + "крысы"
  elif PodC == 2 :
    s = s + "коровы"
  elif PodC == 3 :
    s = s[:10] + "ого " + "тигра"
  elif PodC == 4 :
    s = s[:10] + "ого " + "зайца"
  elif PodC == 5 :
    s = s[:10] + "ого " + "дракона"
  elif PodC == 6 :
    s = s + "змеи"
  elif PodC == 7 :
    s = s + "лошади"
  elif PodC == 8 :
    s = s + "овцы"
  elif PodC == 9 :
    s = s + "обезьяны"
  elif PodC == 10:
    s = s + "курицы"
  elif PodC == 11:
    s = s + "собаки"
  elif PodC == 12:
    s = s + "свиньи"
if ch == 4 :
  s = " год белой "
  if PodC == 1 :
    s = s + "крысы"
  elif PodC == 2 :
    s = s + "коровы"
  elif PodC == 3 :
    s = s[:10] + "ого " + "тигра"
  elif PodC == 4 :
    s = s[:10] + "ого " + "зайца"
  elif PodC == 5 :
    s = s[:10] + "ого " + "дракона"
  elif PodC == 6 :
    s = s + "змеи"
  elif PodC == 7 :
    s = s + "лошади"
  elif PodC == 8 :
    s = s + "овцы"
  elif PodC == 9 :
    s = s + "обезьяны"
  elif PodC == 10:
    s = s + "курицы"
  elif PodC == 11:
    s = s + "собаки"
  elif PodC == 12:
    s = s + "свиньи"
if ch == 5 :
  s = " год чёрной "
  if PodC == 1 :
    s = s + "крысы"
  elif PodC == 2 :
    s = s + "коровы"
  elif PodC == 3 :
    s = s[:10] + "ого " + "тигра"
  elif PodC == 4 :
    s = s[:10] + "ого " + "зайца"
  elif PodC == 5 :
    s = s[:10] + "ого " + "дракона"
  elif PodC == 6 :
    s = s + "змеи"
  elif PodC == 7 :
    s = s + "лошади"
  elif PodC == 8 :
    s = s + "овцы"
  elif PodC == 9 :
    s = s + "обезьяны"
  elif PodC == 10:
    s = s + "курицы"
  elif PodC == 11:
    s = s + "собаки"
  elif PodC == 12:
    s = s + "свиньи"
Year = str(year) + " -" + s
print(Year)
