<?php
/**
 * I used SourceGuardian to protect my ``verify`` function.
 * It's so easy and you even don't need to decompile the extension...
 *
 * If you can't run this file, download loaders from https://www.sourceguardian.com/loaders.html
 */
// error_reporting(E_ALL);

// namespace V;

// function a($q, $y, $z, $p, $e, $k) {
// 	var_dump($q);
// 	var_dump($y);
// 	var_dump($z);
// 	var_dump($p);
// 	var_dump($e);
// 	var_dump($k);
// }

// verify("\xffffffa0\"\x01\x02\x01","7F26B84B450EEB27AAQAAAAXAAAABIgAAACABAAAAAAAAAD/Nqcgl3yEZoZqJ6tA2gb1VGz0Gw0ihBUXoypKI7VeAPFvj4TXHx1et2CblX+8PEIKOjxTPzBaLf4TcfqtojGEIudFcWJ0Crz2T6Hqv1R+RNcoq5mJxIJbOFLuCqgqZ2VEjLDICbOerELxzxS3E7nWdtQZgdhKiEpor+OByrwZ+zMYpf3NwNPobDYAAACICgAAhbO5R3y6q6FCRSwssqUM356iWkygGq7GusQFurYV3nWNOAa7JX0StE7lzaeejqUI7p9NfGcUlvZKEOdEa+QCFTvx1UFiO/zju3nVPWRRFNb77hJvlvGx+iDFqxau2C7zcLNZat1idG7I5aKwRK8HDhYhqgwyRpjgYdTPwVvF1/TcEWoK0DdApjHjqzFiptilvMcsxNPGPpBXChLjCiGirdaSVcIIAqwl5Xo8YZxhtlAZIWnl9DI2MSJ6p+Sqfcv4Zc2Nbo2RtIsR21T/gxJrAPY2fmfFHYLr4bVCPjatvcN0WqCa5FVkWWqCwM0sAWmksOTFk+3QwAKHlH2QCkT7xFXhN48abQIJQS1lZCCFiJW3UYg72hipM+CGeI+jlX6+aDYb0tQRHXt2NDgvIoSsgMjef2HUi8OI7fc9tm4w0IOp+yY/6UcekrhV3yWbQp4hOBzQgaDeUTmIny0TlI79CwzhmrQnSxdoHnKHxm0FoWC7MJ4+pPmjDg/2weZLeHehlvNSve4EZ7D6HpJnw9wZvm5BGjZoGYxdw9qMM029u+X0B4wWXICAtT3horYI97vGq+e4C372IfNTFmkEmipa6oYzgYTwzYj9FcJUVbMwd9SteyI1G5JSdz4O12B/jn8TGt+yukdS5z7dUeWQGmbVg0j6IuY5H4uk9hd59fvoVEGSHoH6J9YCFqhnqUBpxMRUihf2sjfmUfY5K8wzzAqgaYPFyxeBFzwoniIpWbnZ+Ruop0u0KOPxITXi2eg8LbY15g1j7aWjQuYIhfj","'","X ");
// unpack("V*");
// str_repeat("",strlen($flag) mod 4);
// unpack("V*", $flag);

require __DIR__ . '/protected.php';

// print_r(a("aaa", "asda", "123asda", "asda", "asda", "asda"));

if (verify('FLAGFLAGFLAGFLAGFLAGFLAGFLAGFLAGFLAGFLAG')) {
	echo 'Correct!';
} else {
	echo 'Wrong!';
}