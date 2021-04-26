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
		
		td:nth-child(4){
			width: 80px;
		}
		
		td:nth-child(5),
		td:nth-child(6),
		td:nth-child(7){
			width: 60px;
		}
		
		td:nth-child(8){
			width: 100px;
		}
	</style>
</head>
<body>
	<div class="top">
		<h1>예매현황</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px"><b>확인</b></button>
		</form>
	</div>
	
	<table border="1">
		<tr>
			<td>아이디</td>
			<td>이름</td>
			<td>이메일</td>
			<td>날짜</td>
			<td>대인</td>
			<td>소인</td>
			<td>유아</td>
			<td>가격</td>
		</tr>
		<c:forEach var="vo" items="${reservationlist}"> <%--reservationController->reservationAll.do --%>
			<tr>
				<td>${vo.id}</td>
				<td>${vo.name}</td>
				<td>${vo.email}</td>
				<td>${vo.month}월 ${vo.day}일</td>
				<td>${vo.adultNum}명</td>
				<td>${vo.childNum}명</td>
				<td>${vo.babyNum}명</td>
				<td>${vo.price}원</td>
			</tr>
		</c:forEach>
		<tr>
			<td colspan="5"></td>
			<td colspan="2">총합계 : </td>
			<td>${reservation_totalPrice}원</td>
		</tr>
	</table>
</body>
</html>