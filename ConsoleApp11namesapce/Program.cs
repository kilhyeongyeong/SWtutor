using System;
using Test;
using Test.Com;

namespace ConsoleApp11namesapce
{
    //.NET Framework는 무수하게 많은 클래스들을 가지고 있는데,
    //예를 들면 .NET 4.0은 약 11,000개의 클래스를 가지고 있다.
    //이렇게 많은 클래스들을 충돌없이 보다 편리하게 관리/사용하기 위해
    //.NET 에서 네임스페이스를 사용한다.

    //C#에서도 이러한 개념을 적용하여 클래스들이 대개 네임스페이스 안에서 정의 된다.
    //비록 클래스가 네임스페이스 없이도 정의 될 수는 있지만,
    //거의 모든 경우 네임스페이스를 정의하는 것이 일반적이다.

    class Animal
    {
        //클래스에 대해서는 차후에 상세 설명
    }
    class Persom
    {
        //클래스에 대해서는 차후에 상세 설명
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Animal a = new Animal();
            Console.WriteLine(a);

            //Test.School sc = new Test.School();
            School sc = new School();
            Console.WriteLine(sc);

            //Test.Com.Car c = new Test.Com.Car();
            Car c = new Car();
            Console.WriteLine(c);
        }
    }
}

namespace Test
{
    class School
    {
        //클래스에 대해서는 차후에 상세 설명
    }

    namespace Com
    {
        class Car
        {
            //클래스에 대해서는 차후에 상세 설명
        }
    }
}
