//lab 3, task 1
#include <iostream>
using namespace std;
int main() {
  int N = 0;
  int flag = 1;
  int count = 0;
  int sum = 0;
  int pr = 1;
    cout << "Input number of elements" << endl;
      cin >> N;
  int temp[N];
    cout << "Cin elements" << endl;
  for(int i=0; i<N; i++){
      cin >> temp[i];
      cout << endl;
  } 
  for (int j=0; j<N; j++) {
    if (temp[j] % 2 != 0) {
      sum = sum + temp[j];
      pr = pr * temp[j];
      count = count + 1;
    }  
  }
  cout << "Сумма нечётных чисел равна:" << sum << endl;
  cout << "Произведение нечётных чисел равно:" << pr << endl;
  cout << "Количество нечётных чисел равно:" << count << endl;
  }
