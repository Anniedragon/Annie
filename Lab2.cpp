//lab 2, task 1.1
#include <iostream>
using namespace std;
int main() {
 float N;
 cout << "Enter N" << endl;
 cin >> N;
 int i;
 float st;
 st = 1;
 for (i = 1; i <= N; i++) {
  st = st * 2;
 }
 cout << st << endl;
 return 0;
}

//lab 2, task 1.2
#include <iostream>
using namespace std;
int main() {
 float N;
 cout << "Enter N" << endl;
 cin >> N;
 int i;
 float F;
 F = 1;
 for (i = 1; i <= N; i++) {
  F = F * i;
 }
 cout << F << endl;
 return 0;
}

//lab 2, task 1.4
#include <iostream>
using namespace std;
#include <math.h>
int main() {
  int N;
  int i;
  float A;
  cout << "Введите N " << endl;
  cin >> N;
  A = sqrt(2);
  cout << A << endl;
  for (i=1; i<=N; i++) {
   A = sqrt(2 + A);
   cout << A << endl;
  }
  cout << A << endl;
  return 0;
}
