using System;
using System.Linq;

namespace ConsoleApp19Lambda
{
    // 네임 스페이스 영역이나 클래스 영역에서만 선언 가능
    delegate int Calculate(int x, int y);
    delegate int Calculate2();
    delegate void Calculate3(int x, int y);
    delegate void Calculate4();
    class Profile
    {
        public string Name { get; set; }
        public int Age { get; set; }
        public override string ToString()
        {
            return "Profile : Name : "+Name+", Age : "+Age;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            //Calculate cal = delegate (int x, int y)
            //{
            //    return x + y;
            //};

            //Calculate cal = (int x, int y) =>
            //{
            //    return x + y;
            //};

            Calculate cal = (int x, int y) => x + y; // 함수를 변수에 할당 : 델리게이트를 이용          
            int result = cal(11, 22);
            Console.WriteLine("result : " + result);

            Calculate2 cal2 = () => 10 * 10;
            result = cal2();
            Console.WriteLine("result : " + result);

            Calculate3 cal3 = (x, y) =>
            {
                Console.WriteLine(x / y);
            };
            cal3(100,5);

            Calculate4 cal4 = () => Console.WriteLine("lambda cal4()");
            cal4();

            test1(cal); // 덧셈하는 델리게이트 람다 함수
            test1((int x, int y) => x* y); // 곱셈하는 람다 함수
             
            // Func : 리턴 하는 값이 있는 람다 함수용
            Func<int, int, int> fn1 = (x, y) => x + y;
            Console.WriteLine(fn1(44,55));

            test2(fn1);
            test2((x, y) => x - y);

            Func<int> fn2 = () => 100;
            Console.WriteLine(fn2());

            Func<int,double> fn3= (x) => x * 2.0;
            Console.WriteLine(fn3(33));

            //Action : 리턴 값이 없는 람다 함수용
            Action<int> act = (x) => Console.WriteLine("x : " + x);
            act(100);

            int sum = 0;
            Action<int> act2 = (x) => sum += x;
            act2(100);
            Console.WriteLine("sum : " + sum);
            act2(100);
            Console.WriteLine("sum : " + sum);
            act2(100);
            Console.WriteLine("sum : " + sum);

            test3(act);

            Console.WriteLine("===================LINQ=====================");
            Profile[] pArray =
            {
                new Profile() {Name = "kim", Age = 33 },
                new Profile() {Name = "lee", Age = 22 },
                new Profile() {Name = "choi", Age = 11 },
                new Profile() {Name = "han", Age = 55 }
            };

            foreach (var p in pArray)
            {
                Console.WriteLine(p);
            }

            Console.WriteLine("=====================================");
            // 주어진 배열을 이용하여 33세 이하의 사람들의 이름순으로 출력하도록 구현
            var ps = from p in pArray
                     where p.Age <= 33
                     //orderby p.Name 
                     orderby p.Name descending
                     select p;
            foreach (var p in ps)
            {
                Console.WriteLine(p);
            }
        }
        static void test1(Calculate cal)
        {
            Console.WriteLine(cal(10,10));
        }
        static void test2(Func<int, int, int> fn)
        {
            Console.WriteLine(fn(11,22));
        }
        static void test3(Action<int> act)
        {
            act(999);
        }
    }
}
