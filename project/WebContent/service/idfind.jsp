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
		
		tr:nth-child(3) td:nth-child(2){
			width : 70px;
			color: white;
		}
	</style>
</head>
<body>
	<div class="top">
		<h1>아이디 찾기</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px"><b>확인</b></button>
		</form>
	</div>
	<form action="idfindOK.do">
		<table>
			<tr>
				<td>이름</td>
				<td><input type="text" name="findname"></td>
				<td rowspan="2">${param.msg }</td>
			</tr>
			<tr>
				<td>이메일</td>
				<td><input type="text" name="findemail"></td>
			</tr>
			<tr>
				<td colspan="2"></td>
				<td>NotID</td>
			</tr>
			<tr>
				<td colspan="3"><input type="submit" value="확인"></td>
			</tr>
		</table>
	</form>
</body>
</html>