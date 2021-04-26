<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Main</title>
	<style>
		body{
			text-align: center;
		}
		
		.top {
			margin-bottom: 150px;
		}
		.top h1{
			display: inline;
		}
		
		.top > .top1{
			display: inline;
			position : absolute;
			top: 20px;
			right: 240px;
		}
		
		.top > .top2{
			display: inline;
			position : absolute;
			top: 20px;
			right: 140px;
		}
		
		.top > .top3{
			display: inline;
			position : absolute;
			top: 43px;
			right: 40px;
		}
		
		.top > .top4{
			display: inline;
			position : absolute;
			top: 83px;
			right: 40px;
		}
		
		.top > .top5{
			display: inline;
			position : absolute;
			top: 123px;
			right: 40px;
		}
		
		.top > .top6{
			display: inline;
			position : absolute;
			top: 163px;
			right: 40px;
		}
		
		.top > .top7{
			display: inline;
			position : absolute;
			top: 203px;
			right: 40px;
		}
		
		table{
			margin: 0 auto;
			border-collapse: collapse;
		}
		
		td{
			width: 200px;
		}
		
		td:nth-child(1) {
			border-right: 3px dashed gray;
		}
		
		tr:nth-child(2) {	
			border-bottom: 3px dashed gray;
		}
		
		tr:nth-child(2),
		tr:nth-child(3){
			color: white;
		}
	</style>
</head>
<body>
	<c:if test='${sessionScope.login != "mng_Successed" && sessionScope.login != "mem_Successed"}'>
		<div class="top">
			<h1>Main</h1>
			<form action="login.do" class="top3">
				<button type="submit" style="width: 50">로그인</button>
			</form>
		</div>
		<div class="mid">
			<table>
				<tr>
					<td>
						<form action="reservation.do">
							<button>예약</button>
						</form>
					</td>
					<td>
						<form action="rsv_checkAll.do">
							<button>예약확인 및 변경</button>
						</form>
					</td>
				</tr>
				<tr>
					<td>Line1</td>
					<td>    </td>				
				</tr>
				<tr>
					<td>Line2</td>
					<td>    </td>				
				</tr>
				<tr>
					<td>
						<form action="member_facility.do">
							<button>전체이용안내</button>
						</form>
					</td>
					<td>
						<form action="member_notice.do">
							<button>공지사항</button>	
						</form>
					</td>
				</tr>
			</table>
		</div>
	</c:if>
	
	<c:if test='${sessionScope.login == "mng_Successed"}'>
		<div class="top">
			<h1>Main</h1>
			<div class="top1">
				<img alt="" width="50" src="upload/${sessionScope.userProfile}">
			</div>
			<div class="top2"> 
				<h4>${sessionScope.userID }</h4>
			</div>
			<form action="logout.do" class="top3">
				<button style="width: 50">로그아웃</button>
			</form>
			<form action="memberAll.do" class="top4">
				<button style="width: 50">회원정보</button>
			</form>
			<form action="reservationAll.do" class="top5">
				<button style="width: 50">예약현황</button>
			</form>
			<form action="mng_password.do" class="top6">
				<input type="hidden" name="mng_nextpage" value="mng_delete.do">
				<button style="width: 50">회원탈퇴</button>
			</form>
			<form action="mng_password.do" class="top7">
				<input type="hidden" name="mng_nextpage" value="mng_update.do">
				<button style="width: 50">내 정보 수정</button>
			</form>
		</div>
		<div class="mid">
			<table>
				<tr>
					<td>
						<form action="reservation.do">
							<button>예약</button>
						</form>
					</td>
					<td>
						<form action="mng_password.do">
							<input type="hidden" name="mng_nextpage" value="rsv_checkAll.do">
							<button>예약확인</button>
						</form>
					</td>
				</tr>
				<tr>
					<td>Line1</td>
					<td>    </td>				
				</tr>
				<tr>
					<td>Line2</td>
					<td>    </td>				
				</tr>
				<tr>
					<td>
						<form action="manager_guide.do">
							<button>전체이용안내</button>
						</form>
					</td>
					<td>
						<form action="manager_notice.do">
							<button>공지사항</button>	
						</form>
					</td>
				</tr>
			</table>		
		</div>
	</c:if>

	<c:if test='${sessionScope.login == "mem_Successed"}'>
		<div class="top">
			<h1>Main</h1>
			<div class="top1">
				<img alt="" width="50" src="upload/${sessionScope.userProfile}">
			</div>
			<div class="top2">
				<h4>${sessionScope.userID }</h4>
			</div>
			<form action="logout.do" class="top3">
				<button style="width: 50">로그아웃</button>
			</form>
			<form action="mem_password.do" class="top4">
				<input type="hidden" name="mem_nextpage" value="mem_delete.do">
				<button style="width: 50">회원탈퇴</button>
			</form>
			<form action="mem_password.do" class="top5">
				<input type="hidden" name="mem_nextpage" value="mem_update.do">
				<button style="width: 50">내 정보 수정</button>
			</form>
		</div>
		<div class="mid">
			<table>
				<tr>
					<td>
						<form action="reservation.do">
							<button>예약</button>
						</form>
					</td>
					<td>
						<form action="mem_password.do">
							<input type="hidden" name="mem_nextpage" value="rsv_checkAll.do">
							<button>예약확인</button>
						</form>
					</td>
				</tr>
				<tr>
					<td>Line1</td>
					<td>    </td>				
				</tr>
				<tr>
					<td>Line2</td>
					<td>    </td>				
				</tr>
				<tr>
					<td>
						<form action="member_facility.do">
							<button>전체이용안내</button>
						</form>
					</td>
					<td>
						<form action="member_notice.do">
							<button>공지사항</button>	
						</form>
					</td>
				</tr>
			</table>			
		</div>	
	</c:if>
</body>
</html>