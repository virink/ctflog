<?php
require_once('config.php');
require_once('function.php');

$code = $_POST['code'];
$username = $_POST['username'];
$password = $_POST['password'];

$invite_code = time();
$mysqli = new mysqli(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE);
if ($mysqli->connect_errno) {
    exit("shit,".$mysqli->error);
 }
$username = $mysqli->escape_string($_POST['username']);
$password = sha1($_POST['password']);


if($code != $invite_code){
    echo '<div class="alert alert-danger alert-dismissable">
    <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
    Fuck u,man! u need invited code to register!</div>
    <div id="returnVal" style="display:none;">false</div>';
}else{
      $query = "insert into user (username, password) values ('$username', '$password')";
        if ($mysqli->query($query) !== TRUE) {
	    echo '<div class="alert alert-warning"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>Register fail!</div><div id="returnVal" style="display:none;">false</div>';
	    exit('shit,'.$mysqli->error);
          }
	
	$query = "update user set locked=1 where username='$username'";
	if ($mysqli->query($query) === TRUE) {
	    echo '<div class="alert alert-success"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>Register success.</div><div id="returnVal" style="display:none;">true</div>';
	    exit(); 
	}else{
	    echo '<div class="alert alert-warning"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>Register fail!</div><div id="returnVal" style="display:none;">false</div>';	
	}

		      	
}
