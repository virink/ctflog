<?php

if(isset($_GET['u'])){
    header("Location: ".$_GET['u'].".php");
    $log = date("Y-m-d H:i:s")." : ".$_SERVER[REMOTE_ADDR]." redirect to: ".$_GET['u'].".php\n\r";
    file_put_contents("log.txt",$log,FILE_APPEND);
}else{
    header("Location: index.php");
}

