<?php
session_start();

include_once "config.php";
// include_once "func.php";

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
	$BlackList = "[\w']+";
	if (!preg_match("/{$BlackList}/is", $para)) {
		die("FilterPara Detect Dangerous Behavior");
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
	var_dump($password);
	$sql = sprintf("SELECT * FROM SU_user WHERE username = '%s' and password='%s'", $username, $password);
	var_dump($sql);
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
	$BlackList = ".*";
	if (!preg_match("/{$BlackList}/is", $ip)) {
		die("Flag Detect Dangerous Behavior");
	}
	if (strlen($ip) > 50) {
		die("IP Too Long");
	}
	$sql = sprintf("INSERT INTO ips values(%s);SELECT Flag||%s from Flag;", $ip, $Flag);
	var_dump($sql);
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

// end

$post = array();
$get = array();
global $MysqlLink;
global $tables;
global $columns;
GetPara();
$MysqlLink = mysqli_connect("127.0.0.1", $datauser, $datapass);
if (!$MysqlLink) {
	die("Mysql Connect Error!");
}
$selectDB = mysqli_select_db($MysqlLink, $dataName);
if (!$selectDB) {
	die("Choose Database Error!");
}

$tables = "users|Flag|ips";
$columns = "id|username|password|flag|money|ip";

switch (@$_GET['action']) {
case "register":
	if (!empty($post['username']) && !empty($post["password"])) {
		if (strlen($post["username"]) > 70) {
			die("Username Too Long");
		}
		Register($post['username'], $post['password']);
	} else {
		echo <<<EOF
            <form action="index.php?action=register" method="post" >
                <input type="text" name="username">
                <input type="password" name="password">
                <input type="submit" value="Register">
            </form>
EOF;
	}
	die();
case "login":
	if (!empty($post["username"]) && !empty($post["password"])) {
		$money = Login($_REQUEST["username"], $post["password"]);
		$_SESSION["money"] = $money;
		$_SESSION["action"] = "Logined";
	}
	break;
case "logout":
	unset($_SESSION["username"]);
	unset($_SESSION["action"]);
	unset($_SESSION["role"]);
	unset($_SESSION["money"]);
	mysqli_close($MysqlLink);
	header("Location:index.php");
case "buy":
	if (!empty($get["money"])) {
		$money = $get["money"];
		$_SESSION["money"] = BuyGoods($money);
		header("Location:index.php");
	} else {
		exit("No money");
	}
default:
	break;
}
if (!isset($_SESSION["action"])) {
	$_SESSION["action"] = "NO_Logined";
}

if ($_SESSION["action"] !== "Logined") {
	echo <<<EOF
<form action="index.php?action=login" method="post" >
    <input type="text" name="username">
    <input type="password" name="password">
    <input type="submit" value="Login">
</form>
<a href="index.php?action=register">Register</a>
<!-- code.txt -->
<!-- username:admin   -->
EOF;
	exit();
} elseif ($_SESSION["action"] === "Logined") {
	echo "You have money:" . getMoney() . "<br>";
	echo "<a href='index.php?action=buy&money=20'>Apple Pen:20</a><br>";
	echo "<a href='index.php?action=buy&money=20'>Milk:20</a><br>";
	echo "<a href='index.php?action=buy&money=200'>House:200</a><br>";
	echo "<a href='index.php?action=logout'>Logout</a>";
	if ($_SESSION["role"] == "admin") {
		if (isset($get["Flag"])) {
			$Flag = $get["Flag"];
			$guessResult = GuessFlag($Flag, $_SERVER["HTTP_X_FORWARDED_FOR"]);
			print_r($guessResult);
		}
	}
}

?>










