<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>회원가입</title>
	<style>
		body{
			text-align: center;
		}
		
		.top form{
			display: inline;
			position : absolute;
			top: 20px;
			right: 40px;
		}
		
		table {
			margin: 0 auto;
		}
		
		.mid{
			margin : 35px;
		}
		
		td:nth-child(1) : td:nth-child(6) {
			text-align: left;
			width: 100px;
		}
		
		tr:nth-child(9) {
			color: white;
		}
		
		tr:nth-child(7) {
			text-align: center;
		}
	</style>
</head>
<body>
	<div class="top">
		<h1>회원가입</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px">Home</button>
		</form>
	</div>
	<div class="mid">
		<form action="member_idCheck.do" method="post">
			아이디 중복체크 : <input type="text" name="memid_check"> 
			<input type="submit" value="확인"> ${param.msg}
		</form>
	</div>
	
	<form action="member_insert.do" method="post" enctype="multipart/form-data">
		<table border="1">
			<tr>	
				<td>아이디</td>
				<td><input type="text" name="memid" value=${param.id }></td>
			</tr>
			<tr>
				<td>비밀번호</td>
				<td><input type="text" name="mempw"></td>
			</tr>
			<tr>
				<td>이름</td>
				<td><input type="text" name="memname"></td>
			</tr>
			<tr>	
				<td>핸드폰번호</td>
				<td><input type="text" name="memphone"></td>
			</tr>
			<tr>
				<td>이메일</td>
				<td><input type="text" name="mememail"></td>
			</tr>
			<tr>
				<td>프로필사진</td>
				<td><input type="file" name="userProfile"></td>
			</tr>
			<tr>
				<td colspan="2"><input type="submit" value="확인"></td>
			</tr>
		</table>
	</form>
</body>
</html>