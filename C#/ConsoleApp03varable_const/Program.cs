using System;

namespace ConsoleApp03varable_const
{
    class Program
    {
        string model = "BMW";
        const string model2 = "BMW2";

        readonly string name = "yangssem";

        Program() 
        {
            name = "lee"; //readonly = 생성자에서는 변경 가능
            //but const는 생성자에서도 변경 불가
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            const int x = 100;
            //readonly : 지역변수에서는 사용 불가
            Console.WriteLine("x : " + x);

            Program p = new Program();
            Console.WriteLine("model : " + p.model); //전역변수의 경우 const일때는 객체명으로 접근 안됨
            Console.WriteLine("model : " + Program.model2); //전역변수의 경우 const일때는 클래스명으로 접근
            Console.WriteLine("model : " + p.name); //readonly 객체명으로 접근가능

        }
    }
}
