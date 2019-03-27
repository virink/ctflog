<?php
error_reporting(E_ALL);
session_start();
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>web3</title>
    <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
    <script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
    <nav class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
        <div class="navbar-header">
            <a class="navbar-brand" href="index.php">首页</a>
        </div>
            <ul class="nav navbar-nav navbra-toggle">
                <li class="active"><a href="file.php?file=">查看文件</a></li>
                <li><a href="upload_file.php">上传文件</a></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
                <li><a href="index.php"><span class="glyphicon glyphicon-user"></span><?php echo $_SERVER['REMOTE_ADDR']; ?></a></li>
            </ul>
        </div>
    </nav>
</body>
</html>
<!--flag is in f1ag.php-->