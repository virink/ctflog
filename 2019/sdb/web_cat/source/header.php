<?php
require_once('config.php');
require_once('function.php');
?>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>CAT LOST</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <script src="js/jquery-2.2.4.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
</head>

<body>
<div class="container-fluid">
    <nav class="navbar navbar-inverse" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapse" data-toggle="collapse" data-target=".navbar-collapse">
                    <a class="navbar-brand" href="/">Profile</a>
                </button>
            </div>
            <div class="collapse navbar-collapse">
                <ul class="nav navbar-nav">
                    <li class=""> <a href="index.php">INDEX</a> </li>
                    <li class=""> <a href="market.php">CAT MARKET</a> </li>
                </ul>
                <?php
                if(isset($_SESSION['username'])){
                    echo '
            <ul class="nav navbar-nav navbar-right">
                <li><a href="logout.php">Logout</a></li>
            </ul>';
                }
                else{
                    echo '
            <ul class="nav navbar-nav navbar-right">
                <li><a href="login.php">Login</a></li>
                <li><a href="register.php">Register</a></li>
            </ul>';
                }
                ?>
            </div>
        </div>
    </nav>
