using System;

namespace ConsoleApp09string
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            /*Console.WriteLine("==========String.Empty, 와 빈문자=============");
            //String.Empty는 객체생성 없이 빈문자 할당
            //""는 객체 생성해서 빈문자 할당
            //반복되는 사용에서는 String.Empty쪽이 약간의 성능향상이 있을 수 있다.
            Console.WriteLine("String.Empty == \"\" : " + (String.Empty == ""));
            string str1 = "yangssem";
            str1 = "";
            string str2 = "yangssem";
            str2 = String.Empty;
            string str3 = "yangssem";
            str3 = null;

            Console.WriteLine("======빈문자 체크 1. 변수.Length==0 ============");
            Console.WriteLine("str1.Length == 0 : {0}", str1.Length == 0);
            Console.WriteLine("str2.Length == 0 : {0}", str2.Length == 0);
            //Console.WriteLine("str3.Length == 0 : {0}", str3.Length == 0); //System.NullReference...

            Console.WriteLine("string.IsNullOrEmpty(str1) : " + string.IsNullOrEmpty(str1));
            Console.WriteLine("string.IsNullOrEmpty(str2) : " + string.IsNullOrEmpty(str2));
            Console.WriteLine("string.IsNullOrEmpty(str3) : " + string.IsNullOrEmpty(str3));

            string name1 = "kim";
            string name2 = "kim";
            Console.WriteLine(name1.Equals(name2));
            Console.WriteLine(name1.CompareTo(name2)==0);

            string txt = "abcdefg";
            Console.WriteLine("txt[0] : " + txt[0]);
            Console.WriteLine("txt[1] : " + txt[1]);
            Console.WriteLine("txt[2] : " + txt[2]);

            Console.WriteLine("=============txt[System.Range]===============");
            Console.WriteLine(txt[0..3]);
            string temp = txt[0..3];

            Console.WriteLine("=============ToCharArray===============");
            char[] cs = txt.ToCharArray();
            foreach (var item in cs)
            {
                Console.WriteLine(item);
            }

            Console.WriteLine(cs[3..5]);

            Console.WriteLine("=============Substring===============");
            Console.WriteLine("txt.Substring(1,2) : " + txt.Substring(1,2));
            Console.WriteLine("txt[1..2] : " + txt[1..2]);
            Console.WriteLine(txt.Substring(1,3));
            Console.WriteLine(txt.Substring(4));*/

            Console.WriteLine("=============Trim===============");
            string txt = "     aaa bbb ccc    ";
            Console.WriteLine(txt);
            Console.WriteLine(txt.Length);
            Console.WriteLine(txt.Trim().Length);
            Console.WriteLine(txt.Length);

            Console.WriteLine("=============Replace===============");
            Console.WriteLine(txt.Replace("aaa","xxx"));
            Console.WriteLine(txt);
            txt = txt.Replace("aaa", "xxx");
            Console.WriteLine(txt);

            //C# 문자열은 immutable 즉 한번 문자열이 설정되면, 다시 변경할 수 없다.
            //  (주 : 한번 그 값이 설정되면 다시 변경할 수 없는 타입을 immutable Type이라
            //  부르고, 반대로 값을 계속 변경할 수 있는 것을 Mutable Type이라 부른다)
            //  예를들어, 문자열 변수 str 가 있을 때, str = "hello";
            //  이라고 한 후 다시 str = "hello2"; 이라고 실행하면,
            //  .NET 시스템은 새로운 string 객체를 생성하여 "hello2"이라는 데이터로 
            //  초기화 한 후 이를 변수명 str에 할당한다. 즉, 변수 str는 내부적으로는 
            //  전혀 다른 메모리를 갖는 객체를 가리키는 것이다.
            string str = "hello";
            str = "hello2";

            //string str = new string("hello");
            //str = new string("hello2");

            //그래서, Immutable이기 때문에, 많은 양의 문자열 갱신을 많이 하는 프로그램에서는 적
            DateTime startTime = DateTime.Now;
            for (int i = 0; i < 50000; i++)
            {
                str += "hello" + i;
            }

            TimeSpan ts = DateTime.Now - startTime;
            Console.WriteLine(ts);
            Console.WriteLine(string.Format("{0:hh\\:mm\\:ss}", ts));
        }
    }
}
