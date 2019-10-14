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

//lab 3, task 3
#include <iostream>
using namespace std;
int main(){
 int x, b, N;
 x = 0;
 cout << "Cin number of elements ";
 cin >> N;
 int temp[N];
 int t[N];
 cout << "Cin b ";
 cin >> b;
 for(int i = 0; i<N; i++){
   cout << "Cin " << i+1 << " element ";
   cin >> t[i];
   temp[i] = 0;
 }
 for (int j = 0; j<N; j++){
   if(t[j]>=b){
     cout << t[j] << " ";
   }
 }
return 0;
}

//lab 3, task 4(8)
#include <iostream>
using namespace std;
int main(){
  int x = 0;
  int f = 0;
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
      f = i;
    }
  } 
  temp[f] = 0 - temp[f];
  for(int k = 1; k<=x; k++){
    cout << temp[k] << " ";
  }
   return 0;
}
