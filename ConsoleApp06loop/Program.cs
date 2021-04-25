using System;

namespace ConsoleApp06loop
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            /*for(int i=0; i<10; i++)
            {
                Console.WriteLine("i : {0}", i);
            }
            Console.WriteLine("----------------------------------");
            for (int i = 10; i > 0; i--)
            {
                Console.WriteLine("i : {0}", i);
            }
            Console.WriteLine("----------------------------------");
            for (char i = 'A'; i <= 'Z'; i++)
            {
                Console.WriteLine("{0} : {1}", i, (int)i);
            }
            Console.WriteLine("----------------------------------");
            for (char i = '가'; i < '나'; i++)
            {
                Console.WriteLine("{0} : {1}", i, (int)i);
            }
            Console.WriteLine("----------------------------------");
            for (double i = 1.0; i < 2.0; i+=0.1)
            {
                Console.WriteLine("i : {0:0.0}", i);
            }*/

            //콘솔에서 텍스트 입력받기 : Console.readLine();
            /* Console.WriteLine("-------------------------------------------");
             for(int i=0; i<3; i++)
             {
                 string kor = Console.ReadLine();
                 Console.WriteLine(kor + 100);
                 Console.WriteLine(int.Parse(kor) + 100);
             }*/

            /*for(int x = 0; x<3; x++)
            {
                for(int i=0; i<10; i++)
                {
                    Console.Write(i + " ");
                }
                Console.WriteLine();
            }*/

            /*for (int x = 0; x < 3; x++)
            {
                for (int i = 0; i < 10; i++)
                {
                    Console.Write(i + " ");
                    if (i == 5) break;
                    //if(i==5) continue;
                }
                Console.WriteLine();
            }*/

            /*string[] names = new string[] { "kim", "lee", "yangssem" };
            foreach (string item in names)
            {
                Console.WriteLine(item);
            }

            foreach(var item in names)
            {
                Console.WriteLine(item);
            }*/

            /*int[] sus = new int[] { 11, 22, 33 };

            foreach(int item in sus)
            {
                Console.Write(item + " ");
            }

            foreach(var item in sus)
            {
                Console.Write(item + " ");
            }*/

            Console.WriteLine("구구단");
            for(int i=2; i<10; i++)
            {
                for(int j=1; j<10; j++)
                {
                    Console.Write("{0} * {1} = {2} \t", i, j, i*j);
                }
                Console.WriteLine();
            }

            Console.WriteLine("성적증명서");

            for (int i=1; i<=3; i++)
            {
                Console.Write("이름을 입력하세요>>");
                string name = Console.ReadLine();
                Console.Write("국어 점수를 입력하세요>>");
                int kor = int.Parse(Console.ReadLine());
                Console.Write("영어 점수를 입력하세요>>");
                int eng = int.Parse(Console.ReadLine());
                Console.Write("수학 점수를 입력하세요>>");
                int math = int.Parse(Console.ReadLine());

                int total = kor + eng + math;
                double avg = total / 3.0;

                char grade = 'F';
                switch ((int)avg / 10)
                {
                    case 10:
                    case 9:
                        grade = 'A';
                        break;
                    case 8:
                        grade = 'B';
                        break;
                    case 7:
                        grade = 'C';
                        break;
                    case 6:
                        grade = 'D';
                        break;
                    default:
                        grade = 'F';
                        break;
                }
                Console.WriteLine("{0} : {1} : {2} : {3} : {4} : {5} : {6} : {7}", i, name, kor, eng,
                    math, total, avg, grade);
                Console.WriteLine();
            }
        }
    }
}
