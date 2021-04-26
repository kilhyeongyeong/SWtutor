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
	</style>
</head>
<body>
	<div class="top">
		<h1>비밀번호를 입력하세요</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px">Home</button>
		</form>
	</div>
	<form action="mem_passwordOK.do">
		<p><b>비밀번호 : <input type="password" name="passwordCK"></b>
			<input type="submit" value="확인">
		</p>
		<h3>${param.msg }</h3>
	</form>
</body>
</html>