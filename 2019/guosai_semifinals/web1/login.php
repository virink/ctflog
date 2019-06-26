<?php
error_reporting(E_ALL);
session_start();
if (isset($_SESSION['login'])) {
	header("Location: index.php");
	die();
}
?>

<!doctype html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <title>鐧诲綍</title>

  <!-- Bootstrap core CSS -->
  <link href="static/css/bootstrap.min.css" rel="stylesheet">


  <style>
    .bd-placeholder-img {
      font-size: 1.125rem;
      text-anchor: middle;
    }

    @media (min-width: 768px) {
      .bd-placeholder-img-lg {
        font-size: 3.5rem;
      }
    }
  </style>
  <!-- Custom styles for this template -->
  <link href="static/css/std.css" rel="stylesheet">
</head>

<body class="text-center">
  <form class="form-signin" action="login.php" method="POST">
    <h1 class="h3 mb-3 font-weight-normal">鐧诲綍</h1>
    <label for="username" class="sr-only">Username</label>
    <input type="text" name="username" class="form-control" placeholder="Username" required autofocus>
    <label for="password" class="sr-only">Password</label>
    <input type="password" name="password" class="form-control" placeholder="Password" required>
    <button class="btn btn-lg btn-primary btn-block" type="submit">鎻愪氦</button>
    <p class="mt-5 text-muted">杩樻病鏈夎处鍙�? <a href="register.php">娉ㄥ唽</a></p>
    <p class="text-muted">&copy; 2018-2019</p>
  </form>
  <div class="top" id="toast-container"></div>
</body>

<script src="static/js/jquery.min.js"></script>
<script src="static/js/bootstrap.bundle.min.js"></script>
<script src="static/js/toast.js"></script>
</html>


<?php
include "class.php";

if (isset($_GET['register'])) {
	echo "<script>toast('娉ㄥ唽鎴愬姛', 'info');</script>";
}

if (isset($_POST["username"]) && isset($_POST["password"])) {
	// $u = new User();
	$username = (string) $_POST["username"];
	$password = (string) $_POST["password"];
	if (strlen($username) < 20) {
		$_SESSION['login'] = true;
		$_SESSION['username'] = htmlentities($username);
		$sandbox = "uploads/" . sha1($_SESSION['username'] . "sftUahRiTz") . "/";
		if (!is_dir($sandbox)) {
			mkdir($sandbox);
		}
		$_SESSION['sandbox'] = $sandbox;
		header("Location: index.php");
		die();
	}
	echo "<script>toast('璐﹀彿鎴栧瘑鐮侀敊璇�', 'warning');</script>";
}
?>