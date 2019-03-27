<?php

error_reporting(E_ALL);

class UserInfo
{
    public $name = "";
    public $age = 0;
    public $blog = "";

    public function __construct($name, $age, $blog)
    {
        $this->name = $name;
        $this->age = (int)$age;
        $this->blog = $blog;
    }

    function get($url)
    {
        $ch = curl_init();

        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        $output = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        if($httpCode == 404) {
            return 404;
        }
        curl_close($ch);

        return $output;
    }

    public function getBlogContents()
    {
        return $this->get($this->blog);
    }

    public function isValidBlog ()
    {
        $blog = $this->blog;
        return preg_match("/^(((http(s?))\:\/\/)?)([0-9a-zA-Z\-]+\.)+[a-zA-Z]{2,6}(\:[0-9]+)?(\/\S*)?$/i", $blog);
    }

}

$con = mysql_connect("localhost","root","123456");
if (!$con)
{
    die('Could not connect: ' . mysql_error());
}

mysql_select_db("test", $con);

$no = $_GET['no'];

if(strpos($no,"union select") !== False){
    die("Hacker");
}

$result = mysql_query("SELECT * FROM users where no={$no}") or print_r(mysql_error());

while($row = mysql_fetch_array($result))
{
    var_dump($row);
    var_dump($row['username']);
    var_dump($row['data']);
    $user = unserialize($row['data']);
    if($user){
        var_dump($user->age);
        var_dump($user->blog);
        $res = $user->getBlogContents();
        if($res){
            var_dump($res);
            $res = base64_encode($res);
            print_r("<iframe src='data:text/html;base64,{$res}'></iframe>");
        }else{
            var_dump("no contents");
        }
    }
}

mysql_close($con);

?>

