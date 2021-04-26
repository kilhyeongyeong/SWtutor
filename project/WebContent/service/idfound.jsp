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
			margin: 0 auto;
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
	<table>
		<tr>
			<td>아이디</td>
			<td>${param.foundid }</td>
		</tr>
		<tr>
			<td>비밀번호</td>
			<td>${param.foundpw }</td>
		</tr>
	</table>
</body>
</html>