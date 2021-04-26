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
		
		table {
			margin: 0 auto;
			border-collapse: collapse;
			border: 0px white;
		}
		
		tr:nth-child(3){
			border-bottom: 4px double gray;
		}
		
		tr:nth-child(2) {
			color: white;
		}
	</style>
</head>
<body>
	<div class="top">
		<h1>예약 목록</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px"><b>확인</b></button>
		</form>
	</div>
	
	<table border="1">
		<tr>
			<td></td>
			<td><b>아이디</b></td>
			<td colspan="3"><b>${sessionScope.userID}</b></td>
			<td></td>
		</tr>
		<tr>
			<td colspan="6">Line</td>
		</tr>
		<tr>
			<th>이름</th>
			<th>날짜</th>
			<th>어른</th>
			<th>소인</th>
			<th>유아</th>
			<th>가격</th>
		</tr>
		<c:forEach var="vo" items="${list}">
			<tr>
				<td width="55px"><a href="rsv_checkOne.do?ch_name=${vo.name}">${vo.name}</a></td>
				<td width="80px">${vo.month}월 ${vo.day }일</td>
				<td width="40px">${vo.adultNum}명</td>
				<td width="40px">${vo.childNum}명</td>
				<td width="40px">${vo.babyNum}명</td>
				<td width="80px">${vo.price}명</td>
			</tr>
		</c:forEach>
	</table>
</body>
</html>