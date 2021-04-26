<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>이용요금시설</title>
	<style>
		body{
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
	</style>
</head>
<body>
	<div class="top">
		<h1>이용시설 설정</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px">Home</button>
		</form>
	</div>
	<form action="manager_facilityOK.do" method="post" encType="multipart/form-data">
		<p>파일선택</p>
		<input type="file" name="picture"> 
		<input type="submit" value="확인">
	</form>
</body>
</html>