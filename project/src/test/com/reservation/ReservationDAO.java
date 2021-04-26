package test.com.reservation;

import java.util.*;

public interface ReservationDAO {
	
	public int insert(ReservationVO vo);
	
	public int update(ReservationVO vo);
	
	public int delete(ReservationVO vo, int num);
	
	public int reservationOK(ReservationVO vo);
	
	public List<ReservationVO> selectAll(ReservationVO vo);
	
	public List<ReservationVO> selectAll();
	
	public ReservationVO selectOne(ReservationVO vo);
	
	public int totalPrice();
	
	public int price(String state, String adult_state, String adult, String child, String baby, int adultNum, int childNum, int babyNum);

}
