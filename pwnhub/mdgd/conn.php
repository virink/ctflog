<?php
error_reporting(E_ALL & ~E_DEPRECATED);
$con = mysql_pconnect("localhost",'root','');
if(!$con)
{
   die('error'.mysql_error());
}
mysql_select_db('test');
