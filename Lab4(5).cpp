//lab 4(5), task 1
#include <iostream>
using namespace std;
int main() {
  int N;
  int k = 0;
  cout << "Enter N ";
    cin >> N;
  int A[N][N];
  for (int i=1; i<=N; i++) {
    for (int j=1; j<=N; j++) {
        cout << "Enter element ";
        cin >> A[i][j];
      }
    }
  int min = A[0][0];
  for (int i=1; i<=N; i++) {
    for (int j=1; j<=N; j++) {
      if (j < N) {
        cout << A[i][j] << " ";
      }
      if (j == N) {
        cout << A[i][j] << endl;
      } 
    }
  }
  for (int i=1; i<=N; i++) {
    for (int j=1; j<=N; j++) {
      if (A[i][j] < min) {
        min = A[i][j];
      }
    }
  }
  cout << "Minimum = " << min << endl;
}

//lab 4(5), task 2
#include <iostream>
using namespace std;
int main() {
  cout << "Cin razmer matiz ";
  int x, y, k, m, max, l, f;
  cin >> x;
  y = x;
  k = 0;
  m = 0;
  max = 0;
  l = 0;
  f = 0;
  int temp[x][y];
  for (int i=0; i<x; i++) {
    for (int j=0; j<y; j++) {
      cin >> temp[i][j];
    }
  }
  for (int i=0; i<x; i++) {
    for (int j=0; j<y; j++) {
      if (j == 0) {
        max = temp[i][j];
        f = j;
      }
      if (temp[i][j] > max) {
        max = temp[i][j];
        f = j;
      }
      if (j == (x - 1)) {
        l = temp[m][k];
        temp[m][k] = max;
        temp[i][f] = l;
        max = -214783647;
        k++;
        m++;
      }
    }
  }
  for (int i=0; i<x; i++) {
    for (int j=0; j<x; j++) {
      if (j == (y - 1)) {
        cout << temp[i][j] << endl;
      }
      else {
        cout << temp[i][j] << " ";
      }
    }
  }
  return 0;
}

//lab4(5), task 3
#include <iostream>
using namespace std;
int main() {
  int N, M, ymno, slo;
 
  cout << "Cin razmer matrizyu ";
  cout << "Cin N ";
  cin >> N;
  cout  << "Cin M ";
  cin >> M;
  int t[N][M];
  for(int i = 0; i<N; i++){
    for(int j = 0; j < M; j++){
    cin >>t[i][j];
    }
  }
    for(int i = 0; i<N; i++){
     ymno = 1;
     slo = 0;
    for(int j = 0; j < M; j++){
    slo = slo+t[i][j];
    ymno = ymno*t[i][j];
    }
    cout << slo << " " << ymno << endl;
  }
}

//lab4(5), task 4
#include <iostream>
using namespace std;
int main() {
  int N, M, slo, k;
 
  cout << "Cin razmer matrizyu ";
  cout << "Cin N ";
  cin >> N;
  cout  << "Cin M ";
  cin >> M;
  int t[N][M];
  for(int i = 0; i<N; i++){
    for(int j = 0; j < M; j++){
    cin >>t[i][j];
    }
  }
    for(int j = 0; j<M;j++){
     slo = 0;
    for(int i = 0; i < N; i++){
      if (t[i][j] > 0){
    slo = slo+t[i][j];
    }
    }
    cout << slo << " ";
  }
  cout << endl;
  for(int j = 0; j<M;j++){
    k = 0;
    for(int i = 0; i < N; i++){
      if (t[i][j] > 0){
   k++;
    }
    }
    cout << k << " ";
  }
}

//lab4(5), task 5
#include <iostream>
using namespace std;
int main() {
  cout << "Cin razmer matiz ";
  int x, y, f=0, n=0;
  int sum1=0, sum2=0, ymn1=1, ymn2=1, x1=0, x2=0, x3=0, x4=0;
  cin >> x;
  y = x;
  int temp[x][y];
  for(int i = 0; i<x; i++){
    for(int j = 0; j<y; j++){
      cin >> temp[i][j];
    }
  }
  for(int i = 0; i<x; i++){
    for(int j = 0; j<y; j++){
     if((i == f)&&(j>n)){
       sum1 = temp[i][j] + sum1;
       if(temp[i][j]<0){
         sum2 = sum2 + temp[i][j];
         x2++;
       }
       x1++;
     }
     if((i == f)&&(j<n)){
       ymn1 = temp[i][j] * ymn1;
       if(temp[i][j]>0){
         ymn2 = ymn2 * temp[i][j];
         x4++;
       }
       x3++;
     }  
    }
    n++;
    f++;
  }
  cout << "1. " << ymn1 << " " << x3 << endl;
  cout << "2. " << sum1 << " " << x1 << endl;
  cout << "3. " << ymn2 << " " << x4 << endl;
  cout << "4. " << sum2 << " " << x2 << endl;
}
