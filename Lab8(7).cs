//lab 8(7) task 1
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace Lab8_task1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Введите коэффициенты первого уравнения: ");
            int a1 = Convert.ToInt32(Console.ReadLine());
            int b1 = Convert.ToInt32(Console.ReadLine());
            int c1 = Convert.ToInt32(Console.ReadLine());
            int d1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите коэффициенты второго уравнения: ");
            int a2 = Convert.ToInt32(Console.ReadLine());
            int b2 = Convert.ToInt32(Console.ReadLine());
            int c2 = Convert.ToInt32(Console.ReadLine());
            int d2 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите коэффициенты третьего уравнения: ");
            int a3 = Convert.ToInt32(Console.ReadLine());
            int b3 = Convert.ToInt32(Console.ReadLine());
            int c3 = Convert.ToInt32(Console.ReadLine());
            int d3 = Convert.ToInt32(Console.ReadLine());

            double o = a1 * b2 * c3 + a2 * b3 * c1 + a3 * b1 * c2 - (a3 * b2 * c1 + a2 * b1 * c3 + a1 * b3 * c2);
            double o1 = d1 * b2 * c3 + d2 * b3 * c1 + d3 * b1 * c2 - (d3 * b2 * c1 + d2 * b1 * c3 + d1 * b3 * c2);
            double o2 = a1 * d2 * c3 + a2 * d3 * c1 + a3 * d1 * c2 - (a3 * d2 * c1 + a2 * d1 * c3 + a1 * d3 * c2);
            double o3 = a1 * b2 * d3 + a2 * b3 * d1 + a3 * b1 * d2 - (a3 * b2 * d1 + a2 * b1 * d3 + a1 * b3 * d2);
            double x = o1 / o;
            double y = o2 / o;
            double z = o3 / o;

            Console.WriteLine("x = {0}, y = {1}, z = {2}", x, y, z);
            Console.Read();
        }
    }
}

//lab 8(7), task 2
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace Lab8_task2
{
    class Program
    {
        static void Main(string[] args)
        {
            const float Eps = 1e-10f;
            Console.WriteLine("Введите число, из которого нужно извлечь корень: ");
            int q = Convert.ToInt32(Console.ReadLine());
            double xc = 1;
            double xn = q;
            while (Math.Abs(xn - xc) >= Eps) {
            xc = xn;
            xn = (xc + q / xc) / 2;
            }
            Console.WriteLine("Корень по формуле Ньютона: {0}", xn);
            Console.WriteLine("Корень по стандартному виду: {0}", Math.Sqrt(q));
            Console.Read();
        }
    }
}

//lab 8(7) task 3
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace Lab8_task3
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите число: ");
            int N = Convert.ToInt32(Console.ReadLine());
            int n, k;
            while (N > 10)
            {
                n = N;
                k = 0;
                while (n > 10)
                {
                    n /= 10;
                    k++;
                }
                Console.WriteLine(n);
                N = N % Convert.ToInt32(Math.Pow(10, k));

            }
            Console.WriteLine(N);
            Console.Read();
        }
    }
}

//lab 8(7), task 4
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab8_task4
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите N: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int[] A = new int[n];
            A[0] = 1;
            Console.Write(A[0]);
            Console.WriteLine();
            for (int i = 1; i < n; i++)
            {
                int l = 0;
                for (int j = 0; j <= i; j++)
                {
                    int p = A[j];
                    A[j] += l;
                    l = p;
                    Console.Write(A[j]);
                    Console.Write(" ");
                }
                Console.WriteLine(" ");
            }
            Console.Read();
        }
    }
}

//lab 8(7), task 5
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
namespace Lab8_task5
{
    class Program
    {
        static void Main(string[] args)
        {
            int s, max;
            string i, o, Filename;
            string[] A;
            Filename = "Laba_text.txt";

            Console.WriteLine("1 - Запись в текстовый файл информации, вводимой с клавиатуры");
            Console.WriteLine("2 - Считывание на экран информации из текстового файла");
            Console.WriteLine("3 - Построчное считывание строк файла и их перезапись задом наперед");
            Console.WriteLine("4 - Поиск и вывод самой длинной строки в файле");
            Console.WriteLine("5 - Перемешивание строк в файле случайным образом");
            Console.WriteLine("6 - Удаление всех строк из файла");
        again:
            Console.Write("Номер действия: ");
            s = Convert.ToInt32(Console.ReadLine());

            switch (s)
            {
                case 1:
                    Console.WriteLine("Введите текст: ");
                    i = Console.ReadLine();
                    File.AppendAllText(Filename, i);
                    File.AppendAllText(Filename, "\n");
                    break;
                case 2:
                    o = File.ReadAllText(Filename);
                    Console.WriteLine("Информации из текстового файла: {0}", o);
                    break;
                case 3:
                    A = File.ReadAllLines(Filename);
                    File.WriteAllText(Filename, null);
                    for (int j = 0; j < A.Length / 2; j++)
                    {
                        string tmp = A[j];
                        A[j] = A[A.Length - 1 - j];
                        A[A.Length - 1 - j] = tmp;
                    };
                    File.WriteAllLines(Filename, A);
                    break;
                case 4:
                    max = -1;
                    A = File.ReadAllLines(Filename);
                    for (int j = 0; j < A.GetLength(0); j++)
                    {
                        if (A[j].Length > max) {
                            max = A[j].Length;
                        };
                    };
                    for (int j = 0; j < A.GetLength(0); j++)
                    {
                        if (A[j].Length == max) {
                            Console.WriteLine("Самая длинная строка в файле: {0}", A[j]);
                            break;
                        };
                    };
                    break;
                case 5:
                    A = File.ReadAllLines(Filename);
                    Random rand = new Random();
                    for (int j = A.Length - 1; j >= 1; j--)
                    {
                        int k = rand.Next(j + 1);
                        string tmp = A[k];
                        A[k] = A[j];
                        A[j] = tmp;
                    };
                    File.WriteAllText(Filename, null);
                    File.WriteAllLines(Filename, A);
                    break;
                case 6:
                    File.WriteAllText(Filename, null);
                    break;
            }
            goto again;
        }
    }
}

//lab 8(7), task 6
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
namespace Lab8_task6
{
    class Program
    {
        public static TimeSpan Bubble(int[] A){
            Stopwatch sWatch = new Stopwatch();
            TimeSpan k;
            int l = 0;
            int[] B = new int[A.Length];
            for (int i = 0; i < A.Length; i++) {
                B[i] = A[i];
            }
            sWatch.Start();
            for (int j = 0; j < A.Length - 1; j++) {
                for (int i = 1; i < A.Length - 1 - j; i++) {
                    if (A[i - 1] > A[i]) {
                        int p = A[i - 1];
                        A[i - 1] = A[i];
                        A[i] = p;
                        l++;
                    }
                }
            }
            sWatch.Stop();
            for (int i = 0; i < A.Length; i++)
            {
                A[i] = B[i];
            }
            k = sWatch.Elapsed;
            Console.WriteLine("Сортировка Пузырек: ");
            Console.WriteLine("Время - {0}", k);
            Console.WriteLine("Количество итераций - {0}", l);
            Console.WriteLine();
            return k;
        }
        public static TimeSpan Select(int[] A)
        {
            Stopwatch sWatch = new Stopwatch();
            TimeSpan k;
            int l = 0;
            int i, j, p, s;
            int[] B = new int[A.Length];
            for (i = 0; i < A.Length; i++)
            {
                B[i] = A[i];
            }
            sWatch.Start();
            for (j = 0; j < A.Length - 1; j++)
            {
                p = j;
                for (i = j + 1; i < A.Length; i++)
                {
                    if (A[i] < A[p])
                    {
                        p = i;
                        l++;
                    }
                }
                s = A[j];
                A[j] = A[p];
                A[p] = s;
            }
            sWatch.Stop();
            for (i = 0; i < A.Length; i++)
            {
                A[i] = B[i];
            }
            k = sWatch.Elapsed; 
            Console.WriteLine("Сортировка выбором: ");
            Console.WriteLine("Время - {0}", k);
            Console.WriteLine("Количество итераций - {0}", l);
            Console.WriteLine();
            return k;
        }
        public static TimeSpan Insert(int[] A)
        {
            Stopwatch sWatch = new Stopwatch();
            TimeSpan k;
            int l = 0;
            int i, j, p;
            int[] B = new int[A.Length];
            for (i = 0; i < A.Length; i++)
            {
                B[i] = A[i];
            }
            sWatch.Start();
            for (i = 0; i < A.Length; i++)
            {
                p = A[i];
                for (j = i - 1; j >= 0 && A[j] > p; j--)
                {
                    A[j + 1] = A[j];
                    l++;
                }
                A[j + 1] = p;
            }
            sWatch.Stop();
            for (i = 0; i < A.Length; i++)
            {
                A[i] = B[i];
            }
            k = sWatch.Elapsed;
            Console.WriteLine("Сортировка вставками: ");
            Console.WriteLine("Время - {0}", k);
            Console.WriteLine("Количество итераций - {0}", l);
            Console.WriteLine();
            return k;
        }
        public static TimeSpan Gnome(int[] A)
        {
            Stopwatch sWatch = new Stopwatch();
            TimeSpan k;
            int l = 0;
            int i, p;
            int[] B = new int[A.Length];
            for (i = 0; i < A.Length; i++)
            {
                B[i] = A[i];
            }
            sWatch.Start();
            i = 0;
            while (i < A.Length)
            {
                if (i == 0 || A[i - 1] <= A[i])
                    i++;
                else
                {
                    p = A[i];
                    A[i] = A[i - 1];
                    A[i - 1] = p;
                    i--;
                    l++;
                }
            }
            sWatch.Stop();
            for (i = 0; i < A.Length; i++)
            {
                A[i] = B[i];
            }
            k = sWatch.Elapsed;
            Console.WriteLine("Сортировка гномья: ");
            Console.WriteLine("Время - {0}", k);
            Console.WriteLine("Количество итераций - {0}", l);
            Console.WriteLine();
            return k;
        }
        public static TimeSpan Quick(int[] A, int first, int last)
        {
            Stopwatch sWatch = new Stopwatch();
            TimeSpan k;
            int l = 0;
            int i, j, p, s;
            int[] B = new int[A.Length];
            for (i = 0; i < A.Length; i++)
            {
                B[i] = A[i];
            }
            sWatch.Start();
            s = A[(last - first) / 2 + first];
            i = first;
            j = last;
            while (i <= j)
            {
                while (A[i] < s && i <= last) i++;
                while (A[j] > s && j >= first) j--;
                if (i <= j)
                {
                    p = A[i];
                    A[i] = A[j];
                    A[j] = p;
                    i++;
                    j--;
                    l++;
                }
            }
            if (j > first)
            {
                Quick(A, first, j);
            }
            if (i < last) { 
                Quick(A, i, last);
            }
            sWatch.Stop();
            for (i = 0; i < A.Length; i++)
            {
                A[i] = B[i];
            }
            k = sWatch.Elapsed;
            return k;
        }
        static void Main(string[] args)
        {
            int[] A = new int[1000];
            Random rand = new Random();
            for (int i = 0; i < A.Length; i++)
                A[i] = rand.Next();
            int[] B = new int[10000];
            for (int i = 0; i < B.Length; i++)
                B[i] = rand.Next();
            int[] C = new int[100000];
            for (int i = 0; i < C.Length; i++)
                C[i] = rand.Next();
            int[] D = new int[1000000];
            for (int i = 0; i < D.Length; i++)
                D[i] = rand.Next();
            int[] E = new int[10000000];
            for (int i = 0; i < E.Length; i++)
                E[i] = rand.Next();

            TimeSpan k;

            Console.WriteLine("Сортиовка массива на 1000: ");
            Console.WriteLine();
            Console.WriteLine();
            Bubble(A);
            Select(A);
            Insert(A);
            Gnome(A);
            k = Quick(A, 0 , A.Length - 1);
            Console.WriteLine("Быстрая сортировка: ");
            Console.WriteLine("Время - {0}", k);
            Console.WriteLine();
            Console.WriteLine();

            Console.WriteLine("Сортиовка массива на 10000: ");
            Console.WriteLine();
            Bubble(B);
            Select(B);
            Insert(B);
            Gnome(B);
            k = Quick(B, 0, B.Length - 1);
            Console.WriteLine("Быстрая сортировка: ");
            Console.WriteLine("Время - {0}", k);
            Console.WriteLine();
            Console.WriteLine();

            Console.WriteLine("Сортиовка массива на 100000: ");
            Console.WriteLine();
            Bubble(C);
            Select(C);
            Insert(C);
            Gnome(C);
            k = Quick(C, 0, C.Length - 1);
            Console.WriteLine("Быстрая сортировка: ");
            Console.WriteLine("Время - {0}", k);
            Console.WriteLine();
            Console.WriteLine();

            Console.WriteLine("Сортиовка массива на 1000000: ");
            Console.WriteLine();
            Bubble(D);
            Select(D);
            Insert(D);
            Gnome(D);
            k = Quick(D, 0, D.Length - 1);
            Console.WriteLine("Быстрая сортировка: ");
            Console.WriteLine("Время - {0}", k);
            Console.WriteLine();
            Console.WriteLine();

            Console.WriteLine("Сортиовка массива на 10000000: ");
            Console.WriteLine();
            Bubble(E);
            Select(E);
            Insert(E);
            Gnome(E);
            k = Quick(E, 0, E.Length - 1);
            Console.WriteLine("Быстрая сортировка: ");
            Console.WriteLine("Время - {0}", k);
            Console.WriteLine();
            Console.WriteLine();

            Console.Read();
        }
    }
}
