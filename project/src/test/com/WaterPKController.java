package test.com;

import java.io.IOException;
import test.com.member.*;
import test.com.manager.*;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import test.com.member.MemberVO;

/**
 * Servlet implementation class WaterPKController
 */
@WebServlet({"/index.do", "/login.do", "/signup.do", "/loginOK.do", "/logout.do", "/idfind.do","/idfindOK.do",
	"/idfound.do"})
public class WaterPKController extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public WaterPKController() {
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
		
		if(sPath.equals("/index.do")) {//--------------------------------------------------------------------------------------------index.do
			System.out.println("index.jsp");
			System.out.println();
			
			RequestDispatcher rd = request.getRequestDispatcher("index.jsp");
			rd.forward(request, response);
		}else if(sPath.equals("/login.do")) {//--------------------------------------------------------------------------------------login.do
			System.out.println("login.jsp");
			System.out.println();
			
			RequestDispatcher rd = request.getRequestDispatcher("service/login.jsp");
			rd.forward(request, response);
		}else if(sPath.equals("/signup.do")) {
			
			RequestDispatcher rd = request.getRequestDispatcher("service/signup.jsp");
			rd.forward(request, response);
			
		}else if(sPath.equals("/loginOK.do")) {//--------------------------------------------------------------------------------------loginOK.do
	
			MemberVO mem_vo = new MemberVO();
			MemberDAO mem_dao = new MemberDAOimpl();
			
			mem_vo.setId(request.getParameter("id"));
			mem_vo.setPw(request.getParameter("pw"));
			
			String mem_res = mem_dao.loginOK(mem_vo);
			
			if(!mem_res.equals("WrongPW") && !mem_res.equals("NotID")) {
				request.getSession().setAttribute("login", "mem_Successed");
				request.getSession().setAttribute("userID", mem_vo.getId());
				request.getSession().setAttribute("userProfile", mem_res);
				//request.getSession().setMaxInactiveInterval(300); //300초 동안 세션 유지
				
				response.sendRedirect("index.do");
				
			}else if(mem_res.equals("WrongPW")){
				request.getSession().setAttribute("login", mem_res);
				//request.getSession().setMaxInactiveInterval(300); //300珥� �뮘 session 留뚮즺
				response.sendRedirect("lonin.do");
			}else {
				ManagerVO mng_vo = new ManagerVO();
				ManagerDAO mng_dao = new ManagerDAOimpl();
				
				mng_vo.setId(request.getParameter("id"));
				mng_vo.setPw(request.getParameter("pw"));
				
				String mng_res = mng_dao.loginOK(mng_vo);
				System.out.println(mng_res);
				
				if(!mng_res.equals("WrongPW") && !mng_res.equals("NotID")) {
					request.getSession().setAttribute("login", "mng_Successed");
					request.getSession().setAttribute("userID", mng_vo.getId());
					request.getSession().setAttribute("userProfile", mng_res);
					response.sendRedirect("index.do");
					
				}else {
					request.getSession().setAttribute("login", mng_res);
					
					response.sendRedirect("login.do");
				}
			}
		}else if(sPath.equals("/logout.do")) {
			//request.getSession().invalidate(); //모든 세션 제거
			request.getSession().removeAttribute("login");
			request.getSession().removeAttribute("userID");
			request.getSession().removeAttribute("userProfile");
			response.sendRedirect("index.do");
		}else if(sPath.equals("/idfind.do")) {
			RequestDispatcher rd = request.getRequestDispatcher("service/idfind.jsp");
			rd.forward(request, response);
		}else if(sPath.equals("/idfindOK.do")) {
			MemberVO mem_vo = new MemberVO();
			MemberDAO mem_dao = new MemberDAOimpl();
			
			mem_vo.setName(request.getParameter("findname"));
			mem_vo.setEmail(request.getParameter("findemail"));
			
			MemberVO mem_vo2 = mem_dao.idFind(mem_vo);
			
			if(mem_vo2.getId() == null) {
				ManagerVO mng_vo = new ManagerVO();
				ManagerDAO mng_dao = new ManagerDAOimpl();
				
				mng_vo.setName(request.getParameter("findname"));
				mng_vo.setEmail(request.getParameter("findemail"));
				
				ManagerVO mng_vo2 = mng_dao.idFind(mng_vo);
				
				if(mng_vo2.getId() == null) {
					response.sendRedirect("idfind.do?msg=NotID");
				}else {
					String str = mng_vo2.getPw();
					int str_length = str.length();
					str = str.substring(0, 4);
					for(int i=0; i<(str_length-4); i++) {
						str = str.concat("*");
					}
					response.sendRedirect("idfound.do?foundid="+mng_vo2.getId()+"&foundpw="+str);
				}
			}else {
				String str = mem_vo2.getPw();
				int str_length = str.length();
				str = str.substring(0, 4);
				for(int i=0; i<(str_length-4); i++) {
					str = str.concat("*");
				}
				response.sendRedirect("idfound.do?foundid="+mem_vo2.getId()+"&foundpw="+str);
			}
			
		}else if(sPath.equals("/idfound.do")) {
			RequestDispatcher rd = request.getRequestDispatcher("service/idfound.jsp");
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
