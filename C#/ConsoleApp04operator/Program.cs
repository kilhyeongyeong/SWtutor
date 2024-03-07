using System;

namespace ConsoleApp04operator
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            int x = 100;
            Console.WriteLine("x += 10 : " + (x += 10));
            Console.WriteLine("x += 10 : " + (x += 10));
            Console.WriteLine("x -= 10 : " + (x -= 10));
            Console.WriteLine("x -= 10 : " + (x -= 10));
            Console.WriteLine("====================");
            x = 15;
            Console.WriteLine(x + " &= 10 : " + (x &= 10));

            x = 15;
            Console.WriteLine(x + " |= 10 : " + (x |= 10));

            x = 15;
            Console.WriteLine(x + " <<= 1 : " + (x <<= 1));
            Console.WriteLine("====================");

            Console.WriteLine("5 == 5: " + (5 == 5));
            Console.WriteLine("5 != 5: " + (5 != 5));
            Console.WriteLine("5 >= 5: " + (5 >= 5));
            Console.WriteLine("5 <= 5: " + (5 <= 5));
            Console.WriteLine("5 > 5: " + (5 > 5));
            Console.WriteLine("5 < 5: " + (5 < 5));

            Console.WriteLine("====================");
            //string 비교
            string txt = "Hello c#!!";
            Console.WriteLine("CompareTo : " + (txt.CompareTo("Hello c#!!") == 0));
            Console.WriteLine("Equals : " + txt.Equals("Hello c#!!"));

            Console.WriteLine("====================");
            x = 200;
            Console.WriteLine(x >= 5? "big" : "small");

            x = 88;
            Console.WriteLine(x >= 90 ? "A" : x >= 80 ? "B" : "C");

            Console.WriteLine("======?? 연산자 null대체연산자==============");
            int? nullSu = 77;
            nullSu = nullSu ?? 0;
            Console.WriteLine("nullSu : " + nullSu);

            string nullStr = null;
            nullStr = nullStr ?? "yangssem";
            Console.WriteLine("nullStr : " + nullStr);
        }
    }
}
