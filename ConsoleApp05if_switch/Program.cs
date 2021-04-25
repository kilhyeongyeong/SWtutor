using System;

namespace ConsoleApp05if_switch
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            bool b = true;
            if (b)
            {
                Console.WriteLine("True!!");
            }
            Console.WriteLine("-----------------------------");
            b = false;
            if (b)
            {
                Console.WriteLine("True!!");
            }
            else
            {
                Console.WriteLine("false~~");
            }
            Console.WriteLine("-----------------------------");
            int avg = 90;
            if(avg >= 90)
            {
                Console.WriteLine("A");
            }
            else if (avg >= 80)
            {
                Console.WriteLine("B");
            }
            else if (avg >= 70)
            {
                Console.WriteLine("C");
            }
            else if (avg >= 60)
            {
                Console.WriteLine("D");
            }
            else
            {
                Console.WriteLine("F");
            }
            Console.WriteLine("-----------------------------");
            int su = 88;
            switch (su / 10)
            {
                case 10:
                case 9:
                    Console.WriteLine("A");
                    break;
                case 8:
                    Console.WriteLine("B");
                    break;
                case 7:
                    Console.WriteLine("C");
                    break;
                default:
                    Console.WriteLine("F");
                    break;
            }

            Console.WriteLine("-----------------------------");
            char c = '*';
            switch (c)
            {
                case '+':
                    Console.WriteLine("더하기");
                    break;
                case '-':
                    Console.WriteLine("빼기");
                    break;
                case '*':
                    Console.WriteLine("곱하기");
                    break;
                case '/':
                    Console.WriteLine("나누기");
                    break;
                default:
                    Console.WriteLine("잘못입력");
                    break;
            }
            Console.WriteLine("-----------------------------");
            string menu = "insert";
            switch (menu)
            {
                case "insert":
                    Console.WriteLine("입력");
                    break;
                case "update":
                    Console.WriteLine("수정");
                    break;
                case "delete":
                    Console.WriteLine("삭제");
                    break;
                case "select":
                    Console.WriteLine("검색");
                    break;
                default:
                    Console.WriteLine("잘못선택");
                    break;
            }
        }
    }
}
