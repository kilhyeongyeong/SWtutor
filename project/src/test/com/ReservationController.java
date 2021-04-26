package test.com;

import java.io.IOException;
import java.util.List;

import test.com.board.BoardVO;
import test.com.reservation.*;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class ReservationController
 */
@WebServlet({"/reservation.do", "/reservationOK.do", "/rsv_insert", "/rsv_checkOne.do",
	"/rsv_revise.do", "/rsv_reviseOK.do", "/rsv_delete.do", "/rsv_checkAll.do", "/reservationAll.do",
	"/rsv_deleteAll.do"})
public class ReservationController extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ReservationController() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//response.getWriter().append("Served at: ").append(request.getContextPath());
		String sPath = request.getServletPath();
		
		ReservationVO vo = new ReservationVO();
		ReservationDAO dao = new ReservationDAOimpl();
		System.out.println();
		
//--------------------------------------------------------------------------------------------------------------------------------		
		if(sPath.equals("/reservation.do")) {
			System.out.println("reservation.jsp");
			
			String loginSession = (String)request.getSession().getAttribute("login");
			
			if(loginSession == null || loginSession.equals("WrongPW") || loginSession.equals("NotID")) {
				response.sendRedirect("login.do");
			}else {
				RequestDispatcher rd = request.getRequestDispatcher("reservation/reservation.jsp");
				rd.forward(request, response);
			}
//---------------------------------------------------------------------------------------------------------------------------			
		}else if(sPath.equals("/reservationOK.do")) {
			System.out.println("reservationOK.do");
		
			int adultNum = Integer.parseInt(request.getParameter("rsv_adult"));
			int childNum = Integer.parseInt(request.getParameter("rsv_child"));
			int babyNum = Integer.parseInt(request.getParameter("rsv_baby"));
			String state = (String)request.getSession().getAttribute("login");
			String adult_state = (String)request.getSession().getAttribute("adult");
			String adult_price = (String)request.getSession().getAttribute("adult");
			String child_price = (String)request.getSession().getAttribute("child");
			String baby_price = (String)request.getSession().getAttribute("baby");
			
			vo = new ReservationVO();
			vo.setId((String)request.getSession().getAttribute("userID"));
			vo.setName(request.getParameter("rsv_name"));
			
			int check_res = dao.reservationOK(vo);
			
			if(check_res == 1) {
				System.out.println("이미 있는 이름");
				request.setAttribute("rsv_nameCheck", "already name");
				RequestDispatcher rd = request.getRequestDispatcher("reservation/reservation.jsp");
				rd.forward(request, response);
			}else {
				vo.setEmail(request.getParameter("rsv_email"));
				vo.setAdultNum(adultNum);
				vo.setChildNum(childNum);
				vo.setBabyNum(babyNum);
				vo.setMonth(Integer.parseInt(request.getParameter("rsv_month")));
				vo.setDay(Integer.parseInt(request.getParameter("rsv_day")));
				
				int total_price = dao.price(state, adult_state, adult_price, child_price, baby_price, adultNum, childNum, babyNum);
				vo.setPrice(total_price);
				
				int res = dao.insert(vo);
				
				if(res == 1) {
					System.out.println("reservation_insert_OK");
					response.sendRedirect("rsv_checkAll.do");
				}else {
					System.out.println("reservation_insert_failed");
					response.sendRedirect("reservaion.do");
				}
			}
//-----------------------------------------------------------------------------------------------------------------------------			
		}else if(sPath.equals("/rsv_checkAll.do")) {
			System.out.println("rsv_checkAll.do");

			String loginSession = (String)request.getSession().getAttribute("login");
			
			if(loginSession == null || loginSession.equals("WrongPW") || loginSession.equals("NotID")) {
				response.sendRedirect("login.do");
			}else {
				vo = new ReservationVO(); 
				vo.setId((String)request.getSession().getAttribute("userID"));
				
				List<ReservationVO> list = dao.selectAll(vo);
				for (ReservationVO x : list) {
					System.out.println(x);
				}

				request.setAttribute("list", list);

				RequestDispatcher rd = request.getRequestDispatcher("reservation/reservation_checkAll.jsp");
				rd.forward(request, response);
			}
//-----------------------------------------------------------------------------------------------------------------------------			
		}else if(sPath.equals("/rsv_checkOne.do")) {
			System.out.println("rsv_checkOne.do");
			System.out.println(request.getParameter("ch_name"));
					
			vo = new ReservationVO();
			vo.setId((String)request.getSession().getAttribute("userID"));
			vo.setName(request.getParameter("ch_name"));

			ReservationVO vo2 = dao.selectOne(vo);
			System.out.println(vo2);

			request.setAttribute("reservation_vo2", vo2);
					
			RequestDispatcher rd = request.getRequestDispatcher("reservation/reservation_check.jsp");
			rd.forward(request, response);
//-----------------------------------------------------------------------------------------------------------------------------			
		}else if(sPath.equals("/rsv_revise.do")) {
			System.out.println("rsv_revise.do");
			
			vo = new ReservationVO();
			vo.setId((String)request.getSession().getAttribute("userID"));
			vo.setName(request.getParameter("rsv_update"));
			request.getSession().setAttribute("name", request.getParameter("rsv_update"));

			ReservationVO vo2 = dao.selectOne(vo);
			System.out.println(vo2);

			request.setAttribute("reservation_revise_vo2", vo2);
			
			RequestDispatcher rd = request.getRequestDispatcher("reservation/reservation_revise.jsp");
			rd.forward(request, response);
			
//-------------------------------------------------------------------------------------------------------------------------			
		}else if(sPath.equals("/rsv_reviseOK.do")) {
			System.out.println("rsv_reviseOK.do");
			
			int adultNum = Integer.parseInt(request.getParameter("rsv_re_adult"));
			int childNum = Integer.parseInt(request.getParameter("rsv_re_child"));
			int babyNum = Integer.parseInt(request.getParameter("rsv_re_baby"));
			String state = (String)request.getSession().getAttribute("login");
			String adult_state = (String)request.getSession().getAttribute("adult");
			String adult_price = (String)request.getSession().getAttribute("adult");
			String child_price = (String)request.getSession().getAttribute("child");
			String baby_price = (String)request.getSession().getAttribute("baby");
			
			vo = new ReservationVO();
			vo.setId((String)request.getSession().getAttribute("userID"));
			vo.setPastName((String)request.getSession().getAttribute("name"));
			request.getSession().removeAttribute("name");
			vo.setName(request.getParameter("rsv_re_name"));
			vo.setEmail(request.getParameter("rsv_re_email"));
			vo.setAdultNum(adultNum);
			vo.setChildNum(childNum);
			vo.setBabyNum(babyNum);
			vo.setMonth(Integer.parseInt(request.getParameter("rsv_re_month")));
			vo.setDay(Integer.parseInt(request.getParameter("rsv_re_day")));
			
			int total_price = dao.price(state, adult_state, adult_price, child_price, baby_price, adultNum, childNum, babyNum);
			vo.setPrice(total_price);
			
			int res = dao.update(vo);
			
			if(res == 1) {
				System.out.println("업데이트 성공");
				response.sendRedirect("rsv_checkAll.do");
			}else {
				System.out.println("업데이트 실패...");
				response.sendRedirect("rsv_revise.do");
			}
		}else if(sPath.equals("/rsv_delete.do")){
			System.out.println("reservation_revise.jsp");
			
			vo = new ReservationVO();
			vo.setId((String)request.getSession().getAttribute("userID"));
			vo.setName(request.getParameter("rsv_delete"));

			int res = dao.delete(vo, 0);
			
			if(res == 1) {
				System.out.println("삭제 성공");
				request.setAttribute("delete", "삭제되었습니다.");
				response.sendRedirect("rsv_checkAll.do");
			}else {
				System.out.println("삭제 실패...");
				request.setAttribute("delete", "삭제되었습니다.");
				RequestDispatcher rd = request.getRequestDispatcher("reservation/reservation_delete.jsp");
				rd.forward(request, response);
			}
		}else if(sPath.equals("/reservationAll.do")) {
			System.out.println("board_selectAll");
			
			int total = dao.totalPrice();
			
			List<ReservationVO> list = dao.selectAll();
			for (ReservationVO x : list) {
				System.out.println(x);
			}

			request.setAttribute("reservationlist", list);
			request.setAttribute("reservation_totalPrice", total);
			System.out.println(total);
			
			RequestDispatcher rd = request.getRequestDispatcher("reservation/reservationAll.jsp");
			rd.forward(request, response);
		}else if(sPath.equals("/rsv_deleteAll.do")) {
			System.out.println("rsv_deleteAll.do");
			
			vo = new ReservationVO();
			vo.setId((String)request.getSession().getAttribute("userID"));

			int res = dao.delete(vo, 1);
			
			if(res == 1) {
				System.out.println("삭제 성공");
				response.sendRedirect("logout.do");
			}else {
				System.out.println("삭제 실패...");
				response.sendRedirect("index.do");
			}
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
