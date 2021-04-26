<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Insert title here</title>
	<style>
		body {
			text-align: center;
		}
		
		table {
			margin: 0 auto;
		}
		
		td {
			width: 80px;
		}
		
		div{
			margin: 25px;
		}
		
		form{
			display : inline;
		}
	</style>
</head>
<body>
	<h1>로그인</h1>
	<c:if test='${sessionScope.login != "Successed"}'>
		<h3>${sessionScope.login }</h3>
	</c:if>
	<form action="loginOK.do">
		<table>
			<tr>
				<td>아이디</td>
				<td><input type="text" name="id"></td>
				<td rowspan="2"><input type="submit" value="확인" style="height: 50px; width: 50px"></td>
			</tr>
			<tr>
				<td>비밀번호</td>
				<td><input type="password" name="pw"></td>
			</tr>
		</table>
	</form>
	<div>
		<form action="signup.do">
			<button>회원가입</button>
		</form>
		<form action="index.do">
			<button>메인화면</button>
		</form>
		<form action="idfind.do">
			<button>아이디찾기</button>
		</form>
	</div>
</body>
</html>