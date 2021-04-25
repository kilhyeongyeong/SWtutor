using System;

namespace ConsoleApp08enum
{
    //C#의 키워드 enum은 열거형 상수(constant)를 표현하기 위한 것으로
    //이를 이용하면 상수 숫자들을 보다 의미있는 단어들로 표현할 수 있어서
    //프로그램을 읽기 쉽게 해준다.

    //enum의 각 요소는 별도의 지정없이는 첫번째 요소가 0,
    //      두번째 요소가 1, 세번째 요소가 2 등과 같이 1씩 증가된 값들을 할당받는다.
    //      물론, 개발자가 임의로 의미있는 번호를 지정해 줄 수도 있다.
    //enum 문은 클래스 안이나 네임스페이스 내에서만 선언될 수 있다.
    //      즉, 메서드 안이나 속성 안에서는 선언되지 않는다.

    //네임스페이스 영역
    enum Car
    {
        BMW,SM,OOOO,MS,RAY=100,Mini=101
    }
    class Program
    {
        //클래스 영역
        enum City
        {
            Seoul,
            Daejun,
            Busan = 5,
            Jeju = 10
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Console.WriteLine(Car.BMW);
            Console.WriteLine(Car.SM);
            Console.WriteLine(Car.OOOO);
            Console.WriteLine(Car.MS);
            Console.WriteLine((int)Car.MS==3);
            Console.WriteLine((int)Car.RAY==100);

            Console.WriteLine("==================================");
            Console.WriteLine(City.Seoul);
            Console.WriteLine(City.Daejun);
            Console.WriteLine(City.Busan);
            Console.WriteLine(City.Jeju);
        }
    }
}
