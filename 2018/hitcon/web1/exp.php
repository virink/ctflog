<?php

define("CACHE_DIR", "./test/");

class Test {
	function __construct($v) {
		$this->v = $v;
	}
	function __wakeup() {
		echo "\n__wakeup\n";
		echo "\n$this->v\n";
	}
}

class DymmyResponse {
	function __construct($headers, $body) {
		$this->headers = $headers;
		$this->body = $body;
	}
}

function cache_set($response) {
	if (!file_exists(CACHE_DIR)) {
		mkdir(CACHE_DIR, 0700, true);
	}
	file_put_contents(CACHE_DIR . "body.cache", $response->body);
	file_put_contents(CACHE_DIR . "headers.cache", serialize($response->headers));
}

function cache_get() {
	if (file_exists(CACHE_DIR)) {
		$body = file_get_contents(CACHE_DIR . "/body.cache");
		$headers = file_get_contents(CACHE_DIR . "/headers.cache");

		$body = "<!-- from cache -->\n" . $body;
		$headers = unserialize($headers);
		return new DymmyResponse($headers, $body);
	} else {
		return null;
	}
}

$_headers = [
	"Host" => "127.0.0.11",
	"vvv" => ["a"],
	"test" => [new Test('test')],
];

$headers = [];
foreach ($_headers as $key => $value) {
	if (in_array(strtolower($key), ['host', 'connection', 'expect', 'content-length'])) {
		continue;
	}
	if (count($value) == 0) {
		continue;
	}
	$headers[$key] = $value[0];
}

$response = new DymmyResponse($headers, "test");

// cache_set($response);

$response = cache_get();

var_dump($response);
