using System;

namespace ConsoleApp07array
{
    class Program
    {
        static void Print(int value)
        {
            Console.WriteLine($"{value}");
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            //1차 배열 : 인덱스는 항상 0부터 양수이며 총갯수 -1까지 할당
            int[] sus = new int[3]; //정수의 기본값이 3개 자동할당됨.{0,0,0}
            sus[0] = 11;
            sus[1] = 22;
            sus[2] = 33;
            //sus[3] = 33; 주의 : System.IndexOutOfRangeException

            /*Console.WriteLine("=======================");
            Console.WriteLine("sus[0] : " + sus[0]);
            Console.WriteLine("sus[1] : " + sus[1]);
            Console.WriteLine("sus[2] : " + sus[2]);

            for(int i=0; i<sus.Length; i++)
            {
                Console.WriteLine("sus["+i+"] : " + sus[i]);
            }

            Console.WriteLine("=======================");
            foreach (var item in sus)
            {
                Console.WriteLine(item);
            }*/

            /*Console.WriteLine("=======================");
            string[] names = new string[10];
            for (int i = 0; i < names.Length; i++)
            {
                names[i] = "kim" + i;
            }

            foreach (var item in names)
            {
                Console.Write(item + " ");
            }*/

            /*Console.WriteLine("=======================");
            int[] sus2 = { 44, 55, 66 }; //선언과 초기화 동시에 할때는 new int[] 새략가능
            sus2 = new int[3] { 44, 55, 66 }; //초기화만 할때는 new int[3]생략불가.
            sus2 = new int[] { 44, 55, 66 };//초기화만 할때는 new int[] 생략불가
            //배열의 길이를 의미하는 [3]생략가능.
            foreach (var item in sus2)
            {
                Console.WriteLine(item);
            }*/

            int[] sus3 = new int[] { 77, 88, 99 };
            sus3 = new int[] { 880, 770, 990 };
           /* foreach (var item in sus3)
            {
                Console.WriteLine(item);
            }

            Console.WriteLine("sus3.GetType() : " + sus3.GetType());

            Console.WriteLine("===========Array.Sort(sus3)============");
            Array.Sort(sus3);
            foreach (var item in sus3)
            {
                Console.WriteLine(item);
            }

            //indexOf(배열명,값) : 값이 위치하는 인덱스 반환
            Console.WriteLine("Array.IndexOf(sus3,990) : " + Array.IndexOf(sus3,990));

            Console.WriteLine("===========Array.Clear(배열명, 시작인덱스, 기본값으로 초기화할 개수)============");
            *//*Array.Clear(sus3,0, sus3.Length);
            foreach (var item in sus3)
            {
                Console.WriteLine(item);
            }*//*

            Array.Clear(sus3, 0, 2); //0번 방부터 2개의 타입의 초기값으로 변경해라.
            foreach (var item in sus3)
            {
                Console.WriteLine(item);
            }*/

            Console.WriteLine("=======================");
            Array.ForEach<int>(sus3, new Action<int>(Print));
            /*Console.WriteLine("=======================");
            string[] names2 = new string[] { "kim", "lee", "yang" };
            names2 = new string[3] { "kim", "lee", "yang" };
            names2 = new string[] { "kim", "lee", "yang" };
            Console.WriteLine("names2.GetType() : " + names2.GetType()); //names2.GetType() : System.String[]
            Console.WriteLine("names2.GetType().BaseType : " + names2.GetType().BaseType); //names2.GetType().BaseType : System.Array
            Console.WriteLine("names2.GetValue(0) : " + names2.GetValue(0)); //names2.GetValue(0) : kim
            Console.WriteLine("names2.GetValue(1) : " + names2.GetValue(1)); //names2.GetValue(1) : lee
            Console.WriteLine("names2.GetValue(2) : " + names2.GetValue(2)); //names2.GetValue(2) : yang
            foreach (var item in names2)
            {
                Console.WriteLine(item);
            }*/

            /*Console.WriteLine("=======================");

            //2차원 배열 : int[,]
            int[,] suss = { { 11, 22, 33 }, { 44, 55, 66 } };
            Console.WriteLine("suss.Length : " + suss.Length); //모든 데이터 개수 반환
            Console.WriteLine("suss[0, 0] : " + suss[0, 0]);
            Console.WriteLine("suss[0, 1] : " + suss[0, 1]);
            Console.WriteLine("suss[0, 2] : " + suss[0, 2]);
            Console.WriteLine("suss[1, 0] : " + suss[1, 0]);
            Console.WriteLine("suss[1, 1] : " + suss[1, 1]);
            Console.WriteLine("suss[1, 2] : " + suss[1, 2]);

            foreach (var item in suss)
            {
                Console.WriteLine(item);
            }*/

            Console.WriteLine("=======================");
            int[][] suss2 = new int[2][];
            //int[][] suss2 = new int[2][3]; //error
            Console.WriteLine("suss2.Length : " + suss2.Length);
            suss2 = new int[2][] { new int[] { 11, 22, 33 }, new int[] { 44, 55, 66 } };
            //suss2 = new int[2][] {{11,22,23},{44,55,66}}; //error

            foreach (var items in suss2)
            {
                Console.WriteLine(items);
                foreach (var item in items)
                {
                    Console.WriteLine(item);
                }
            }

            suss2[0] = new int[] { 110, 220, 330 };
            suss2[1] = new int[] { 110, 220, 330 };

            foreach (var items in suss2)
            {
                Console.WriteLine(items);
                foreach (var item in items)
                {
                    Console.WriteLine(item);
                }
            }
            Console.WriteLine("=======================");

            //2차배열 선언 및 초기화
            string[,] Depts = { { "김과장", "경리부" }, { "이과장", "총무부" } };
            string[][] Depts2 = {
                                    new string[] {"김과장","경리부"},
                                    new string[] {"이과장","총무부"}
                                };

            //3차 배열 선언
            string[,,] Cubes;
            string[][][] Cubes2;
        }
    }
}
