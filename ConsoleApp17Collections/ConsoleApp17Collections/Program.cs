using System;
using System.Collections;
using System.Collections.Generic;

namespace ConsoleApp17Collections
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            ArrayList list = new ArrayList();
            list.Add("kim");
            list.Add("kim2");
            list.Add("kim3");
            list.Add(3333);

            list.Insert(1, "yangssem");

            list.RemoveAt(3);

            Console.WriteLine("list.Count : " + list.Count);

            foreach (var name in list)
            {
                Console.WriteLine(name);
            }
            Console.WriteLine("==================================");

            Queue q = new Queue(); // FIFO-First In First Out
            q.Enqueue(11);
            q.Enqueue(22);
            q.Enqueue(44);
            q.Enqueue(3);
            q.Enqueue(22);
            q.Enqueue("aaaa");

            foreach (var x in q)
            {
                Console.WriteLine(x);
            }

            Console.WriteLine("q.Conut : " + q.Count);
            Console.WriteLine(q.Dequeue());

            Console.WriteLine("q.Conut : " + q.Count);
            Console.WriteLine(q.Dequeue());

            Console.WriteLine("q.Conut : " + q.Count);
            Console.WriteLine(q.Dequeue());
            Console.WriteLine("==================================");

            Stack s = new Stack(); // FILO-First In Last Out
            s.Push("aaa");
            s.Push("bbb");
            s.Push("fff");
            s.Push("www");
            s.Push("aa");
            s.Push(123);

            foreach (var x in s)
            {
                Console.WriteLine(x);
            }

            Console.WriteLine("s.Conut : " + s.Count);
            Console.WriteLine(s.Pop());

            Console.WriteLine("s.Conut : " + s.Count);
            Console.WriteLine(s.Pop()); 

            Console.WriteLine("s.Conut : " + s.Count);
            Console.WriteLine(s.Pop());
            Console.WriteLine("==================================");

            Hashtable map = new Hashtable();
            map["name"] = "kim";
            map["age"] = 33;
            map["weight"] = 82.5;
            map["age"] = 3333;

            foreach (var x in map.Keys)
            {
                Console.WriteLine(x + " : " + map[x]);
            }

            // 제네릭 <T> : 명시한 타입으로 아이템을 확정함
            List<int> sus = new List<int>();
            sus.Add(11);
            sus.Add(111);
            //sus.Add("111"); // int 타입만 탑재가능
            Console.WriteLine(sus.Count);

            Queue<int> q2= new Queue<int>(); // FIFO-First In First Out
            q2.Enqueue(11);
            q2.Enqueue(22);
            q2.Enqueue(44);
            q2.Enqueue(3);
            q2.Enqueue(22);
            //q2.Enqueue("aaaa"); // error

            Stack<string> s2 = new Stack<string>(); // FILO-First In Last Out
            s2.Push("aaa");
            s2.Push("bbb");
            s2.Push("fff");
            s2.Push("www");
            s2.Push("aa");
            //s2.Push(123); // error

            Dictionary<string, string> dict = new Dictionary<string, string>();
            dict["key1"] = "lee";
            //dict["key2"] = 33.33; // error
            dict["key3"] = "lee";

        }
    }
}
