<?php
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
  <title>娉ㄥ唽</title>

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
  <form class="form-signin" action="register.php" method="POST">
    <h1 class="h3 mb-3 font-weight-normal">娉ㄥ唽</h1>
    <label for="username" class="sr-only">Username</label>
    <input type="text" name="username" class="form-control" placeholder="Username" required autofocus>
    <label for="password" class="sr-only">Password</label>
    <input type="password" name="password" class="form-control" placeholder="Password" required>
    <button class="btn btn-lg btn-primary btn-block" type="submit">鎻愪氦</button>
    <p class="mt-5 mb-3 text-muted">&copy; 2018-2019</p>
  </form>
</body>
<div class="top" id="toast-container"></div>

<script src="static/js/jquery.min.js"></script>
<script src="static/js/bootstrap.bundle.min.js"></script>
<script src="static/js/toast.js"></script>
</html>


<?php
include "class.php";

if (isset($_POST["username"]) && isset($_POST["password"])) {
	// $u = new User();
	$username = (string) $_POST["username"];
	$password = (string) $_POST["password"];
	if (strlen($username) < 20 && strlen($username) > 2 && strlen($password) > 1) {
		if ($u->add_user($username, $password)) {
			header("Location: login.php?register");
			die();
		} else {
			echo "<script>toast('姝ょ敤鎴峰悕宸茶浣跨敤', 'warning');</script>";
			die();
		}
	}
	echo "<script>toast('璇疯緭鍏ユ湁鏁堢敤鎴峰悕鍜屽瘑鐮�', 'warning');</script>";
}
?>