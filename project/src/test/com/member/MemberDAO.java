package test.com.member;

import java.util.*;

public interface MemberDAO {
	
	public int insert(MemberVO vo);
	
	public int update(MemberVO vo);
	
	public int delete(MemberVO vo); 
	
	public List<MemberVO> selectAll();
	
	public MemberVO selectOne(MemberVO vo);
	
	public MemberVO idFind(MemberVO vo);
	
	public String idCheck(MemberVO vo);
	
	public String loginOK(MemberVO vo);

}
