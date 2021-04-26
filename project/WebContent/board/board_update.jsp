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
		.top{
			margin-bottom: 50px;
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
	</style>
</head>
<body>
	<div class="top">
		<h1>공지사항 수정</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px">Home</button>
		</form>
	</div>
	<form action="board_updateOK.do">
		<table border="1">
			<tr>
				<td>작성자 </td>
				<td>${sessionScope.userID }</td>
			</tr>
			<tr>
				<td>제목</td>
				<td><input type="text" name="update_title" value=${h_update_title }></td>
			</tr>
			<tr>
				<td>내용 </td>
				<td><input type="text" name="update_content" value="${h_update_content }"></td>
			</tr>
			<tr>
				<td colspan="2"><input type="submit" value="확인"></td>
			</tr>
		</table>
	</form>
</body>
</html>