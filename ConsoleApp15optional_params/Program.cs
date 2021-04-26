using System;

namespace ConsoleApp15optional_params
{
    class Calculate
    {
        public void Cal(int su1, int su2, string key = "+")
        {
            Console.WriteLine("key : {0}", key);
            switch (key)
            {
                case "+":
                    Console.WriteLine("{0}+{1}={2}", su1, su2, su1 + su2);
                    break;
                case "-":
                    Console.WriteLine("{0}-{1}={2}", su1, su2, su1 - su2);
                    break;
                case "*":
                    Console.WriteLine("{0}*{1}={2}", su1, su2, su1 * su2);
                    break;
                case "/":
                    Console.WriteLine("{0}/{1}={2}", su1, su2, su1 / su2);
                    break;
                default:
                    break;
            }
        }
        public void Sum(params int[] sus)
        {
            int sum = 0;
            foreach (var su in sus)
            {
                sum += su;
            }
            Console.WriteLine("sum : {0}", sum);
        }

        public void Info(params string[] names)
        {
            foreach (var name in names)
            {
                Console.WriteLine(name);
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            /*C# 4.0에서부터 어떤 메서드의 파라미터가 디폴드 값을 갖고 있다면,
            메서드 호출시 이러한 파라미터를 생략하는 것을 허용하였다.
            이렇게 디폴트 값을 가진 파라미터를 Optional 파라미터라고 한다.
            optionqal 파라미터는 반드시 파라미터들 중 맨 마지막에 놓여져야 한다.
            복수개의 Optional 파라미터가 있는 경우
            반드시 Optional 이 아닌 파라미터들 뒤에 위치해야 한다.
            */

            Calculate cal = new Calculate();
            int su1 = 100;
            int su2 = 200;
            cal.Cal(su1, su2);
            cal.Cal(su1, su2,"*");
            cal.Cal(su1, su2);
            cal.Cal(su1, su2,"/");

            Console.WriteLine("====가변인자를 받는 params====");
            /*일반적으로 메서드의 파라미터 갯수는 고정되어 있다.
             * 하지만 어떤 경우는 파라미터의 갯수를 파라미터의 갯수를 미리 알 수 없는 경우도 있는데
             * 이런 경우 C# 키워드 params를 사용한다.
             * 이 params키워드는 가변적인 배열을 인수로 갖게 해주는데,
             * 파라미터들 중 반드시 하나만 존재해야 하며, 맨 마지막에 위치해야 한다.
             */
            cal.Sum(1, 2, 3, 4, 5);
            cal.Sum(7,8,9);
            cal.Sum(new int[] { 10,20,30,40,50});

            cal.Info("aaa", "bbb", "ccc");
            cal.Info("xxx", "yyy");
            cal.Info(new string[] { "kim", "lee", "han","choi","yang","yoo"});
        }
    }
}
