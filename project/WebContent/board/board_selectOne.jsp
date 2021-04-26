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
		
		td:nth-child(2) {
			float: left;
			width: 300px;
		}
		
		.mid{
			text-align: center;
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
		<h1>공지사항</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px"><b>확인</b></button>
		</form>
	</div>
	<table border="1">
		<tr>
			<td width="70px">제목</td>
			<td>${vo2.title }</td>
		</tr>
		<tr>
			<td>내용</td>
			<td>${vo2.content }</td>
		</tr>
		<tr>
			<td>작성자</td>
			<td>${vo2.writer }</td>
		</tr>
		<tr>
			<td>날짜</td>
			<td>${vo2.wDate }</td>
		</tr>
	</table>
	<c:if test='${sessionScope.login == "mng_Successed"}'>
		<div class="mid">
			<div class="mid1">
				<form action="board_update.do">
					<input type="hidden" name="h_update_title" value="${vo2.title }">
					<input type="hidden" name="h_update_content" value="${vo2.content }">
					<button>수정</button>
				</form>
			</div>
			<div class="mid2">
				<form action="board_delete.do">
					<input type="hidden" name="delete_content" value="${vo2.content }"> 
					<button>삭제</button>
				</form>
			</div>
		</div>
	</c:if>
</body>
</html>