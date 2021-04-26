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
		}
		
		tr:nth-child(2) {
			color: white;
		}
		
		.bottom{
			margin-top: 50px;
			display: inline-block;
		}
		
		.bottom2{
			position: relative;
			bottom: 30px;
	        left: 50px;
		}
	</style>
</head>
<body>
	<div class="top">
		<h1>예약 확인</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px"><b>확인</b></button>
		</form>
	</div>
		
	<table>
		<tr>
			<td width="50px"></td>
			<td><b>이름 : </b></td>
			<td colspan="2"><b>${reservation_vo2.name }</b></td>
			
		</tr>
		<tr>
			<td>Line</td>
		</tr>
		<tr>
			<td>대인 : </td>
			<td>${reservation_vo2.adultNum }명</td>
			<td></td>
			<td width="50px">날짜 : </td>
			<td>${reservation_vo2.month }월 ${reservation_vo2.day }일</td>
		</tr>
		<tr>
			<td>소인 : </td>
			<td>${reservation_vo2.childNum }명</td>
			<td></td>
			<td>가격 : </td>
			<td>${reservation_vo2.price }원</td>
		</tr>
		<tr>
			<td>유아 : </td>
			<td>${reservation_vo2.babyNum }명</td>
		</tr>
	</table>
	<div class="bottom">
		<div class="bottom1">
			<form action="rsv_revise.do">
				<input type="hidden" name="rsv_update" value="${reservation_vo2.name }">
				<button style="height: 30px;">변경</button>
			</form>
		</div>
		<div class="bottom2">
			<form action="rsv_delete.do">
				<input type="hidden" name="rsv_delete" value="${reservation_vo2.name }">
				<button style="height: 30px">삭제</button>
			</form>
		</div>	
	</div>
	
</body>
</html>