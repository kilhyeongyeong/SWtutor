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
		
		.top{
			margin-bottom: 50px;
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
		
		tr:nth-child(4) {
			color: white;
		}
	</style>
</head>
<body>
	<div class="top">
		<h1>이용요금 설정</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px"><b>확인</b></button>
		</form>
	</div>
	<form action="manager_costOK.do">
		<table>
			<tr>
				<td>대인 :</td>
				<td>
					<c:if test='${sessionScope.adult == null}'>
						<input type="text" name="adult" value="45000">원
					</c:if>
					<c:if test='${sessionScope.adult != null}'>
						<input type="text" name="adult" value="${sessionScope.adult}">원
					</c:if>
				</td>
			</tr>
			<tr>
				<td>소인 :</td>
				<td>
					<c:if test='${sessionScope.child == null}'>
						<input type="text" name="child" value="35000">원
					</c:if>
					<c:if test='${sessionScope.child != null}'>
						<input type="text" name="child" value="${sessionScope.child}">원
					</c:if>
				</td>
			</tr>
			<tr>
				<td>유아 :</td>
				<td>
					<c:if test='${sessionScope.baby == null}'>
						<input type="text" name="baby" value="28000">원
					</c:if>
					<c:if test='${sessionScope.adult != null}'>
						<input type="text" name="baby" value="${sessionScope.baby}">원
					</c:if>
				</td>
			</tr>
			<tr>
				<td>Line</td>
			</tr>
			<tr>
				<td></td>
				<td><input type="submit" value="확인"></td>
			</tr>
		</table>
	</form>
</body>
</html>