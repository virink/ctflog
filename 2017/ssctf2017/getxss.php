<?php
	error_reporting(0);
	class GetFromXSS
	{
		public function __construct($filename)
		{
			$this->filename = $filename;
		}

		public function Flow()
		{
			/* Method */
	        $flowdata['method'] = $_SERVER['REQUEST_METHOD'];
	        /* Header */
	        $arr = array(
	            'HTTP_HOST',
	            'HTTP_REFERER',
	            'HTTP_USER_AGENT'
	            // 'HTTP_ACCEPT',
	            // 'HTTP_ACCEPT_LANGUAGE',
	            // 'HTTP_ACCEPT_ENCODING',
	            // 'HTTP_CONNECTION'
	            );
	        foreach($arr as $key){
	            $flowdata['Header'][ucwords(strtolower(str_replace("HTTP_", "", $key)))] = $_SERVER[$key];
	        }
	        /* Url */
	        $flowdata['uri'] = $_SERVER['REQUEST_URI'];
	        /* Protocol */
	        $flowdata['protocol'] = $_SERVER['SERVER_PROTOCOL'];
	        /* IP */
	        $flowdata['ip'] = array(
	            'REMOTE_ADDR'=>$_SERVER['REMOTE_ADDR'],
	            'CLIENT_IP'=>$_SERVER['HTTP_CLIENT_IP'],
	            'X_FORWARDED_FOR'=>$_SERVER['HTTP_X_FORWARDED_FOR']
	        );
	        /* Time */
	        $flowdata['time'] = date('Y-m-d H:i:s',$_SERVER['REQUEST_TIME']);
	        /* CONTENT_TYPE */
	        $flowdata['ctype'] = $_SERVER['CONTENT_TYPE'];
		if(isset($_GET)){
			$flowdata['get'] = $_GET;
		}
	        /* PostData */
	        if(isset($_POST) or strtolower($flowdata['Method']) == 'post' ){
	            if($flowdata['ctype'] == 'application/x-www-form-urlencoded'){
	                $flowdata['post'] = $_POST;
	            }else{
	                $flowdata['post'] = file_get_contents('php://input');
	            }
	        }
			$this->WriteFile($this->filename,print_r($flowdata,true),FILE_APPEND);
		}

		public function WriteFile($filename,$content,$FILE_APPEND=FILE_APPEND)
		{
			$content .= "\r\n=================================================================\r\n";
			file_put_contents($filename,$content,$FILE_APPEND);
		}
	}

	$Catchs = new GetFromXSS('log.txt');
	$Catchs->Flow();
?>
