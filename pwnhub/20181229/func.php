<?php

function GetPara() {
	global $get, $post, $MysqlLink;
	foreach ($_POST as $k => $v) {
		if (!empty($v) && is_string($v)) {
			$post[$k] = trim(addslashes($v));
		}
	}
	foreach ($_GET as $k => $v) {
		if (!empty($v) && is_string($v)) {
			$get[$k] = trim(addslashes($v));
		}
	}
}
function FilterPara($para) {
	global $tables, $columns;
	$BlackList = "virink";
	if (!preg_match("/{$BlackList}/is", $para)) {
		die("Detect Dangerous Behavior");
	}
	return $para;
}
function Register($username, $password) {
	global $MysqlLink;
	if (strlen($username) > 55) {
		header("Location:index.php?action=register");
		exit();
	}
	$password = FilterPara($password);
	$sql = sprintf("INSERT INTO SU_user (username,password,money) VALUES ('%s',md5('%s'),1000)", $username, $password);
	$query = mysqli_query($MysqlLink, $sql, MYSQLI_USE_RESULT);
	if (!$query) {

		die("Some Errors Happend");
	}
	$sql = sprintf("SELECT * FROM SU_user WHERE username='%s'", $username);
	$query = mysqli_query($MysqlLink, $sql, MYSQLI_USE_RESULT);
	if (!$query) {
		die("Some Errors Happend");
	}
	$result = mysqli_fetch_array($query, MYSQLI_ASSOC);
	if ($username === "admin") {
		$_SESSION["role"] = "admin";
	}
	$_SESSION["username"] = $username;
	$_SESSION["money"] = $result["money"];
	$_SESSION["action"] = "Logined";
	$_SESSION["role"] = "user";
	header("Location:index.php");
}
function getMoney() {
	if (isset($_SESSION["money"])) {
		return $_SESSION["money"];
	} else {

		global $MysqlLink;
		$sql = sprintf("SELECT * FROM SU_user WHERE username='%s'", $_SESSION['username']);
		$query = mysqli_query($MysqlLink, $sql);
		$result = mysqli_fetch_array($query);
		return (int) $result["money"];
	}
}
function Login($username, $password) {
	global $MysqlLink;
	$password = md5(FilterPara($password));
	$username = FilterPara($username);
	$sql = sprintf("SELECT * FROM SU_user WHERE username = '%s' and password='%s'", $username, $password);
	$query = mysqli_query($MysqlLink, $sql, MYSQLI_USE_RESULT);
	if (!$query) {
		die("Some Errors Happend");
	}
	$result = mysqli_fetch_array($query);
	if (count($result) > 0) {
		$_SESSION["id"] = $result["id"];
		$_SESSION["username"] = $result["username"];
	} else {
		die("Login Failed");
	}
	mysqli_free_result($query);
	$sql1 = sprintf("SELECT * FROM SU_user WHERE username='%s'", $_SESSION["username"]);
	$query1 = mysqli_query($MysqlLink, $sql1);
	if (!$query1) {
		var_dump(mysqli_error($MysqlLink));
		die("Get Money Failed");
	}
	$result1 = mysqli_fetch_array($query1);
	if ($username == "admin") {
		$_SESSION['role'] = "admin";
	}
	return (int) $result1["money"];
}
function BuyGoods($money) {
	global $MysqlLink;
	FilterPara($money);

	$sql = sprintf("UPDATE SU_user SET money=money-%d WHERE username='%s';SELECT * FROM SU_user where username=%s", $money, $_SESSION['username'], $_SESSION["username"]);if (mysqli_multi_query($MysqlLink, $sql)) {
		do {
			if ($res = mysqli_store_result($MysqlLink)) {
				// var_dump($res);
				while ($row = mysqli_fetch_row($res)) {
					$money = $row[0];
				}
			}
		} while (@mysqli_next_result($MysqlLink));
	}
	return $money;
}
function GuessFlag($Flag, $ip) {
	global $MysqlLink, $tables;
	$flag = "";
	if (strlen($Flag) > 2) {
		die("Your Flag Too Long");
	}
	$BlackList = "virink";
	if (!preg_match("/{$BlackList}/is", $ip)) {
		die("Detect Dangerous Behavior");
	}
	if (strlen($ip) > 50) {
		die("IP Too Long");
	}
	$sql = sprintf("INSERT INTO ips values(%s);SELECT Flag||%s from Flag;", $ip, $Flag);
	if (mysqli_multi_query($MysqlLink, $sql)) {
		do {
			if ($res = mysqli_store_result($MysqlLink)) {
				while ($row = mysqli_fetch_row($res)) {
					$flag = $row[0];
				}
			}
		} while (@mysqli_next_result($MysqlLink));
	} else {
		if (!$query) {
			die("<br>Unknown Query Error!<br>");
		}
	}
	return $flag;
}
