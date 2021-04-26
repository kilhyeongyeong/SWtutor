package test.com.reservation;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import test.com.board.BoardVO;

public class ReservationDAOimpl implements ReservationDAO {
	
	private final String DRIVER_NAME = "oracle.jdbc.OracleDriver";
	private final String URL = "jdbc:oracle:thin:@localhost:1521:xe";
	private final String USER_NAME = "hyeon";
	private final String PASSWORD = "hyeon98";

	private Connection conn;
	private PreparedStatement pstmt;
	private ResultSet rs;
	
	public ReservationDAOimpl() {
		System.out.println("ManagerDAOimpl()...");
		try {
			Class.forName(DRIVER_NAME);
			System.out.println("find successed");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}

	@Override
	public int insert(ReservationVO vo) {
		System.out.println("insert()...");
		System.out.println(vo);
		int flag=0;
		
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed");
			
			String sql = "insert into reservation(id,name,email,month,day,adult_num,child_num,baby_num,price) "
					+ "values(?,?,?,?,?,?,?,?,?)";
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setString(1, vo.getId());
			pstmt.setString(2, vo.getName());
			pstmt.setString(3, vo.getEmail());
			pstmt.setInt(4, vo.getMonth());
			pstmt.setInt(5, vo.getDay());
			pstmt.setInt(6, vo.getAdultNum());
			pstmt.setInt(7, vo.getChildNum());
			pstmt.setInt(8, vo.getBabyNum());
			pstmt.setInt(9, vo.getPrice());
			
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
	public int update(ReservationVO vo) {
		System.out.println("update()...");
		System.out.println(vo);
		int flag = 0;
		
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed....");
			
			String sql = "update reservation set name=?, email=?, adult_num=?, child_num=?, baby_num=?, month=?, "
					+ "day=?, price=? where id=? and name=?";
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setString(1, vo.getName());
			pstmt.setString(2, vo.getEmail());
			pstmt.setInt(3, vo.getAdultNum());
			pstmt.setInt(4, vo.getChildNum());
			pstmt.setInt(5, vo.getBabyNum());
			pstmt.setInt(6, vo.getMonth());
			pstmt.setInt(7, vo.getDay());
			pstmt.setInt(8, vo.getPrice());
			pstmt.setString(9, vo.getId());
			pstmt.setString(10, vo.getPastName());
			
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
	public int delete(ReservationVO vo, int num) {
		System.out.println("delete()...");
		System.out.println(vo);
		
		int flag = 0;
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed....");
			if(num == 0) {
				String sql = "delete from reservation where id=? and name=?";
				pstmt = conn.prepareStatement(sql);
				
				pstmt.setString(1, vo.getId());
				pstmt.setString(2, vo.getName());
			}else {
				String sql = "delete from reservation where id=?";
				pstmt = conn.prepareStatement(sql);
				
				pstmt.setString(1, vo.getId());
			}
			
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
	public List<ReservationVO> selectAll(ReservationVO vo) {
		System.out.println("selectAll()...");
		
		List<ReservationVO> list = new ArrayList<ReservationVO>();
		
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed....");
			
			String sql = "select * from reservation where id=? order by name";
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setString(1, vo.getId());
			
			rs = pstmt.executeQuery();
			while(rs.next()) {
				ReservationVO vo2 = new ReservationVO();
				
				vo2.setId(rs.getString("id"));
				vo2.setName(rs.getString("name"));
				vo2.setEmail(rs.getString("email"));
				vo2.setMonth(rs.getInt("month"));
				vo2.setDay(rs.getInt("day"));
				vo2.setAdultNum(rs.getInt("adult_num"));
				vo2.setChildNum(rs.getInt("child_num"));
				vo2.setBabyNum(rs.getInt("baby_num"));
				vo2.setPrice(rs.getInt("price"));
				list.add(vo2);
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

		return list;
	}

	@Override
	public ReservationVO selectOne(ReservationVO vo) {
		System.out.println("selectOne()...");
		System.out.println(vo);
		
		ReservationVO vo2 = new ReservationVO();
		
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed....");
			
			String sql = "select * from reservation where id=? and name=?";
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setString(1, vo.getId());
			pstmt.setString(2, vo.getName());
			
			rs = pstmt.executeQuery();
			while(rs.next()) {
				vo2.setId(rs.getString("id"));
				vo2.setName(rs.getString("name"));
				vo2.setEmail(rs.getString("email"));
				vo2.setMonth(rs.getInt("month"));
				vo2.setDay(rs.getInt("day"));
				vo2.setAdultNum(rs.getInt("adult_num"));
				vo2.setChildNum(rs.getInt("child_num"));
				vo2.setBabyNum(rs.getInt("baby_num"));
				vo2.setPrice(rs.getInt("price"));
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
	public int price(String state, String adult_state, String adult, String child, String baby, int adultNum, int childNum, int babyNum) {
		int adult_price = 0;
		int child_price = 0;
		int baby_price =0 ;
		
		if(state.equals("mem_Successed")) {
			System.out.println("mem_reservation");
			
			if(adult_state == null) {
				adult_price = 45000*adultNum;
				child_price = 35000*childNum;
				baby_price = 28000*babyNum;
			}else {
				int adult_p = Integer.parseInt(adult);
				int child_p = Integer.parseInt(child);
				int baby_p = Integer.parseInt(baby);
				
				adult_price = adult_p*adultNum;
				child_price = child_p*childNum;
				baby_price = baby_p*babyNum;
			}
		}else if(state.equals("mng_Successed")) {
			System.out.println("mng_reservation");
			
			if(adult_state == null) {
				adult_price = 45000*adultNum - 22500;
				child_price = 35000*childNum;
				baby_price = 28000*babyNum;
			}else {
				int adult_p = Integer.parseInt(adult);
				int child_p = Integer.parseInt(child);
				int baby_p = Integer.parseInt(baby);
				
				adult_price = adult_p*adultNum - (int)(adult_p*0.5);
				child_price = child_p*childNum;
				baby_price = baby_p*babyNum;
			}
			
		}
		return adult_price + child_price + baby_price;
	}

	@Override
	public List<ReservationVO> selectAll() {
		System.out.println("selectAll()...");
		List<ReservationVO> list = new ArrayList<ReservationVO>();
		
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed....");
			
			String sql = "select * from reservation order by id";
			pstmt = conn.prepareStatement(sql);
			
			rs = pstmt.executeQuery();
			
			while(rs.next()) {
				ReservationVO vo2 = new ReservationVO();
				
				vo2.setId(rs.getString("id"));
				vo2.setName(rs.getString("name"));
				vo2.setEmail(rs.getString("email"));
				vo2.setMonth(rs.getInt("month"));
				vo2.setDay(rs.getInt("day"));
				vo2.setAdultNum(rs.getInt("adult_num"));
				vo2.setChildNum(rs.getInt("child_num"));
				vo2.setChildNum(rs.getInt("baby_num"));
				vo2.setPrice(rs.getInt("price"));
				list.add(vo2);
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

		return list;
	}

	@Override
	public int totalPrice() {
		System.out.println("delete()...");
		
		int sum = 0;
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed....");
			
			String sql = "select price from reservation";
			pstmt = conn.prepareStatement(sql);

			rs = pstmt.executeQuery();
			
			while(rs.next()) {
				sum += rs.getInt("price");
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
		
		return sum;
	}

	@Override
	public int reservationOK(ReservationVO vo) {
		System.out.println("reservationOK()....");
		System.out.println(vo);
		int res = 0;
		
		try {
			conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
			System.out.println("conn successed");
			
			String sql = "select * from reservation where id=? and name=?";
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setString(1, vo.getId());
			pstmt.setString(2, vo.getName());
			
			rs = pstmt.executeQuery();
			while(rs.next()) {
				res = 1;
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
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

}
