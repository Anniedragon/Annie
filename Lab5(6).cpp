//lab5(6), task 1
#include <iostream>
using namespace std;
int main(){
int x, t=0, f=0, q=0, y=0, k=0;
int min;
y = 0;
cout << "Cin razmer massiva ";
cin >> x;
int temp[x];
for(int i = 0; i<x; i++){
  cin >> temp[i];
}
for(int i = 0; i<x; i++){  
  k = 0;
  for(int j = y; j<x; j++){
    if(k==0){
      min = temp[j];
      q = j;
      k++;
    }
    if(min > temp[j]){
      min = temp[j];
      q = j;
    }
  }
  t = temp[f];
  temp[f] = min;
  temp[q] = t;
  y++;
  f++;
}
for(int i = 0; i<x; i++){
  cout << temp[i] << " ";
}
return 0;
}
//lab5(6), task 2
#include <iostream>
using namespace std;
int main(){
int x, f=0;
int min;
cout << "Cin razmer massiva ";
cin >> x;
int temp[x];
for(int i = 0; i<x; i++){
  cin >> temp[i];
}
for(int i = 0; i<x; i++ ){
  for(int j = 1; j<x; j++){
    if(temp[j]<temp[j-1]){
      f = temp[j-1];
      temp[j-1] = temp[j];
      temp[j] = f;
    }
  }
}
for(int i = 0; i<x; i++){
  cout << temp[i] << " ";
}
return 0;
}
