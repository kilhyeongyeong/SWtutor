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
		
		h1{
			margin : 0 auto;
		}
		
		table{
			margin : 0 auto;
			border: 3px dashed blue;
		}
		
		.bottom{
			margin: 20px;
		}
	</style>
</head>
<body>
	<div class="top">
		<h1>전체이용안내</h1>
		<form action="index.do">
			<button style="height: 35px; width: 55px"><b>확인</b></button>
		</form>
	</div>
	<h3>-이용요금</h3>
	<table border="1">
		<tr>
			<td rowspan="3">이용요금</td>
			<td>대인</td>
			<td>
				<c:if test='${sessionScope.adult == null}'>45,000</c:if>
				<c:if test='${sessionScope.adult != null}'>${sessionScope.adult}</c:if>
			</td>
		</tr>
		<tr>
			<td>소인</td>
			<td>
				<c:if test='${sessionScope.child == null}'>35,000</c:if>
				<c:if test='${sessionScope.child != null}'>${sessionScope.child}</c:if>
			</td>
		</tr>
		<tr>
			<td>유아</td>
			<td>
				<c:if test='${sessionScope.baby == null}'>28,000</c:if>
				<c:if test='${sessionScope.baby != null}'>${sessionScope.baby}</c:if>
			</td>
		</tr>
	</table>
	
	<c:if test='${sessionScope.picture == null}'>
		<img alt="" src="picture.png">
	</c:if>
	<c:if test='${sessionScope.picture != null}'>
		<h3>-가이드 맵</h3>
		<img alt="" src="upload/${sessionScope.picture}">
	</c:if>
</body>
</html>