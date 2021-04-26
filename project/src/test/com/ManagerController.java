package test.com;

import java.io.IOException;
import java.util.Enumeration;

import test.com.board.BoardVO;
import test.com.manager.*;
import test.com.member.MemberVO;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.oreilly.servlet.MultipartRequest;
import com.oreilly.servlet.multipart.DefaultFileRenamePolicy;

/**
 * Servlet implementation class ManagerController
 */
@WebServlet({"/manager_signup.do","/manager_insert.do","/manager_idCheck.do","/manager_facility.do",
	"/manager_facilityOK.do","/manager_guide.do","/manager_cost.do", "/manager_costOK.do",
	"/manager_notice.do","/mng_delete.do", "/mng_update.do","/mng_updateOK.do", "/mng_password.do",
	"/mng_passwordOK.do"})
public class ManagerController extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ManagerController() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//response.getWriter().append("Served at: ").append(request.getContextPath());	
		ManagerDAO dao = new ManagerDAOimpl();
		ManagerVO vo = new ManagerVO();
		
		String sPath = request.getServletPath();
		
		if(sPath.equals("/manager_signup.do")) {//--------------------------------------------------------------------------------------------index.do
			System.out.println("manager_signup.jsp");
			System.out.println();
			
			RequestDispatcher rd = request.getRequestDispatcher("manager/manager_signup.jsp");
			rd.forward(request, response);
			
		}else if(sPath.equals("/manager_insert.do")) {//--------------------------------------------------------------------------------------------index.do
			System.out.println("manager_insert.jsp");

			vo = new ManagerVO();
			
			String uploadPath = request.getServletContext().getRealPath("upload");
			System.out.println("uploadPath:"+uploadPath);
			
			int size = 10 * 1024 * 1024;
			
			try {
				MultipartRequest multi = new MultipartRequest(request, uploadPath, size, "UTF-8",
						new DefaultFileRenamePolicy());
			
				vo.setId(multi.getParameter("mngid"));
				vo.setPw(multi.getParameter("mngpw"));
				vo.setName(multi.getParameter("mngname"));
				vo.setPhone(multi.getParameter("mngphone"));
				vo.setEmail(multi.getParameter("mngemail"));
				vo.setBank(multi.getParameter("mngbank"));
				vo.setAccount(multi.getParameter("mngaccount"));
				
				Enumeration files = multi.getFileNames();

				String picture = (String) files.nextElement();
				System.out.println("pusa1:"+picture);
				String filename = multi.getFilesystemName(picture);
				System.out.println("filename:"+filename);
				
				vo.setProfile(filename);
				
				int res = dao.insert(vo);
				
				if(res == 1) {
					System.out.println("OK");
					response.sendRedirect("login.do");
				}else {
					System.out.println("Failed");
					response.sendRedirect("manager_signup.do");
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
			
		}else if(sPath.equals("/manager_idCheck.do")) {//--------------------------------------------------------------------------------------------index.do
			
			System.out.println(request.getParameter("mngid_check"));
			
			vo = new ManagerVO();
			vo.setId(request.getParameter("mngid_check"));
			
			int res = dao.idCheck(vo);
			
			if(res==0) {
				response.sendRedirect("manager_signup.do?id=" + vo.getId() + "&msg=OK");
			}else {
				response.sendRedirect("manager_signup.do?msg=NotOK");
			}
			
		}else if(sPath.equals("/manager_facility.do")) {
			System.out.println("manager_facility.do");

			RequestDispatcher rd = request.getRequestDispatcher("manager/manager_facility.jsp");
			rd.forward(request, response);
			
		}else if(sPath.equals("/manager_facilityOK.do")) {
			System.out.println("manager_facilityOK.do");

			String uploadPath = request.getServletContext().getRealPath("upload");
			System.out.println("uploadPath:"+uploadPath);
			
			int size = 10 * 1024 * 1024;

			try {
				MultipartRequest multi = new MultipartRequest(request, uploadPath, size, "UTF-8",
						new DefaultFileRenamePolicy());

				Enumeration files = multi.getFileNames();

				String picture = (String) files.nextElement();
				System.out.println("pusa1:"+picture);
				String filename = multi.getFilesystemName(picture);
				System.out.println("filename:"+filename);
//				String pusa2 = (String) files.nextElement();
//				String filename2 = multi.getFilesystemName(pusa2);
//				System.out.println("filename2:"+filename2);
				
				request.getSession().setAttribute("picture", filename);
			} catch (Exception e) {
				e.printStackTrace();
			}
			
			response.sendRedirect("member_facility.do");
			
		}else if(sPath.equals("/manager_guide.do")) {
			RequestDispatcher rd = request.getRequestDispatcher("manager/manager_guide.jsp");
			rd.forward(request, response);
			
		}else if(sPath.equals("/manager_cost.do")) {
			RequestDispatcher rd = request.getRequestDispatcher("manager/manager_cost.jsp");
			rd.forward(request, response);
			
		}else if(sPath.equals("/manager_costOK.do")) {
			System.out.println("manager_costOK.do");
			
			String adult = request.getParameter("adult");
			String child = request.getParameter("child");
			String baby = request.getParameter("baby");
			
			System.out.println("adult : " + adult);
			
			request.getSession().setAttribute("adult", adult);
			request.getSession().setAttribute("child", child);
			request.getSession().setAttribute("baby", baby);
			
			response.sendRedirect("member_facility.do");
			
		}else if(sPath.equals("/manager_notice.do")) {
			
			response.sendRedirect("board_selectAll.do");
			
		}else if(sPath.equals("/mng_delete.do")) {
			vo = new ManagerVO();
			vo.setId((String)request.getSession().getAttribute("userID"));

			int result = dao.delete(vo);

			if (result == 1) {
				System.out.println("회원탈퇴 성공!");
				response.sendRedirect("rsv_deleteAll.do");
			}else {
				System.out.println("회원탈퇴 실패!");
				response.sendRedirect("index.do");
			}
		}else if(sPath.equals("/mng_update.do")) {
			vo = new ManagerVO();
			vo.setId((String)request.getSession().getAttribute("userID"));

			ManagerVO vo2 = dao.selectOne(vo);
			System.out.println(vo2);

			request.setAttribute("vo2", vo2);
			
			RequestDispatcher rd = request.getRequestDispatcher("manager/manager_update.jsp");
			rd.forward(request, response);
		}else if(sPath.equals("/mng_updateOK.do")) {
			System.out.println("member_updateOK.do");
			vo = new ManagerVO();
			
			String uploadPath = request.getServletContext().getRealPath("upload");
			System.out.println("uploadPath:"+uploadPath);
			
			int size = 10 * 1024 * 1024;

			try {
				MultipartRequest multi = new MultipartRequest(request, uploadPath, size, "UTF-8",
						new DefaultFileRenamePolicy());
				
				vo.setId((String)request.getSession().getAttribute("userID"));
				vo.setPw(multi.getParameter("mngpw"));
				vo.setName(multi.getParameter("mngname"));
				vo.setPhone(multi.getParameter("mngphone"));
				vo.setEmail(multi.getParameter("mngemail"));
				vo.setBank(multi.getParameter("mngbank"));
				vo.setAccount(multi.getParameter("mngaccount"));

				Enumeration files = multi.getFileNames();

				String picture = (String) files.nextElement();
				System.out.println("pusa1:"+picture);
				String filename = multi.getFilesystemName(picture);
				System.out.println("filename:"+filename);
				
				vo.setProfile(filename);
				
				int res = dao.update(vo);
				
				if(res == 1) {
					System.out.println("업데이트 성공!");
					request.getSession().setAttribute("userProfile", filename);
					response.sendRedirect("index.do");
				}else {
					System.out.println("업데이트 실패!");
					response.sendRedirect("mng_update.do");
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
		}else if(sPath.equals("/mng_password.do")) {
			request.getSession().setAttribute("nextpage", request.getParameter("mng_nextpage"));
			
			RequestDispatcher rd = request.getRequestDispatcher("manager/mng_password.jsp");
			rd.forward(request, response);
		}else if(sPath.equals("/mng_passwordOK.do")) {			
			String pwCK = request.getParameter("passwordCK");
			
			vo = new ManagerVO();
			vo.setId((String)request.getSession().getAttribute("userID"));

			ManagerVO vo2 = dao.selectOne(vo);
			
			if(vo2.getPw().equals(pwCK)) {
				System.out.println("password_check성공");
				response.sendRedirect("" + request.getSession().getAttribute("nextpage"));
			}else {
				System.out.println("password_check실패");
				String str = (String)request.getSession().getAttribute("nextpage");
				response.sendRedirect("mng_password.do?msg=incorrect PassWord&mng_nextpage="+str);
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
