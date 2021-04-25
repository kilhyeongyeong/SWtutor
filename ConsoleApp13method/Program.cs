using System;

namespace ConsoleApp13method
{
    class Calculate
    {
        public void Sum(int su1, int su2)
        {
            su1++;
            su2++;
            Console.WriteLine("{0} + {1} = {2}", su1, su2, su1+su2);
        }
    }

    class Program
    {
        static void method1()
        {
            Console.WriteLine("method1()....");
        }

        static int method2()
        {
            Console.WriteLine("method2()....");
            return 100;
        }

        static void method3(int x, int y)
        {
            Console.WriteLine("method3(int x, int y)....{0} {1}", x,y);
        }

        static string method4(string x, string y)
        {
            Console.WriteLine("method3(int x, int y)....{0} {1}", x, y);
            return "hello c#";
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("=====메소드 정의방식===== 인자도 없고 리턴도 없고====");
            method1();
            Console.WriteLine("=====메소드 정의방식===== 인자도 없고 리턴은 있고====");
            int result = method2();
            Console.WriteLine("result : " + result);
            Console.WriteLine("=====메소드 정의방식===== 인자는 있고 리턴도 없고====");
            method3(99,88);
            Console.WriteLine("=====메소드 정의방식===== 인자도 있고 리턴도 있고====");
            string msg = method4("kim", "lee");
            Console.WriteLine("msg : " + msg);

            Console.WriteLine("=====Pass by Value 방식====");
            //전달된 인수를 메서드 내에서 변경한다해도
            //메서드가 끝나고 함수가 리턴된 후, 전달되었던 인수의 값은
            //호출자에서 원래 값 그대로 유지된다.
            Calculate cal = new Calculate();

            int su1 = 100;
            int su2 = 200;
            cal.Sum(su1, su2);
            Console.WriteLine("Sum메소드 호출후에도 {0}, {1} 그대로 유지됨.",su1,su2);
        }
    }
}
