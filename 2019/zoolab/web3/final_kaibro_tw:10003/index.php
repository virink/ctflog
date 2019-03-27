<?php

$sandbox = "/var/www/html/sandbox/" . md5($_SERVER['REMOTE_ADDR'] . "QQ");
@mkdir($sandbox);
@chdir($sandbox);

$path = 'code.txt';

if (isset($_GET['_']) && isset($_GET['f'])) {

	$_ = $_GET['_'];
	$f = $_GET['f'];

	if (preg_match("/h/is", pathinfo($f, PATHINFO_EXTENSION))) {
		die("No h4cker will use h :p");
	}

	$c = "Q____Q" . base64_encode($_);
	$path = 'sandbox/' . md5($_SERVER['REMOTE_ADDR'] . "QQ") . '/' . $f;

	@file_put_contents($f, $c);
// Q____QMQ==
}
?>

<!DOCTYPE HTML>

<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>kaibro</title>
		<link href="style.css" rel="stylesheet" type="text/css" />
		<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js' type='text/javascript'></script>
		<script src='script.js' type='text/javascript'></script>
		<script type='text/javascript'>

			Typer.speed=3;

            Typer.file='<?php echo $path; ?>';

			Typer.init();

		</script>
	</head>
	<body>
		<div id='console'>
			Hello, h4ck3r!
		</div>
	</body>
</html>

