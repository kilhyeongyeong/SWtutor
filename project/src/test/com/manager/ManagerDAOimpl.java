package test.com.manager;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import test.com.member.MemberVO;

public class ManagerDAOimpl implements ManagerDAO {
	
	private final String DRIVER_NAME = "oracle.jdbc.OracleDriver";
	private final String URL = "jdbc:oracle:thin:@localhost:1521:xe";
	private final String USER_NAME = "hyeon";
	private final String PASSWORD = "hyeon98";

	private Connection conn;
	private PreparedStatement pstmt;
	private ResultSet rs;
	
	public ManagerDAOimpl() {
		System.out.println("ManagerDAOimpl()...");
		try {
			Class.forName(DRIVER_NAME);
			System.out.println("successed");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}

	@Override
	public int insert(ManagerVO vo) {
		System.out.println("insert()...");
		System.out.println(vo);
		int flag=0;
		
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed");
			
			String sql = "insert into manager(img,id,pw,name,phone,email,bank,account) values(?,?,?,?,?,?,?,?)";
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setString(1, vo.getProfile());
			pstmt.setString(2, vo.getId());
			pstmt.setString(3, vo.getPw());
			pstmt.setString(4, vo.getName());
			pstmt.setString(5, vo.getPhone());
			pstmt.setString(6, vo.getEmail());
			pstmt.setString(7, vo.getBank());
			pstmt.setString(8, vo.getAccount());
			
			flag = pstmt.executeUpdate();
			
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {
			if (rs != null) {
				try {
					rs.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (pstmt != null) {
				try {
					pstmt.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (conn != null) {
				try {
					conn.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
		}
		return flag;
	}

	@Override
	public int update(ManagerVO vo) {
		System.out.println("update()...");
		System.out.println(vo);
		
		int flag = 0;
		
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed....");
			
			String sql = "update manager set pw=?,name=?,phone=?,email=?,bank=?, account=?,img=? where id=?";
			pstmt = conn.prepareStatement(sql);

			pstmt.setString(1, vo.getPw());
			pstmt.setString(2, vo.getName());
			pstmt.setString(3, vo.getPhone());
			pstmt.setString(4, vo.getEmail());
			pstmt.setString(5, vo.getBank());
			pstmt.setString(6, vo.getAccount());
			pstmt.setString(7, vo.getProfile());
			pstmt.setString(8, vo.getId());
			
			flag = pstmt.executeUpdate();
			
			
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {
			if (rs != null) {
				try {
					rs.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (pstmt != null) {
				try {
					pstmt.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (conn != null) {
				try {
					conn.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
		}
		return flag;
	}

	@Override
	public int delete(ManagerVO vo) {
		System.out.println("delete()...");
		System.out.println(vo);
		
		int flag = 0;
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed....");
			
			String sql = "delete from manager where id=?";
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, vo.getId());
			
			flag = pstmt.executeUpdate();
			
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {
			if (rs != null) {
				try {
					rs.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (pstmt != null) {
				try {
					pstmt.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (conn != null) {
				try {
					conn.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
		}
		return flag;
	}

	@Override
	public int idCheck(ManagerVO vo) {
		System.out.println("idCheck()....");
		System.out.println(vo);
		int res = 0;
		
		if(vo.getId().trim().length()==0) return 1;
		
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed....");
			
			String sql = "select * from manager where id = ?";
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, vo.getId());
			
			rs = pstmt.executeQuery();
			while(rs.next()) {
				return 1;
			}
			
			if(res == 0) {
				sql = "select * from member where id = ?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setString(1, vo.getId());
				
				rs = pstmt.executeQuery();
				while(rs.next()) {
					return 1;
				}
			}
			
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {
			if (rs != null) {
				try {
					rs.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (pstmt != null) {
				try {
					pstmt.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (conn != null) {
				try {
					conn.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
		}
		return res;
	}

	@Override
	public String loginOK(ManagerVO vo) {
		System.out.println("loginCheck()....");
		System.out.println(vo);
		
		ManagerVO vo2 = new ManagerVO();
		int check=0;
		
		if(vo.getId().trim().length()==0 || vo.getPw().trim().length()==0) return "NotID";
		
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed....");
			
			String sql = "select * from manager where id = ?";
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, vo.getId());
			
			rs = pstmt.executeQuery();
			while(rs.next()) {
				check=1;
			}
			
			if(check == 1) {
				String sql1 = "select * from manager where id=? and pw = ?";
				pstmt = conn.prepareStatement(sql1);
				pstmt.setString(1, vo.getId());
				pstmt.setString(2, vo.getPw());
				
				rs = pstmt.executeQuery();
				while(rs.next()) {
					check=2;
					vo2.setProfile(rs.getString("img"));
				}
			}
			
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {
			if (rs != null) {
				try {
					rs.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (pstmt != null) {
				try {
					pstmt.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (conn != null) {
				try {
					conn.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
		}
		
		if(check==2) {
			return vo2.getProfile();
		}else if(check == 1){
			return "WrongPW";
		}else {
			return "NotID";
		}
	}

	@Override
	public ManagerVO selectOne(ManagerVO vo) {
		System.out.println("selectOne()...");
		System.out.println(vo);
		
		
		ManagerVO vo2 = new ManagerVO();
		
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed....");
			
			String sql = "select * from manager where id=?";
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, vo.getId());
			
			rs = pstmt.executeQuery();
			while(rs.next()) {
				vo2.setProfile(rs.getString("img"));
				vo2.setId(rs.getString("id"));
				vo2.setPw(rs.getString("pw"));
				vo2.setName(rs.getString("name"));
				vo2.setPhone(rs.getString("phone"));
				vo2.setEmail(rs.getString("email"));
				vo2.setBank(rs.getString("bank"));
				vo2.setAccount(rs.getString("account"));
			}
			
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {
			if (rs != null) {
				try {
					rs.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (pstmt != null) {
				try {
					pstmt.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (conn != null) {
				try {
					conn.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
		}

		return vo2;
	}

	@Override
	public ManagerVO idFind(ManagerVO vo) {
		System.out.println("idFind()...");
		System.out.println(vo);

		ManagerVO vo2 = new ManagerVO();
		
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed....");
			
			String sql = "select * from manager where name=? and email=?";
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setString(1, vo.getName());
			pstmt.setString(2, vo.getEmail());
			
			rs = pstmt.executeQuery();
			while(rs.next()) {
				vo2.setId(rs.getString("id"));
				vo2.setPw(rs.getString("pw"));
			}
			
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {
			if (rs != null) {
				try {
					rs.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (pstmt != null) {
				try {
					pstmt.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (conn != null) {
				try {
					conn.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
		}

		return vo2;
	}

}
