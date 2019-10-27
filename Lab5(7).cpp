//lab5(7), task 1
#include <iostream>
#include <string>
using namespace std;
int main() {
  setlocale(LC_ALL, "Russian");
  cout << "Введите строку" << endl;
  string temp;
  cin >> temp;
  cout << temp.length();
}
//lab5(7), task 2
#include <iostream>
#include <cctype>
#include <string>
#include <algorithm>
int main() {
  setlocale(LC_ALL, "Russian");
  std::cout << "Введите строку ";
  std::string temp;
  std::cin >> temp;
  transform(temp.begin(), temp.end(), temp.begin(), tolower);
  std::cout << temp; 
}
//lab5(7), task 3
//lab5(7), task 4
