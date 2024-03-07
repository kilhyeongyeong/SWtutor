using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");  //자동완성 >> cw Tab Tab
            System.Console.WriteLine("Hello World!");

            Console.Write('A');
            Console.Write('B');
            Console.Write('C');
            Console.Write("DEF");

            Console.WriteLine();

            Console.WriteLine("Hello {0} {1} {2}", 11, 22, 33);
            Console.WriteLine("Hello {0} {1} {2}", "kim", "lee", "yangssem");

            Console.WriteLine("Hello {0}", 10.0); //.0일때는 표시못함
            Console.WriteLine("Hello {0}", 10.9);
            Console.WriteLine("Hello {0:0.0}", 10.0); //.0일때도 표시
            Console.WriteLine("Hello {0:0.0}", 10.9);
            Console.WriteLine("Hello {0:0.0}", 10.56789);//버려지는부분은 반올림 처리
            Console.WriteLine("Hello {0:0.00}", 10.56789);
            Console.WriteLine("Hello {0:0.000}", 10.56789);
        }
    }
}
