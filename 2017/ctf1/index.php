
<?php
/**
 * Created by PhpStorm.
 * User: xyz
 * Date: 2017/7/4
 * Time: 10:15
 */

date_default_timezone_set("Asia/Shanghai"); 
header('Content-Type: text/html; charset=utf-8'); 

include('config.php');
include('session.class.php');

$session = new session($mysqli);

if(isset($_POST['name'])){
    $_SESSION['name'] = $_POST['name'];
    $_SESSION['score'] = 10;
    $session->update_session();
}

echo "username:".$_SESSION['name']."\r\nscore:".$_SESSION['score'];

if(!empty($_SESSION['name']) && ($_SESSION['name'] != 'guest') && ($_SESSION['score'] > 0) ){
    // $_SESSION['score'] >= 100 && $_SESSION['name'] >= 'any'
    if($_SESSION['score'] >= 100){
        echo 'flag: ' . $flag;
    }
    if(!empty($_POST['choose'])) {
        $right = random();
        if($_POST['choose'] === $right){
            $_SESSION['score'] += 1;
            echo "good~\r\n";
        }
        else{
            $_SESSION['score'] -= 1;
            echo "error~\r\n";
        }
        $session->update_session();
    }
    else{
        ?>
            choose：
        <?php

    }
}
else{
    ?>

    <Label align="center">plz input your name</Label> <input type="text" name="name" align="center" />
<?php }
?>
