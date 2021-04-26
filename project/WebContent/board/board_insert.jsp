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
		table {
			margin: 0 auto;
			text-align: center;
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
		
		tr:nth-child(2) td:nth-child(2){
			text-align: left;
		}
	</style>
</head>
<body>
	<div class="top">
		<h1>공지사항 작성</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px">Home</button>
		</form>
	</div>
	<form action="board_insertOK.do">
		<table border="1">
			<tr>
				<td width="70px">작성자 : </td>
				<td>${sessionScope.userID }</td>
			</tr>
			<tr>
				<td>제목 : </td>
				<td><input type="text" name="insert_title"></td>
			</tr>
			<tr>
				<td>내용 : </td>
				<td><textarea rows="10" cols="50" name="insert_content"></textarea></td>
			</tr>
			<tr>
				<td colspan="2"><input type="submit" value="확인"></td>
			</tr>
		</table>
	</form>
</body>
</html>