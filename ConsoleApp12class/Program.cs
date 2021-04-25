using System;
using Test;

namespace ConsoleApp12class
{
    struct Board
    {

    }
    //보통 클래스와 구조체는 네임스페이스 바로 밑에 선언하는데,
    //이때 디폴트로 internal 접근 제한을 갖는다.
    /*internal*/ class Person
    {
        //1.field
        public int age;             //public 선언이 있어야 다른 클래스에서 접근가능
        internal string name;       //동일한 Assembly 내에 있는 다른 타입들이 엑세스 할 수 
        string phone;               //필드에 public 선언이 없으며 디폴트로 private
        private string email;
        protected string weight;    //클래스 외부에서 접근할 수 없으나 파생 클래스에서는

        //constructor
        public Person()     //publid 선언이 있어야 다른 클래스에서 접근가능
        {
            age = 10;
            name = "kim";
            phone = "010-0000-0000";
            email = "aaa@aaa.com";
            weight = "88kg";
        }

        //constructor 오버로딩
        public Person(int age, string name, string phone, string email)     //public 선언이 있어야 다른 클래스에 접근가능
        {
            this.age = age;
            this.name = name;
            this.phone = phone;
            this.email = email;
        }

        //속성 : 은닉필드에 대하여 값설정과 획득을 보조하는 get, set변수,
        public string Phone
        {
            get { return this.phone;  }
            set { this.phone = value; }     //value변수는 예약어로 변경불가
        }

        public override string ToString()
        {
            return string.Format("Person : age : {0}, name : {1}, phone : {2}, email : {3}, weight : {4}", age, name, phone, email, weight);
        }

        public string Eamil
        {
            get { return this.email; }
            set { this.email = value; }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Person p = new Person();
            Console.WriteLine(p);
            Console.WriteLine(p.age);
            Console.WriteLine(p.name);
            //Console.WriteLine(p.phone); public 선언안된 phone에 접근불가
            //Console.WriteLine(p.email); public 선언안된 email에 접근불가

            p.age = 11;
            p.name = "John";

            Console.WriteLine(p.age);
            Console.WriteLine(p.name);

            Console.WriteLine("============인자있는 생성자===============");
            p = new Person(33, "han", "031-333-3333", "ccc@ccc.com");
            Console.WriteLine(p.age);
            Console.WriteLine(p.name);
            p = new Person(44, "han44", "031-444-4444", "ddd@ddd.com");
            Console.WriteLine(p.age);
            Console.WriteLine(p.name);

            Console.WriteLine("============속성으로 접근가능===============");
            p.Phone = "02-222-2222";
            p.Eamil = "bbb@bbb.com";
            Console.WriteLine(p.Phone);
            Console.WriteLine(p.Eamil);

            Console.WriteLine("============미리정의한 메소드로 정보열람.==============");
            Console.WriteLine(p);
            Console.WriteLine(p.ToString());

            Console.WriteLine("============다른 네임스페이스 만들고 클래스생성===============");
            //Test.Car c = new Test.Car();
            Car c = new Car();
            Console.WriteLine(c.model);
            Console.WriteLine(c.price);
            c.Pnumber = "kkk1212";
            Console.WriteLine(c.Pnumber);

            Console.WriteLine(c.st);
            Console.WriteLine(c.MyVars);

            foreach (var item in c.MyVars)
            {
                Console.Write($"{item} ");
            }
            Console.WriteLine();

            //foreach (var item in c.MyVars[1..3]) 1부터 3전까지 복제
            //foreach (var item in c.MyVars[1..]) 1부터 끝까지 복제
            //foreach (var item in c.MyVars[..3]) 0부터 3전까지 복제
            foreach (var item in c.MyVars[..]) //모두 복제
            {
                Console.Write($"{item} ");
            }
            Console.WriteLine();

            Console.WriteLine("============다른 네임스페이스 만들고 클래스생성===============");
            Test.Student st = new Test.Student();
            Console.WriteLine(st);
            st.Name = "Hong";
            st.Age = 88;
            Console.WriteLine(st);
            Console.WriteLine(st.Name);
            Console.WriteLine(st.Age);
        }
    }
}
namespace Test
{
    class Car : Student //Car클래스가 Student 클래스를 상속받음
    {
        public string model = "MODEL";
        public int price = 10000;
        private string pnumber = "kosta1004";
        public Student st = new Student();

        public Car()
        {
            pnumber = "kosta1004";
            price = 50000;
        }

        public Car(string _model) : this()
        {
            Console.WriteLine(Kor);
        }
        private int[] myVars = new int[] { 11, 22, 33, 44, 55, 66 };

        public int[] MyVars
        {
            get { return myVars; }
            set { myVars = value; }
        }


        public string Pnumber
        {
            get { return pnumber; }
            set { pnumber = value; }
        }
        //propfull tab tab

        //ov tab, to + tab
        public override string ToString()
        {
            return string.Format("Car : {0}, {1}, {2}",model, price, Pnumber);
        }

    }
    
    class Student
    {
        //필드없이 간략하게 속성만으로 정의가능
        public string Name { get; set; }
        public int Age { get; set; }
        //단축키 prop tab tab
        public int Kor { get; set; }

        public override string ToString()
        {
            return "Student : " + Name + " " + Age + " " + Kor;
        }
    }
}
