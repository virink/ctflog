<?php
/**
 * Created by PhpStorm.
 * User: phithon
 * Date: 15/10/14
 * Time: 下午9:39
 */

require_once "common.inc.php";

if(isset($req['filename'])) {
    $result = $db->query("select * from `file` where `filename`='{$req['filename']}'");
    if ($result->num_rows>0){
        $result = $result->fetch_assoc();
    }

    $filename = UPLOAD_DIR . $result["filename"] . $result["extension"];
    if ($result && file_exists($filename)) {
        $db->query('delete from `file` where `fid`=' . $result["fid"]);
        unlink($filename);
        redirect("/");
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="">
<meta name="author" content="">
<link rel="icon" href="assets/img/favicon.ico">
    <title>file manage</title>
    <base href="./">
    <meta charset="utf-8" />
    <!-- Bootstrap core CSS -->
<link href="assets/css/bootstrap.css" rel="stylesheet">

<!-- Custom styles for this template -->
<link href="assets/css/custom-animations.css" rel="stylesheet">
<link href="assets/css/style.css" rel="stylesheet">


<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
<script src="assets/js/ie10-viewport-bug-workaround.js"></script>

<!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
<!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
<![endif]-->
</head>
<body>
<! -- ********** HEADER ********** -->
<div id="h">
	<div class="container">
<h1>Delete file</h1>
</div>
</div>
<! -- ********** FOOTER ********** -->
<div id="f">
	<div class="container">
		<div class="row">
			<div class="col-md-8 col-md-offset-2 centered">
    <form method="post">
        <p>
            <span>delete filename(exclude extension)：</span>
            <input type="text" class="subscribe-input" name="filename">
        </p>
        <p>
            <input type="submit" class="subscribe-submit" value="delete">
        </p>
    </form>
    </div>
    </div>
    </div>
    </div>
</body>
</html>
