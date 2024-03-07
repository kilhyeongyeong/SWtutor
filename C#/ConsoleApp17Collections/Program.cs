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

            /*Console.WriteLine("===================ArrayList======================");

            ArrayList list = new ArrayList();
            list.Add("kim1");
            list.Add("kim2");
            list.Add("kim3");
            list.Add(3333)

            list.Insert(1, "yangssem");

            list.RemoveAt(3);

            Console.WriteLine("list.Count : " + list.Count);

            foreach (var name in list)
            {
                Console.WriteLine(name);
            }*/

            /*Console.WriteLine("===================Queue===================");

            Queue q = new Queue(); //FIFO - First In First Out

            q.Enqueue(11);
            q.Enqueue(22);
            q.Enqueue(44);
            q.Enqueue(3);
            q.Enqueue(22);

            foreach (var item in q)
            {
                Console.WriteLine(item);
            }

            Console.WriteLine("q.Count : " + q.Count);
            Console.WriteLine(q.Dequeue());

            Console.WriteLine("q.Count : " + q.Count);
            Console.WriteLine(q.Dequeue());

            Console.WriteLine("q.Count : " + q.Count);
            Console.WriteLine(q.Dequeue());

            Console.WriteLine("q.Count : " + q.Count);
            Console.WriteLine(q.Dequeue());*/

            /*Console.WriteLine("===================Stack====================");

            Stack s = new Stack(); //LIFO - Last In First Out
            s.Push("aaa");
            s.Push("bbb");
            s.Push("fff");
            s.Push("www");
            s.Push("aa");

            foreach (var item in s)
            {
                Console.WriteLine(item);
            }

            Console.WriteLine("s.Count : " + s.Count);
            Console.WriteLine(s.Pop());

            Console.WriteLine("s.Count : " + s.Count);
            Console.WriteLine(s.Pop());

            Console.WriteLine("s.Count : " + s.Count);
            Console.WriteLine(s.Pop());

            Console.WriteLine("s.Count : " + s.Count);
            Console.WriteLine(s.Pop());*/

            Console.WriteLine("===================HashTable====================");
            Hashtable map = new Hashtable();
            map["name"] = "kim";
            map["age"] = 33;
            map["weight"] = 82.5;
            map["age"] = 3333;

            foreach (var item in map.Keys)
            {
                Console.WriteLine(item + ":" + map[item]);
            }

            //제네릭<T> : 명시한 타입으로 아이템을 확정짓는다.
            List<int> sus = new List<int>();
            sus.Add(11);
            sus.Add(111);
            // sus.Add("111"); int타입만 탑재가능
            Console.WriteLine(sus.Count);

            Queue<int> q2 = new Queue<int>(); //FIFO - First In First Out

            q2.Enqueue(11);
            q2.Enqueue(22);
            q2.Enqueue(44);
            q2.Enqueue(3);
            q2.Enqueue(22);
            //q2.Enqueue("aaaa"); error

            Stack<string> s = new Stack<string>(); //LIFO - Last In First Out
            s.Push("aaa");
            s.Push("bbb");
            s.Push("fff");
            s.Push("www");
            s.Push("aa");
            //s.Push(123); error

            Dictionary<string, string> dict = new Dictionary<string, string>();
            dict["key1"] = "lee";
            //dict["key2"] = 3.33;
            dict["key3"] = "lee33";

        }
    }
}
