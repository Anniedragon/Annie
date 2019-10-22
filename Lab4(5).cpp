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
