<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Insert title here</title>
	<style>
		h1{
			text-align: center;
		}
		
		table {
			margin: 0 auto;
			text-align: center;
		}
		
		tr:nth-child(7),
		tr:nth-child(2) {
			color: white;
		}
		
		td:nth-child(1){
			width: 50px;
		}
		.top{
			margin-bottom: 100px;
		}
		.top form{
			display: inline;
			position : absolute;
			top: 20px;
			right: 40px;
		}
	</style>
</head>
<body>
	<div class="top">
		<h1>예약</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px">Home</button>
		</form>
	</div>

	<form action="reservationOK.do">
		<table>
			<tr>
				<td colspan="2"></td>
				<td width="50px"><b>아이디</b></td>
				<td><b>${sessionScope.userID}</b></td>
			</tr>
			<tr>	
				<td>Line</td>
			</tr>
			<tr>
				<td>대인</td>
				<td><input type="number" name="rsv_adult" value="0">명</td>
				<td width="40"></td>
				<td>대표자 이름</td>
				<td><input type="text" name="rsv_name" ></td>
			</tr>
			<tr>
				<td>소인</td>
				<td><input type="number" name="rsv_child" value=0>명</td>
				<td width="40"></td>
				<td>이메일</td>
				<td><input type="text" name="rsv_email"></td>
			</tr>
			<tr>
				<td>유아</td>
				<td><input type="number" name="rsv_baby" value="0">명</td>
				<td colspan="3"></td>
			</tr>
			<tr>
				<td>날짜</td>
				<td><input type="number" name="rsv_month">월</td>
				<td colspan="2" width="200px"><input type="number" name="rsv_day">일</td>
				<td></td>
			</tr>
			<tr>
				<td>Line</td>
				<td>Line</td>
				<td>Line</td>
				<td>Line</td>
			</tr>
			<tr>
				<td colspan="2"></td>
				<td><input type="submit" value="확인"></td>
				<c:if test="${rsv_nameCheck != null }"><td>${rsv_nameCheck}</td></c:if>
			</tr>
		</table>
	</form>
</body>
</html>