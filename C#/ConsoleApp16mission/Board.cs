using System;
using System.Collections.Generic;
using System.Text;
using System.Collections;

namespace NSBoard
{
    class BoardVO
    {
        public int Num { get; set; }
        public string Title { get; set; }
        public string Content { get; set; }
        public string Writer { get; set; }
        public DateTime Wdate { get; set; }
        public string Str_Wdate { get; set; }

        public override string ToString()
        {
            return string.Format("BoardVO:Num:{0} ,Title:{1} ,Content:{2} ,Writer:{3} ,Wdate:{4} ,Str_Wdate:{5} ",Num, Title, Content, Writer, Wdate, Str_Wdate);
        }
    }

    interface IBoardDAO
    {
        int Insert(BoardVO vo);
        int Update(BoardVO vo);
        int Delete(BoardVO vo);
        BoardVO SelectOne(BoardVO vo);
        ArrayList SelectAll();
        ArrayList SearchList(string searchKey, string searchWord);
    }

    class IBoardDAOimpl : IBoardDAO
    {


        public int Insert(BoardVO vo)
        {
            Console.WriteLine("IBoardDAOimpl: insert()");
            Console.WriteLine("IBoardDAOimpl: " + vo);
            int flag = 0;

            flag = 1;

            return flag;
        }

        public ArrayList SearchList(string searchKey, string searchWord)
        {
            Console.WriteLine("IBoardDAOimpl: searchList()");
            Console.WriteLine("IBoardDAOimpl: searchList().." + searchKey);
            Console.WriteLine("IBoardDAOimpl: searchList().." + searchWord);


            return new ArrayList();
        }

        public ArrayList SelectAll()
        {
            Console.WriteLine("IBoardDAOimpl: selectAll()");
            return new ArrayList();
        }

        public BoardVO SelectOne(BoardVO vo)
        {
            Console.WriteLine("IBoardDAOimpl: selectOne()");
            Console.WriteLine("IBoardDAOimpl: " + vo);


            return new BoardVO();
        }

        public int Update(BoardVO vo)
        {
            Console.WriteLine("IBoardDAOimpl: update()");
            Console.WriteLine("IBoardDAOimpl: " + vo);
            int flag = 0;

            flag = 1;

            return flag;
        }

        public int Delete(BoardVO vo)
        {
            Console.WriteLine("IBoardDAOimpl: delete()");
            Console.WriteLine("IBoardDAOimpl: " + vo);
            int flag = 0;

            flag = 1;

            return flag;
        }
    }//end daoimpl
}
