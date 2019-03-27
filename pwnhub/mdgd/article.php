<?php
require 'conn.php';
$id = $_GET['id'];
if(preg_match("/(sleep|benchmark|outfile|dumpfile|load_file|join)/i", $_GET['id']))
{
    die("you bad bad!");
}
$sql = "select * from article where id='".intval($id)."'";
print_r("<hr>");
print_r($sql);
print_r("<hr>");
$res = mysql_query($sql);
if(!$res){
    die("404 not found!");
}
$row = mysql_fetch_array($res, MYSQL_ASSOC);
$sql = "update view set view_times=view_times+1 where id = '".$id." '";

print_r($sql);
print_r("<hr>");

mysql_query($sql);
print_r(mysql_error());
print_r("<hr>");

?>
<html>

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title><?=$row['title']?></title>
    <link href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>
    <div>
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <h1><?=$row['title']?></h1>
                    <article><?=$row['content']?></article>
                </div>
            </div>
        </div>
    </div>
</body>

</html>
