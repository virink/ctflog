<?php 


    // $sandbox = "sandbox/" . md5("orange" . $_SERVER["REMOTE_ADDR"]); 
    // @mkdir($sandbox); 
    // @chdir($sandbox); 

    // $data = shell_exec("GET " . escapeshellarg($_GET["url"])); 
    // $info = pathinfo($_GET["filename"]); 
    // $dir  = str_replace(".", "", basename($info["dirname"])); 
    // @mkdir($dir); 
    // @chdir($dir); 
    // @file_put_contents(basename($info["basename"]), $data); 
    // highlight_file(__FILE__); 



    $sandbox = "sandbox/" . md5("orange" . $_SERVER["REMOTE_ADDR"]); 
    // @mkdir($sandbox); 
    // @chdir($sandbox); 

    // print_r(escapeshellarg($_GET["url"]));
    $data = shell_exec("./GET " . escapeshellarg($_GET["url"])); 
    var_dump($data);
    // $info = pathinfo($_GET["filename"]); 
    // $dir  = str_replace(".", "", basename($info["dirname"])); 
    // var_dump($info);
    // var_dump($dir);
    // var_dump(basename($info["basename"]));
    // @mkdir($dir); 
    // @chdir($dir); 
    // @file_put_contents(basename($info["basename"]), $data); 
    // highlight_file(__FILE__); 
