using System;
using System.Text;

namespace ConsoleApp10StringBuilder
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            //Mutable 타입인 StringBuilder 클래스는
            //문자열 갱신이 많은 곳에서 자주 사용되는데
            //이는 이 클래스가 별도 메모리를 생성, 소멸 하지 않고
            //일정한 버퍼를 갖고 문자열 갱신을 효율적으로 처리하기 때문이다.
            //System.Text,StringBuilder sb = new System.Text,StringBuilder();

            StringBuilder sb = new StringBuilder();
            DateTime startTime = DateTime.Now;

            for (int i = 0; i < 100000; i++)
            {
                sb.Append("Hello" + i);
            }

            TimeSpan ts = DateTime.Now - startTime;
            Console.WriteLine(ts);
        }
    }
}
