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
#include <iostream>
#include <cctype>
#include <string>
#include <algorithm>
int main() {
  setlocale(LC_ALL, "Russian");
  std::cout << "Введите первую строку ";
  std::string temp;
  std::cin >> temp;
  std::cout << "Введите вторую строку ";
  std::string temp2;
  std::cin >> temp2;
  transform(temp.begin(), temp.end(), temp.begin(), tolower);
  transform(temp2.begin(), temp2.end(), temp2.begin(), tolower);
  bool result = temp == temp2;
  if(result == 1){
  std:: cout << "Строки равны";
  }
  else std:: cout << "Строки не равны";
}
//lab5(7), task 4
#include <iostream>
#include <cctype>
#include <string>
#include <algorithm>
int main() {
  setlocale(LC_ALL, "Russian");
  std::cout << "Введите первую строку ";
  std::string temp;
  std::string temp2;
  std::cin >> temp;
  transform(temp.begin(), temp.end(), temp.begin(), tolower);
  for(int i = 0;i<temp.length(); i++){
    if(temp[i] == ' '){
      temp.erase(i,1);
      i--;
    }
  }
  temp2 = temp;
  std::reverse(temp2.begin(), temp2.end());
  if(temp == temp2){
    std:: cout << "Строка является переветрышем";
  }
  else std:: cout << "Строка не является перевертышем";
  std:: cout << temp2;
}
