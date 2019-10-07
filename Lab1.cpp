//lab 1, task 1
#include <iostream>
using namespace std;
int main() {
  float a, b, c, temp;
  cin >> a;
  cin >> b;
  cin >> c;
  if (a > temp) {
   temp = a;
  }
   if (b > temp) {
   temp = b;
  }
   if (c > temp) {
   temp = c;
  }
  cout << "Максимальное:" << temp << endl;
  temp=a;
   
   if ( temp>b ) {
   temp = b;
  }
   if ( temp>c) {
   temp = c;
  }
 cout << "Минимальное:" << temp << endl; 
}

//lab 1, task 2
#include <iostream>
using namespace std;
int main() {
  int a, b, c;
  cin >> a;
  cin >> b;
  cin >> c;
  if (a > 2 and a < 5) {
    cout << a << " принадлежит промежутку от 2 до 5" << endl;
  }
  if (b > 2 and b < 5) {
    cout << b << " принадлежит промежутку от 2 до 5" << endl;
  } 
  if (c > 2 and c < 5) {
    cout << c << " принадлежит промежутку от 2 до 5" << endl;  
  } 
  if (a == 2 || a == 5) {
    cout << a << " лежит на границе" << endl;
  }
  if (b == 2 || b == 5) {
    cout << b << " лежит на границе" << endl;
  } 
  if (c == 2 || c == 5) {
    cout << c << " лежит на границе" << endl;  
  } 
 if (a < 2 || a > 5) {
    cout << a << " не принадлежит промежутку от 2 до 5" << endl;
  }
  if (b < 2 || b > 5) {
    cout << b << " не принадлежит промежутку от 2 до 5" << endl; 
  } 
  if (c < 2 || c > 5) {
    cout << c << " не принадлежит промежутку от 2 до 5" << endl; 
  } 
  return 0;
}

//lab 1, task 3
#include <iostream>
using namespace std;
int main() {
 int age;
 cout << "Введите ваш возраст" << endl;
 cin >> age;
 while ((age <= 0) || (age > 101)) {
   cout << "Возраст некорректен" << endl;
   cout << "Введите ваш возраст" << endl;
   cin >> age;
 }
 if ((age == 1 )||(age % 10 == 1)) {
   cout << "Вам " << age << " год" << endl;
 }
 if (((age==2)||(age==3)||(age==4)||(age % 10==2)||(age % 10==3)||(age % 10==4))&&(!((age==12)||(age==13)||(age==14)))) {
   cout << "Вам " << age << " года" << endl; 
 }
 if (!((age == 1 )||(age % 10 == 1)||(age==2)||(age==3)||(age==4)||(age % 10==2)||(age % 10==3)||(age % 10==4)||(age==12)||(age==13)||(age==14))) {
   cout << "Вам " << age << " лет" << endl;
 } 
 return 0;
}

//lab 1, task 4
#include <iostream>
#include <cmath>
using namespace std;
int main() {
  float a, b, c, x, x1, x2, D;
  cout << "Введите коэффициент а" << endl;
    cin >> a;
  cout << "Введите коэффициент b" << endl;
    cin >> b;
  cout << "Введите коэффициент c" << endl;
    cin >> c;
  if ((a == 0) && (b != 0) && (c != 0)) {
    x = -(c / b);
    cout << "x = " << x << endl;
  }
  if ((b == 0) && (a != 0) && (c != 0)) {
    if ((a > 0) && (c > 0)) {
      cout << "Решений нет." << endl;
    }
    else {
      x1 = sqrt(c / a);
      x2 = -sqrt(c / a);
      cout << "x1 = " << x1 << ", " << "x2 = " << x2 << endl;
    }
  }
  if ((c == 0) && (b != 0) && (a != 0)) {
    x1 = 0;
    x2 = -(b / a);
    cout << "x1 = " << x1 << ", " << "x2 = " << x2 << endl;
  }
  if ((a == 0) && (b == 0) && (c != 0)) {
    cout << "Решений нет." << endl;
  } 
  if ((b == 0) && (c == 0) && (a != 0)) {
    x = 0;
    cout << "x = " << x << endl;
  }
  if ((a == 0) && (c == 0) && (b != 0)) {
    x = 0;
    cout << "x = " << x << endl;
  }
  if ((a == 0) && (b == 0) && (c == 0)) {
    cout << "Бесконечно много решений" << endl;
  }
  if ((a != 0) && (b != 0) && (c != 0)) {
    D = b*b - 4*a*c;
    if (D > 0) {
      x1 = (-b + sqrt(D)) / (2*a);
      x2 = (-b - sqrt(D) / (2*a));
      cout << "x1 = " << x1 << ", " << "x2 = " << x2 << endl;
    }
    if (D == 0) {
      x = -(b / (2*a));
      cout << "x = " << x << endl;
    }
    if (D < 0) {
      cout << "Решений нет." << endl;
    }
  }
  return 0;
  }
  
  



//задание 3.
#include <iostream>
using namespace std;
int main()
{
    setlocale(LC_ALL, "Russian");
    int a, temp;
        cout<<"Введите ваш возраст ";
            cin >> a;
    temp = a-(a/10)*10;
        cout << endl << endl;
    if(a<0||a>100){
        cout << "Введите корректный возрат";
    }
    else{
        if((a == 12)|| (a == 13) || (a == 14) || (temp==5) || (temp == 6) || (temp == 7) || (temp == 8) || (temp == 9) ||(temp == 10)){
            cout << "Вам " << a << " лет";
        }
        else {
            if((temp==2)||(temp==3)||(temp==4)){
                cout <<"Вам " << a << " года";
            }
            else cout << "Вам " << a << " год";
        }
        
    }
    return 0;
}
