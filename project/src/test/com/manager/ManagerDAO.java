package test.com.manager;

public interface ManagerDAO {
	
	public int insert(ManagerVO vo);
	
	public int update(ManagerVO vo);
	
	public int delete(ManagerVO vo);
	
	public int idCheck(ManagerVO vo);
	
	public String loginOK(ManagerVO vo);
	
	public ManagerVO selectOne(ManagerVO vo);
	
	public ManagerVO idFind(ManagerVO vo);
	
}
