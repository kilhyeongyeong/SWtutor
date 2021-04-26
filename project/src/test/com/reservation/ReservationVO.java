package test.com.reservation;

public class ReservationVO {
	
	private String id;
	private String name;
	private String email;
	private int adultNum;
	private int childNum;
	private int babyNum;
	private int Month;
	private int Day;
	private int price;
	private String pastName;
	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public int getAdultNum() {
		return adultNum;
	}
	public void setAdultNum(int adultNum) {
		this.adultNum = adultNum;
	}
	public int getChildNum() {
		return childNum;
	}
	public void setChildNum(int childNum) {
		this.childNum = childNum;
	}
	public int getBabyNum() {
		return babyNum;
	}
	public void setBabyNum(int babyNum) {
		this.babyNum = babyNum;
	}
	public int getMonth() {
		return Month;
	}
	public void setMonth(int month) {
		Month = month;
	}
	public int getDay() {
		return Day;
	}
	public void setDay(int day) {
		Day = day;
	}
	public int getPrice() {
		return price;
	}
	public void setPrice(int price) {
		this.price = price;
	}
	public String getPastName() {
		return pastName;
	}
	public void setPastName(String pastName) {
		this.pastName = pastName;
	}
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + Day;
		result = prime * result + Month;
		result = prime * result + adultNum;
		result = prime * result + babyNum;
		result = prime * result + childNum;
		result = prime * result + ((email == null) ? 0 : email.hashCode());
		result = prime * result + ((id == null) ? 0 : id.hashCode());
		result = prime * result + ((name == null) ? 0 : name.hashCode());
		result = prime * result + ((pastName == null) ? 0 : pastName.hashCode());
		result = prime * result + price;
		return result;
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		ReservationVO other = (ReservationVO) obj;
		if (Day != other.Day)
			return false;
		if (Month != other.Month)
			return false;
		if (adultNum != other.adultNum)
			return false;
		if (babyNum != other.babyNum)
			return false;
		if (childNum != other.childNum)
			return false;
		if (email == null) {
			if (other.email != null)
				return false;
		} else if (!email.equals(other.email))
			return false;
		if (id == null) {
			if (other.id != null)
				return false;
		} else if (!id.equals(other.id))
			return false;
		if (name == null) {
			if (other.name != null)
				return false;
		} else if (!name.equals(other.name))
			return false;
		if (pastName == null) {
			if (other.pastName != null)
				return false;
		} else if (!pastName.equals(other.pastName))
			return false;
		if (price != other.price)
			return false;
		return true;
	}
	@Override
	public String toString() {
		return "ReservationVO [id=" + id + ", name=" + name + ", email=" + email + ", adultNum=" + adultNum
				+ ", childNum=" + childNum + ", babyNum=" + babyNum + ", Month=" + Month + ", Day=" + Day + ", price="
				+ price + ", pastName=" + pastName + "]";
	}
	
	
	
}
