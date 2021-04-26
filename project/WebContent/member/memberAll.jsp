<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
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
		
		table{
			margin: 0 auto;
		}
	</style>
</head>
<body>
	<div class="top">
		<h1>회원정보</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px"><b>확인</b></button>
		</form>
	</div>
	<table border="1">
		<tr>
			<td>프로필사진</td>
			<td>아이디</td>
			<td>비밀번호</td>
			<td>이름</td>
			<td>핸드폰 번호</td>
			<td>이메일</td>
		</tr>
		<c:forEach var="vo" items="${memberlist}"> <%--memberController->memberall.do --%>
			<tr>
				<td><img alt="" width="50" src="upload/${vo.profile}"></td>
				<td>${vo.id}</td>
				<td>${vo.pw}</td>
				<td>${vo.name}</td>
				<td>${vo.phone}</td>
				<td>${vo.email}</td>
			</tr>
		</c:forEach>
	</table>

</body>
</html>