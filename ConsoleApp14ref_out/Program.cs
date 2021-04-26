using System;

namespace ConsoleApp14method_ref_out
{
    class Calculate
    {
        public void Sum(ref int su1,ref int su2)
        {
            su1++;
            su2++;
            Console.WriteLine("{0} + {1} = {2}", su1, su2, su1 + su2);
        }

        public void Minus(int x, int y, out int su3, out int su4)
        {
            su3 = x - 10;
            su4 = y - 20;
            Console.WriteLine("{0}-{1}={2}", su3, su4, su3-su4);
        }
    }

    class Program
    {
        static void Method01(int age, string name, string phone)
        {
            Console.WriteLine("{0},{1},{2}",age, name, phone);
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Console.WriteLine("=====ref=====초기화필요=====");
            Calculate cal = new Calculate();
            int su1 = 100;
            int su2 = 200;
            cal.Sum(ref su1,ref su2);
            Console.WriteLine("Sum메소드 호출후에도 {0}, {1} 그대로 유지됨.", su1, su2);

            Console.WriteLine("=====out=====초기화 불필요=====");
            int su3, su4;
            cal.Minus(100, 200, out su3, out su4);
            Console.WriteLine("Minus메소드 호출후에도 {0}, {1} 그대로 유지됨.", su3, su4);

            Console.WriteLine("=====C# 4.0 : Named 파라미터=====");
            //메서드에 파라미터를 전달할 때, 일반적으로 파라미터 위치에 따라
            //순차적으로 파라미터가 넘겨지는데
            Method01(age:33, "kim", "02");
            //C# 4.0부터는 위치와 상관없이 파라미터명을 매핑하여
            //파라미터를 전달할 수 있게 하였다.
            //이러한 파라미터를 Named Parameter라 부른다
            Method01(name : "kim", phone : "02", age : 33);
        }
    }
}
