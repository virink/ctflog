<?php
error_reporting(0);
header("ACCESS-CONTROL-ALLOW-ORIGIN: *");
class PhpFlowLog
{
    public function __construct()
    {
        $this->flowdata = array();
        $this->redirect = false;
        $this->logfiles = "/tmp/flow.log";
        $this->Flow();
    }

    public function Flow()
    {
        /* Method */
        $this->flowdata['method'] = $_SERVER['REQUEST_METHOD'];
        /* Header */
        $arr = array(
            'HTTP_HOST',
            'HTTP_REFERER',
            'HTTP_USER_AGENT'
        );
        foreach($arr as $key){
            $this->flowdata['header'][ucwords(strtolower(str_replace("HTTP_", "", $key)))] = $_SERVER[$key];
        }
        /* Url */
        $this->flowdata['uri'] = $_SERVER['REQUEST_URI'];
        /* Protocol */
        $this->flowdata['protocol'] = $_SERVER['SERVER_PROTOCOL'];
        /* IP */
        $this->flowdata['ip'] = array(
            'REMOTE_ADDR'=>$_SERVER['REMOTE_ADDR'],
            'CLIENT_IP'=>$_SERVER['HTTP_CLIENT_IP'],
            'X_FORWARDED_FOR'=>$_SERVER['HTTP_X_FORWARDED_FOR']
        );
        /* Time */
        $this->flowdata['time'] = date('Y-m-d H:i:s',$_SERVER['REQUEST_TIME']);
        /* CONTENT_TYPE */
        $this->flowdata['ctype'] = $_SERVER['CONTENT_TYPE'];
        /* GetData ??? */
        $this->flowdata['get'] = json_encode($_GET);
        /* PostData */
        if(isset($_POST) or strtolower($this->flowdata['Method']) == 'post' ){
            if($this->flowdata['ctype'] == 'application/x-www-form-urlencoded'){
                $this->flowdata['post'] = json_encode($_POST);
            }else{
                $this->flowdata['post'] = file_get_contents('php://input');
            }
        }
        $this->Send("null");
    }

    public function Send($keyword)
    {
        $data = $this->flowdata;
        file_put_contents("/tmp/html.log", $_GET["v"],FILE_APPEND);
        file_put_contents($this->logfiles,"\r\n".$keyword."\r\n".print_r($data,true)."\r\n=====================================\r\n",FILE_APPEND);
        return 0;
    }
}

new PhpFlowLog();

