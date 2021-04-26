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
		
		.mid{
			text-align: center;
			margin: 25px;
		}
		
		.mid1{
			display: inline-block;
		}
		
		.mid2{
			display: inline-block;
		}
		
		.bottom{
			text-align: center;
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
	
	<div class="mid">
		<div class="mid1">
			<form action="board_searchList.do">
				<select name="searchKey">
					<option value="writer">작성자</option>
					<option value="title">제목</option>
					<option value="content">내용</option>
				</select> 
				<input type="text" name="searchWord"> 
				<input type="submit" value="검색">
			</form>
		</div>
		<div class="mid2">
			<form action="member_notice.do">
				<button>초기화</button>
			</form>
		</div>
	</div>

	<table border="1">
		<tr>
			<td>작성자</td>
			<td>제목</td>
			<td>내용</td>
			<td>날짜</td>
		</tr>
		<c:forEach var="vo" items="${boardlist}"> <%--boardController->board_selectAll.do --%>
			<tr>
				<td>${vo.writer}</td>
				<td>${vo.title}</td>
				<td width="200"><a href="board_selectOne.do?selectOne_content=${vo.content}">${vo.content}</a></td>
				<td>${vo.wDate}</td>
			</tr>
		</c:forEach>
	</table>
	
	<div class="bottom">
		<c:if test='${sessionScope.login == "mng_Successed"}'>
			<form action="board_notice_insert.do">
				<button>입력</button>
			</form>
		</c:if>
	</div>
</body>
</html>