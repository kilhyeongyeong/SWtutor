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
		
		table{
			margin : 0 auto;
		}
		
		tr:nth-child(2) {
			color: white;
		}
		
		tr:nth-child(7) {
			color: white;
		}
	</style>
</head>
<body>
	<div class="top">
		<h1>전체이용안내</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px"><b>확인</b></button>
		</form>
	</div>
	<form action="rsv_reviseOK.do">
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
				<td width="50px">대인</td>
				<td><input type="number" name="rsv_re_adult" value="${reservation_revise_vo2.adultNum }">명</td>
				<td width="40"></td>
				<td>대표자 이름</td>
				<td><input type="text" name="rsv_re_name" value="${reservation_revise_vo2.name }"></td>
			</tr>
			<tr>
				<td>소인</td>
				<td><input type="number" name="rsv_re_child" value="${reservation_revise_vo2.childNum }">명</td>
				<td width="40"></td>
				<td>이메일</td>
				<td><input type="text" name="rsv_re_email" value="${reservation_revise_vo2.email }"></td>
			</tr>
			<tr>
				<td>유아</td>
				<td><input type="number" name="rsv_re_baby" value="${reservation_revise_vo2.babyNum }">명</td>
				<td colspan="3"></td>
			</tr>
			<tr>
				<td>날짜</td>
				<td><input type="number" name="rsv_re_month" value="${reservation_revise_vo2.month }">월</td>
				<td colspan="2" width="200px"><input type="number" name="rsv_re_day" value="${reservation_revise_vo2.day }">일</td>
				<td></td>
			</tr>
			<tr>
				<td>Line</td>
			</tr>
			<tr>
				<td colspan="2"></td>
				<td><input type="submit" value="확인"></td>
			</tr>
		</table>
	</form>
</body>
</html>