<?php



    // $sandbox = '/www/sandbox/' . md5("orange" . $_SERVER['REMOTE_ADDR']);
    // @mkdir($sandbox);
    // @chdir($sandbox);
    // if (isset($_GET['cmd']) && strlen($_GET['cmd']) <= 5) {
    //     @exec($_GET['cmd']);
    // } else if (isset($_GET['reset'])) {
    //     @exec('/bin/rm -rf ' . $sandbox);
    // }
    // highlight_file(__FILE__);



    if (isset($_GET['cmd']) && strlen($_GET['cmd']) <= 5) {
        var_dump($_GET['cmd']);
        exec($_GET['cmd'],$a);
        var_dump($a);
        // $cmd = urlencode($_GET['cmd']);
        // $url = "http://52.199.204.34/?cmd=$cmd";
        // echo file_get_contents($url);
    } else if (isset($_GET['reset'])) {
        // @exec('/bin/rm -rf ' . $sandbox);
        
    }else{
        var_dump("Too Long");
    }

