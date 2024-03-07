using System;

namespace ConsoleApp02DataType
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            bool b = true;
            Console.WriteLine(b);

            byte by1 = 10;
            Console.WriteLine(by1);
            Console.WriteLine(byte.MinValue + " ~ " + byte.MaxValue);

            sbyte by2 = -10;
            Console.WriteLine(by2);
            Console.WriteLine(byte.MinValue + " ~ " + byte.MaxValue);

            short sh = -32768;
            Console.WriteLine(sh);
            Console.WriteLine(short.MinValue + " ~ " + short.MaxValue);

            int su = 2147483647;
            Console.WriteLine(su);
            Console.WriteLine(int.MinValue + " ~ " + int.MaxValue);

            uint u_su = 1024U;
            Console.WriteLine(u_su);
            Console.WriteLine(uint.MinValue + " ~ " + uint.MaxValue);

            long longSu = 1234L;
            Console.WriteLine(longSu);
            Console.WriteLine(long.MinValue + " ~ " + long.MaxValue);
            
            float f = 123.45F;
            Console.WriteLine(f);
            Console.WriteLine(float.MinValue + " ~ " + float.MaxValue);

            double d1 = 123.45;
            Console.WriteLine(d1);
            Console.WriteLine(double.MinValue + " ~ " + double.MaxValue);

            double d2 = 123.45D;
            Console.WriteLine(d2);
            Console.WriteLine(double.MinValue + " ~ " + double.MaxValue);

            decimal dm = 123.45M;
            Console.WriteLine(dm);
            Console.WriteLine(decimal.MinValue + " ~ " + decimal.MaxValue);
            
            char c = 'A';
            Console.WriteLine(c);
            Console.WriteLine(char.MinValue + " ~ " + char.MaxValue);
//            Console.WriteLine("{0} ~ {1}");

            string str;
            str = null;
            Console.WriteLine(str);
            str = "yangssem";
            Console.WriteLine(str);

            DateTime date = new DateTime(2022, 12, 25, 12, 35, 0); //설정한 날자와 시간.
            date = new DateTime();
            Console.WriteLine(date);//0001-01-01 오전 12:00:00
            Console.WriteLine(DateTime.Now);//2021-03-18 오후 12:05:36
            Console.WriteLine(DateTime.Now.ToString("yyyy MM dd HH:mm:ss"));//2021 03 18

            int? nableSu = null;
            Console.WriteLine(nableSu);

            nableSu = 101;
            Console.WriteLine(nableSu);

            bool? nableBool = null;
            Console.WriteLine(nableBool);

            Nullable<int> nullableSu = null;
            Console.WriteLine(nullableSu);

            nullableSu = 100;
            int changeSu = nullableSu.Value;
            Console.WriteLine(changeSu);
        }
    }
}
