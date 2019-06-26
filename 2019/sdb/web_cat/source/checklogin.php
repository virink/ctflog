<?php
require_once('config.php');
require_once('function.php');



if (isset($_POST['username']) && isset($_POST['password'])) {
  if ($_POST['username']==='' || $_POST['password']==='')
  {
    
    echo '<div class="alert alert-danger alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>This is in deep web, u know it?!</div><div id="returnVal" style="display:none;">false</div>';    
    exit();
  }

  $mysqli = new mysqli(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE);
  
  if ($mysqli->connect_errno) {
    exit("shit,".$mysqli->error);
  }

  $username = $mysqli->escape_string($_POST['username']);
  $password = sha1($_POST['password']);

  $query = "select * from user where username='$username' and password='$password'";
  $result = $mysqli->query($query);
  if ($result->num_rows) {
    $row = $result->fetch_array();
    $_SESSION['locked'] = $row['locked'];
    if($_SESSION['locked']){
	echo '<div class="alert alert-danger alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>You need to active your account first!</div><div id="returnVal" style="display:none;">false</div>';
	exit();
    }
    $_SESSION['username'] = $row['username'];
     echo '<div class="alert alert-success"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>Welcome, bad guy!</div><div id="returnVal" style="display:none;">true</div>';
  } else {
    echo '<div class="alert alert-danger alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>This is in deep web, do not play small trick!</div><div id="returnVal" style="display:none;">false</div>';
    exit();
  }

}

?>
