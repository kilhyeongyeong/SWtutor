using System;
using System.Linq;

namespace ConsoleApp19Lambda
{
    //네임스페이스 영역이나 클래스 영역에만 선언가능
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
            return "Profile : Name : " + Name + ", Age: " + Age;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            /*Calculate cal = delegate (int x, int y)
            {
                return x + y;
            };*/

            /*Calculate cal = (int x, int y) => 
            {
                return x + y;
            };*/

            //함수를 변수에 할당 : 델리케이트 활용
            Calculate cal = (int x, int y) => x + y;

            int result = cal(11, 22);
            Console.WriteLine("result : " + result);

            Calculate2 cal2 = () => 10 * 10;
            result = cal2();
            Console.WriteLine("result : " + result);

            Calculate3 cal3 = (int x, int y) => {
                Console.WriteLine(x / y);
            };

            cal3(100, 5);

            Calculate4 cal4 = () => Console.WriteLine("cal4()");

            cal4();

            test1(cal); //덧셈하는 델리케이트 람다함수
            test1((int x, int y) => x * y); //곱셈하는 람다함수


            //Func : 리턴하는 값이 있는 람다 함수용
            Func<int, int, int> fn1 = (x, y) => x + y;
            Console.WriteLine(fn1(44, 55));

            test2(fn1);
            test2((x, y) => x - y);

            Func<int> fn2 = () => 100;
            Console.WriteLine(fn2());

            Func<int, double> fn3 = (x) => x * 33.33;
            Console.WriteLine(fn3(33));

            //리턴값이 없는 람다 함수용
            Action<int> act = (x) => Console.WriteLine("Action x : " + x);
            act(100);

            int sum = 0;
            Action<int> act2 = (x) => sum += x;
            Console.WriteLine("sum : " + sum);
            act2(100);
            Console.WriteLine("sum : " + sum);
            act2(100);
            Console.WriteLine("sum : " + sum);
            act2(100);
            Console.WriteLine("sum : " + sum);

            test3(act);

            Console.WriteLine("============LINQ==================");
            Profile[] pArray =
            {
                new Profile(){ Name="kim", Age=33}, 
                new Profile(){ Name="lee", Age=22}, 
                new Profile(){ Name="choi", Age=11}, 
                new Profile(){ Name="ann", Age=55}
            };

            foreach (var p in pArray)
            {
                Console.WriteLine(p);
            }

            var ps = from p in pArray
                     where p.Age <= 33
                     orderby p.Name
                     select p;

            foreach (var p in ps)
            {
                Console.WriteLine(p);
            }
        }

        static void test1(Calculate cal)
        {
            Console.WriteLine(cal(55,55));
        }

        static void test2(Func<int, int, int> fn)
        {
            Console.WriteLine(fn(111,222));
        }

        static void test3(Action<int> act)
        {
            act(999);
        }
    }
}
