<?php
/**
 * Created by PhpStorm.
 * User: phithon
 * Date: 15/10/14
 * Time: 下午7:46
 */

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
    <div id="h">
	<div class="container">
        <h1>Content</h1>
   <div class="row">
			<div class="col-md-8 col-md-offset-2 centered">
            <h3>You can upload picture here</h3>
        <form role="form" action="./upload.php" method="post" enctype="multipart/form-data">
            <input type="file"  name="upfile">
            <button class='btn btn-lg btn-info btn-sub subscribe-submit' type="submit">upload file</button>
        </form>
    </div>
    </div>
    
    </div>
    </div>

<! -- ********** FOOTER ********** -->
<div id="f">
    <div class="container">
		<div class="row">
            <h2 class="mb">Control</h2>
    <a href="./delete.php">
        <button class="btn btn-lg btn-info btn-register" >Delete file</button>
    </a>
    <a href="./rename.php">
        <button class="btn btn-lg btn-info btn-register" >Rename file</button>
    </a>     
		</div><! --/row -->
	</div><! --/container -->
    </div>

<! -- ********** CREDITS ********** -->
<div id="c">
	<div class="container">
		<div class="row">
			<div class="col-md-6 col-md-offset-3 centered">
				<p>Copyright &copy; 2018.WhaleCTF All rights reserved.<a target="_blank" href="http://www.whaledu.com">蓝鲸安全</a></p>
			</div>
		</div>
	</div><! --/container -->
</div><! --/C -->

<!-- Bootstrap core JavaScript
================================================== -->
<!-- Placed at the end of the document so the pages load faster -->
<script src="assets/js/jquery.min.js"></script>
<script src="assets/js/bootstrap.min.js"></script>
<script src="assets/js/retina-1.1.0.js"></script>
<script src="assets/js/jquery.unveilEffects.js"></script>
</body>
</html>
