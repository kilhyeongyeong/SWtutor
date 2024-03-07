using System;

namespace ConsoleApp18delegate
{
    delegate int MyDelegate(int x, int y);

    class Calculator
    {
        public int Plus(int x, int y)
        {
            return x + y;
        }

        public int Minus(int x, int y)
        {
            return x - y;
        }

    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Calculator calc = new Calculator();

            int res = calc.Plus(100, 30);
            Console.WriteLine("res = " + res);

            res = calc.Minus(100, 30);
            Console.WriteLine("res = " + res);

            MyDelegate Callback;

            Callback = new MyDelegate(calc.Plus);
            res = Callback(200, 50);
            Console.WriteLine("res : " + res);

            res = new MyDelegate(calc.Plus)(2000, 500);
            Console.WriteLine("res : " + res);

            res = new MyDelegate(calc.Minus)(2000, 500);
            Console.WriteLine("res : " + res);


            //익명메소드로 초기화
            MyDelegate myCallback;

            myCallback = delegate (int x, int y)
            {
                return x * y;
            };

            res = myCallback(35, 35);
            Console.WriteLine("res : " + res);
        }
    }
}
