using System;

namespace ConsoleApp07loop2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            /*int i = 0;
            while (true)
            {
                Console.WriteLine(i);
                i++;

                if (i == 5) break;
            }

            ConsoleKeyInfo keyInfo;
            while (true)
            {
                Console.WriteLine("종료시 [X/x] 입력");
                keyInfo = Console.ReadKey();
                Console.WriteLine();
                if(keyInfo.Key == ConsoleKey.X)
                {
                    break;
                }
            }*/

            //회원가입을 무한히 받기
            //x를 입력하면 종료
            //아이디, 비번, 이름, 폰번 입력받기

            int num = 1;
            ConsoleKeyInfo keyInfo;
            while (true)
            {
                Console.Write("아이디를 입력하세요.>> ");
                string id = Console.ReadLine();
                Console.Write("비밀번호를 입력하세요.>> ");
                string pw = Console.ReadLine();
                Console.Write("이름을 입력하세요>> ");
                string name = Console.ReadLine();
                Console.Write("핸드폰 번호를 입력하세요.>> ");
                string phone = Console.ReadLine();

                Console.WriteLine("{0}. {1} : {2} : {3} : {4}", num, id, pw, name, phone);
                num++;
                Console.Write("종료시 [X/x] 입력.>> ");
                keyInfo = Console.ReadKey();
                Console.WriteLine();
                if (keyInfo.Key == ConsoleKey.X)
                {
                    break;
                }
            }
        }
    }
}
