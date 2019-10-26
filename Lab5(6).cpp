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
    if(temp[j]>temp[j-1]){
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
//lab5(6), task 3
#include <iostream>
using namespace std;
int main(){
int x, f=0, y, k1=0, k2=0, k=0;
int min;
cout << "Cin razmer matriz ";
cin >> x;
y = x;
int temp[x][y];
int t[x];
for(int i = 0; i<x; i++){
  for(int j = 0; j<x; j++){
  cin >> temp[i][j];
}
}
for(int i = 0; i<x; i++){ 
  t[k] = temp[k1][k2]; 
  k++;
  k1++;
  k2++;
}
for(int i = 0; i<x; i++ ){
  for(int j = 1; j<x; j++){
    if(t[j]<t[j-1]){
      f = t[j-1];
      t[j-1] = t[j];
      t[j] = f;
    }
  }
}
k = 0;
k1 = 0;
k2 = 0;
for(int i = 0; i<x; i++){ 
  temp[k1][k2] = t[k]; 
  k++;
  k1++;
  k2++;
}
for(int i = 0; i<x; i++){
  for(int j = 0; j<x; j++){
    if(j!=(x-1)){
      cout << temp[i][j] << " ";
    }
    else cout << temp[i][j] << endl;
  }
}
return 0;
}
