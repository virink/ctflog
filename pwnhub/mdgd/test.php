<pre>
<?php
// require 'conn.php';
$id = $_GET['id'];
if(preg_match("/(sleep|benchmark|outfile|dumpfile|load_file|join)/i", $_GET['id']))
{
    die("you bad bad!");
}
$sql = "select * from article where id='".intval($id)."'";
print_r($sql);
print_r("<hr>");
// $row = mysql_fetch_array($res, MYSQL_ASSOC);
print_r("update view set view_times=view_times+1 where id = '".$id." '");
?>
