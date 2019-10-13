//lab 3, task 1
#include <iostream>
using namespace std;
int main() {
  int N = 0;
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

//lab 3, task 2
#include <iostream>
using namespace std;
int main(){
  int x = 0;
  int max;
  int min;
  cout << "Input number of elements ";
  cin >> x;
  int temp[x];
  for(int k = 1; k<=x; k++){
    cout << "Input " << k << " element ";
    cin >> temp[k];
  }
  for (int i=0; i<x; i++){
    if(i == 0){
      min = temp[i];
    }
    if(temp[i]<min){
      min = temp[i];
    }
  } 
  for (int j=0; j<x; j++){
    if(j == 0){
      max = temp[j];
    }
    if(temp[j]>max){
      max = temp[j];
    }
  } 
  cout << "Min element is " << min << endl;
  cout << "Max element is " << max << endl;
}
