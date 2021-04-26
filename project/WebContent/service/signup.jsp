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
		
		.mid{
			text-align: center;
			margin-top: 150px;
		}
		
		.mid1{
			display: inline-block;
			margin: 25px;
		}
		
		.mid2{
			display: inline-block;
			margin: 25px;
		}
	</style>
</head>
<body>
	<div class="top">
		<h1>회원가입</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px"><b>확인</b></button>
		</form>
	</div>
	<div class="mid">
		<div class="mid1">
			<form action="member_signup.do">
				<button style="height: 35px; width: 100px">개인</button>
			</form>
		</div>
		<div class="mid2">
			<form action="manager_signup.do">
				<button style="height: 35px; width: 100px">법인</button>
			</form>
		</div>
	</div>
</body>
</html>