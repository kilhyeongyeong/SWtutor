<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Insert title here</title>
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
	</style>
</head>
<body>
	<div class="top">
		<h1>내 정보 수정</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px">Home</button>
		</form>
	</div>
	<form action="member_updateOK.do" method="post" enctype="multipart/form-data">
		<table border="1">
			<tr>	
				<td>아이디</td>
				<td>${sessionScope.userID }</td>
			</tr>
			<tr>
				<td>비밀번호</td>
				<td><input type="text" name="mempw" value="${vo2.pw}"></td>
			</tr>
			<tr>
				<td>이름</td>
				<td><input type="text" name="memname" value="${vo2.name}"></td>
			</tr>
			<tr>	
				<td>핸드폰번호</td>
				<td><input type="text" name="memphone" value="${vo2.phone}"></td>
			</tr>
			<tr>
				<td>이메일</td>
				<td><input type="text" name="mememail" value="${vo2.email}"></td>
			</tr>
			<tr>
				<td>프로필사진</td>
				<td><input type="file" name="userProfile" value="${vo2.profile}"></td>
			</tr>
			<tr>
				<td colspan="2"><input type="submit" value="확인"></td>
			</tr>
		</table>
	</form>
</body>
</html>