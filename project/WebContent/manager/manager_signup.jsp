<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>회원가입</title>
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
		
		.mid{
			margin : 35px;
		}
		
		td:nth-child(1) {
			text-align: left;
			width: 100px;
		}
		
		tr:nth-child(9) {
			color: white;
		}
	</style>
</head>
<body>
	<div class="top">
		<h1>회원가입</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px">Home</button>
		</form>
	</div>
	<div class="mid">
		<form action="manager_idCheck.do" method="post">
			아이디 중복체크 : <input type="text" name="mngid_check"> 
			<input type="submit" value="확인"> ${param.msg}
		</form>
	</div>
	<form action="manager_insert.do" method="post" enctype="multipart/form-data">
		<table>
			<tr>
				<td>프로필사진  </td>
				<td><input type="file" name="picture"></td>
			</tr>
			<tr>
				<td>아이디 </td>
				<td><input type="text" name="mngid" value=${param.id }></td>
			</tr>
			<tr>
				<td>비밀번호  </td>
				<td><input type="text" name="mngpw"></td>
			</tr>
			<tr>
				<td>이름  </td>
				<td><input type="text" name="mngname"></td>
			</tr>
			<tr>
				<td>핸드폰번호  </td>
				<td><input type="text" name="mngphone"></td>
			</tr>
			<tr>
				<td>이메일  </td>
				<td><input type="text" name="mngemail"></td>
			</tr>
			<tr>
				<td>은행명  </td>
				<td><input type="text" name="mngbank"></td>
			</tr>
			<tr>
				<td>계좌  </td>
				<td><input type="text" name="mngaccount"></td>
			</tr>
			<tr>
				<td>Line</td>
			</tr>
		</table>
		<input type="submit" value="확인">
	</form>
</body>
</html>