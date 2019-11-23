using System;
class MainClass {
  public static void Main (string[] args) {
    int a, c;
    int j=0;  
    int[] m = {0,0,0,0,0,0,0,0,0,0}; 
    Console.WriteLine ("Cin number < 10000000000");
    a = Convert.ToInt32(Console.ReadLine());
    while (a>0) {
      c=a%10;
      a/=10;
      m[j]=c;
      j++;
    }
    for(int q=j-1; q>=0; q--){
      Console.WriteLine (m[q]);
    }
  }
}
