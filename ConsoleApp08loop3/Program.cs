using System;

namespace ConsoleApp08loop3
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            ConsoleKeyInfo keyInfo;
            do
            {
                Console.WriteLine("종료시 [x]입력 : ");
                keyInfo = Console.ReadKey();
            } while (keyInfo.Key != ConsoleKey.X);

            do
            {
                
            } while (keyInfo.Key != ConsoleKey.X);
        }


    }
}
