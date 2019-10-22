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

//lab 4(5), task 2 In progress
#include <iostream>
using namespace std;
int main() {
  int N;
  int k = 0;
  int temp = 0;
  int maxi = 0;
  int maxj = 0;
  cout << "Enter N ";
    cin >> N;
  int A[N][N];
  for (int i=1; i<=N; i++) {
    for (int j=1; j<=N; j++) {
        cout << "Enter element ";
        cin >> A[i][j];
      }
    }
  int max = A[0][0];
  for (int i=0; i<=N; i++) {
    for (int j=0; j<=N; j++) {
      if (j <= N) {
        if (A[i][j] > max) {
          max = A[i][j];
          maxi = i;
          maxj = j;
        }
        cout << max << endl;
      }
      if (i == j) {
        temp = A[i][j];
        A[i][j] = A[maxi][maxj];
        A[maxi][maxj] = temp;
      }
    }
  }
  for (int i=0; i<=N; i++) {
    for (int j=0; j<=N; j++) {
      if (j == N) {
        cout << A[i][j] << endl;
      }
      else cout << A[i][j] << " ";
    }
  }
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
