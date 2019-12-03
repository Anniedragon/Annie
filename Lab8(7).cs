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

//lab 8(7), task 6
using System;

class MainClass {
    
    static void Main(string[] args) {
            int a;
            Console.Write("Введите количество элементов в массиве: ");
            a = int.Parse(Console.ReadLine());
            Console.WriteLine("");
            int[] arr = new int[a];
            Random rand = new Random(); 
            for (int i = 0; i < arr.Length; i++) {   
                arr[i]= rand.Next(-99999, 99999);
            }
            int min, temp;
    int length = arr.Length;
    for (int i = 0; i < length - 1; i++)
    {
        min = i;
  
        for (int j = i + 1; j < length; j++)
        {
            if (arr[j] < arr[min])
            {
                min = j;
            }
        }
  
        if (min != i)
        {
            temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }
    Console.WriteLine("");
            for (int i = 0; i < arr.Length; i++){
                Console.Write(arr[i] + " ");
            }
            Console.WriteLine("");
            Console.WriteLine("");
}

}
