<?php
require 'conn.php';
$sql = "select * from article";
$res = mysql_query($sql);
if(!$res){
    print_r(mysql_error());
    die("404 not found!");
}
?>
<html>

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Article List</title>
    <link href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>
    <div>
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <h1>Article List</h1>
                    <ul>
                    <?php while($row = mysql_fetch_array($res, MYSQL_ASSOC)): ?>
                    
                        <li><a href="article.php?id=<?=$row['id']?>"><?=$row['title']?></a></li>
                    <?php endwhile; ?>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</body>

</html>
