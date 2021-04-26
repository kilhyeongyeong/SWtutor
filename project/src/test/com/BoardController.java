package test.com;

import java.io.IOException;
import java.util.List;
import test.com.board.*;
import test.com.member.MemberVO;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class BoardController
 */
@WebServlet({"/board_selectAll.do", "/board_update.do", "/board_notice_insert.do","/board_insertOK.do",
	"/board_selectOne.do", "/board_delete.do","/board_updateOK.do", "/board_searchList.do"})
public class BoardController extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public BoardController() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//response.getWriter().append("Served at: ").append(request.getContextPath());
		BoardDAO dao = new BoardDAOimpl();
		BoardVO vo = new BoardVO();
		
		String sPath = request.getServletPath();
		
		if(sPath.equals("/board_selectAll.do")) {//--------------------------------------------------------------------------------------------index.do
			System.out.println("board_selectAll");
			
			List<BoardVO> list = dao.selectAll();
			for (BoardVO x : list) {
				System.out.println(x);
			}

			request.setAttribute("boardlist", list);
			
			RequestDispatcher rd = request.getRequestDispatcher("service/notice.jsp");
			rd.forward(request, response);
//------------------------------------------------------------------------------------------------------------------------------------------------------			
		}else if(sPath.equals("/board_notice_insert.do")) {
			RequestDispatcher rd = request.getRequestDispatcher("board/board_insert.jsp");
			rd.forward(request, response);
//--------------------------------------------------------------------------------------------------------------------------------------------------------
		}else if(sPath.equals("/board_insertOK.do")) {
			
			String writerSesseion = (String)request.getSession().getAttribute("userID");
			vo.setWriter(writerSesseion);
			vo.setTitle(request.getParameter("insert_title"));
			vo.setContent(request.getParameter("insert_content"));
			
			int result = dao.insert(vo);
			
			System.out.println("insert result:" + result);

			if (result == 1)
				response.sendRedirect("board_selectAll.do");
			else
				response.sendRedirect("board_notice_insert.do");
//-------------------------------------------------------------------------------------------------------------------------------------------------------------			
		}else if(sPath.equals("/board_selectOne.do")){

			vo = new BoardVO();
			vo.setContent(request.getParameter("selectOne_content"));

			BoardVO vo2 = dao.selectOne(vo);
			System.out.println(vo2);

			request.setAttribute("vo2", vo2);

			RequestDispatcher rd = request.getRequestDispatcher("board/board_selectOne.jsp");
			rd.forward(request, response);
//-----------------------------------------------------------------------------------------------------------------------------------------------------------			
		}else if(sPath.equals("/board_update.do")) {
			
			request.setAttribute("h_update_title", request.getParameter("h_update_title"));
			request.setAttribute("h_update_content", request.getParameter("h_update_content"));
			
			request.getSession().setAttribute("p_title", request.getParameter("h_update_title"));
			
			RequestDispatcher rd = request.getRequestDispatcher("board/board_update.jsp");
			rd.forward(request, response);
//----------------------------------------------------------------------------------------------------------------------------------------------------------			
		}else if(sPath.equals("/board_delete.do")) {
			vo = new BoardVO();
			vo.setContent(request.getParameter("delete_content"));

			int result = dao.delete(vo);
			System.out.println("delete result:" + result);

			if (result == 1)
				response.sendRedirect("board_selectAll.do");
			else
				response.sendRedirect("board_selectOne.do?content=" + request.getParameter("content"));
//------------------------------------------------------------------------------------------------------------------------------------------------------------
		}else if(sPath.equals("/board_updateOK.do")) {
			
			vo = new BoardVO();
			
			String writerSesseion = (String)request.getSession().getAttribute("userID");
			
			vo.setWriter(writerSesseion);
			vo.setTitle(request.getParameter("update_title"));
			vo.setContent(request.getParameter("update_content"));
			vo.setP_title((String)request.getSession().getAttribute("p_title"));

			int result = dao.update(vo);
			
			System.out.println("update result:" + result);

			if (result == 1)
				response.sendRedirect("board_selectAll.do");
			else
				response.sendRedirect("board_update.do");

		}else if(sPath.equals("/board_searchList.do")) {
			System.out.println("searchKey:" + request.getParameter("searchKey"));
			System.out.println("searchWord:" + request.getParameter("searchWord"));

			List<BoardVO> list = dao.searchList(request.getParameter("searchKey"), request.getParameter("searchWord"));
			for (BoardVO x : list) {
				System.out.println(x);
			}

			request.setAttribute("boardlist", list);

			RequestDispatcher rd = request.getRequestDispatcher("service/notice.jsp");
			rd.forward(request, response);
		}
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		doGet(request, response);
	}

}
