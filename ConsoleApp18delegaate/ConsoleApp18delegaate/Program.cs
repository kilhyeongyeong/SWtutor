using System;

namespace ConsoleApp18delegaate
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
            Console.WriteLine("Hello World! delegate 대리자");

            Calculator calc = new Calculator();
            int result = calc.Plus(100, 30);
            Console.WriteLine("result : " + result);

            result = calc.Minus(100, 30);
            Console.WriteLine("result : " + result);

            MyDelegate Callback;

            Callback = new MyDelegate(calc.Plus);

            result = Callback(200, 50);
            Console.WriteLine("result : " + result);

            result = new MyDelegate(calc.Plus)(2000, 500);
            Console.WriteLine("result : " + result);

            result = new MyDelegate(calc.Minus)(2000, 500);
            Console.WriteLine("result : " + result);

            // 익명 메소드로 초기화
            MyDelegate MyCallback;

            MyCallback = delegate (int x, int y)
            {
                return x * y;
            };

            result = MyCallback(11, 22);
            Console.WriteLine("result : " + result);
        }
    }
}
