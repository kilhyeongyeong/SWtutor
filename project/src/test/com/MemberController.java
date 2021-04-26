package test.com;

import java.io.IOException;
import java.util.Enumeration;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.oreilly.servlet.MultipartRequest;
import com.oreilly.servlet.multipart.DefaultFileRenamePolicy;

import test.com.board.BoardVO;
import test.com.manager.ManagerVO;
import test.com.member.MemberDAO;
import test.com.member.MemberDAOimpl;
import test.com.member.MemberVO;

/**
 * Servlet implementation class MemberController
 */
@WebServlet({"/member_signup.do", "/member_insert.do", "/member_idCheck.do", "/member_facility.do",
	"/member_notice.do", "/memberAll.do", "/mem_update.do", "/member_updateOK.do", "/mem_password.do",
	"/mem_passwordOK.do","/mem_delete.do"})
public class MemberController extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public MemberController() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//response.getWriter().append("Served at: ").append(request.getContextPath());
		
		MemberVO vo = new MemberVO();
		MemberDAO dao = new MemberDAOimpl();
		
		
		String sPath = request.getServletPath();
		System.out.println(sPath);
		
		if(sPath.equals("/member_signup.do")) {//--------------------------------------------------------------------------------------------index.do
			System.out.println("member_signup.jsp");
			System.out.println();
			
			RequestDispatcher rd = request.getRequestDispatcher("member/member_signup.jsp");
			rd.forward(request, response);
//-------------------------------------------------------------------------------------------------------------------		
		}else if(sPath.equals("/member_insert.do")) {//--------------------------------------------------------------------------------------------index.do
			System.out.println("member_insert.jsp");
			
			vo = new MemberVO();
			
			String uploadPath = request.getServletContext().getRealPath("upload");
			System.out.println("uploadPath:"+uploadPath);
			
			int size = 10 * 1024 * 1024;

			try {
				MultipartRequest multi = new MultipartRequest(request, uploadPath, size, "UTF-8",
						new DefaultFileRenamePolicy());
				
				vo.setId(multi.getParameter("memid"));
				vo.setPw(multi.getParameter("mempw"));
				vo.setName(multi.getParameter("memname"));
				vo.setPhone(multi.getParameter("memphone"));
				vo.setEmail(multi.getParameter("mememail"));

				Enumeration files = multi.getFileNames();

				String picture = (String) files.nextElement();
				System.out.println("pusa1:"+picture);
				String filename = multi.getFilesystemName(picture);
				System.out.println("filename:"+filename);
				
				vo.setProfile(filename);
				
				int res = dao.insert(vo);
				
				if(res == 1) {
					System.out.println("로그인 성공!");
					request.getSession().setAttribute("userProfile", filename);
					response.sendRedirect("login.do");
				}else {
					System.out.println("로그인 실패!");
					response.sendRedirect("member_signup.do");
				}
			} catch (Exception e) {
				e.printStackTrace();
			} 
//-------------------------------------------------------------------------------------------------------------------
		}else if(sPath.equals("/member_idCheck.do")) {//--------------------------------------------------------------------------------------------index.do
			System.out.println("member_idCheck");
			
			vo = new MemberVO();
			vo.setId(request.getParameter("memid_check"));
			
			String res = dao.idCheck(vo);
			
			if(res.equals("OK")) {
				response.sendRedirect("member_signup.do?id=" + vo.getId() + "&msg=OK");

			}else {
				response.sendRedirect("member_signup.do?msg=NotOK");

			}
//-------------------------------------------------------------------------------------------------------------------
		}else if(sPath.equals("/member_facility.do")) {//--------------------------------------------------------------------------------------------index.do
			System.out.println("member_facility");
			
			RequestDispatcher rd = request.getRequestDispatcher("member/member_facility.jsp");
			rd.forward(request, response);
//-------------------------------------------------------------------------------------------------------------------
		}else if(sPath.equals("/member_notice.do")) {
			
			response.sendRedirect("board_selectAll.do");
//-------------------------------------------------------------------------------------------------------------------			
		}else if(sPath.equals("/memberAll.do")) {
			System.out.println("member_selectAll");
			
			List<MemberVO> list = dao.selectAll();
			for (MemberVO x : list) {
				System.out.println(x);
			}

			request.setAttribute("memberlist", list);
			
			RequestDispatcher rd = request.getRequestDispatcher("member/memberAll.jsp");
			rd.forward(request, response);
//-------------------------------------------------------------------------------------------------------------------
		}else if(sPath.equals("/mem_update.do")) {
			vo = new MemberVO();
			vo.setId((String)request.getSession().getAttribute("userID"));

			MemberVO vo2 = dao.selectOne(vo);
			System.out.println(vo2);

			request.setAttribute("vo2", vo2);
			
			RequestDispatcher rd = request.getRequestDispatcher("member/member_update.jsp");
			rd.forward(request, response);
//-------------------------------------------------------------------------------------------------------------------
		}else if(sPath.equals("/member_updateOK.do")) {
			System.out.println("member_updateOK.do");
			vo = new MemberVO();
			
			String uploadPath = request.getServletContext().getRealPath("upload");
			System.out.println("uploadPath:"+uploadPath);
			
			int size = 10 * 1024 * 1024;

			try {
				MultipartRequest multi = new MultipartRequest(request, uploadPath, size, "UTF-8",
						new DefaultFileRenamePolicy());
				
				vo.setId((String)request.getSession().getAttribute("userID"));
				vo.setPw(multi.getParameter("mempw"));
				vo.setName(multi.getParameter("memname"));
				vo.setPhone(multi.getParameter("memphone"));
				vo.setEmail(multi.getParameter("mememail"));

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
					response.sendRedirect("mem_update.do");
				}
			} catch (Exception e) {
				e.printStackTrace();
			} 
//-------------------------------------------------------------------------------------------------------------------
		}else if(sPath.equals("/mem_password.do")) {
			request.getSession().setAttribute("nextpage", request.getParameter("mem_nextpage"));
			
			RequestDispatcher rd = request.getRequestDispatcher("member/mem_password.jsp");
			rd.forward(request, response);
//-------------------------------------------------------------------------------------------------------------------
		}else if(sPath.equals("/mem_passwordOK.do")) {
			String pwCK = request.getParameter("passwordCK");
			
			vo = new MemberVO();
			vo.setId((String)request.getSession().getAttribute("userID"));

			MemberVO vo2 = dao.selectOne(vo);
			
			if(vo2.getPw().equals(pwCK)) {
				System.out.println("password_check성공");
				response.sendRedirect("" + request.getSession().getAttribute("nextpage"));
			}else {
				System.out.println("password_check실패");
				String str = (String)request.getSession().getAttribute("nextpage");
				response.sendRedirect("mem_password.do?msg=incorrect PassWord&mem_nextpage="+str);
			}
//-------------------------------------------------------------------------------------------------------------------
		}else if(sPath.equals("/mem_delete.do")) {
			vo = new MemberVO();
			vo.setId((String)request.getSession().getAttribute("userID"));

			int result = dao.delete(vo);

			if (result == 1) {
				System.out.println("회원탈퇴 성공!");
				response.sendRedirect("rsv_deleteAll.do");
			}else {
				System.out.println("회원탈퇴 실패!");
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
