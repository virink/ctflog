<?php
namespace interesting;
function sha1($var) {
	$class = new \ReflectionClass('interesting\FlagSDK');
	$mg = $class->getMethod('getHash');
	$mg->setAccessible(true);
	$sdk = $class->newInstance();
	return $mg->invoke($sdk);
}
$sdk = new FlagSDK();
echo $sdk->verify(1);