<?php

namespace App\Controller;
use Cake\Http\Client;

error_reporting(E_ALL);

class DymmyResponse {
	function __construct($headers, $body) {
		$this->headers = $headers;
		$this->body = $body;
	}
}

class PagesController extends AppController {

	private function httpclient($method, $url, $headers, $data) {
		$options = [
			'headers' => $headers,
			'timeout' => 10,
		];

		$http = new Client();
		return $http->$method($url, $data, $options);
	}

	private function back() {
		return $this->render('pages');
	}

	private function _cache_dir($key) {
		$ip = $this->request->getEnv('REMOTE_ADDR');
		$index = sprintf('mycache/%s/%s/', $ip, $key);
		return CACHE . $index;
	}

	private function cache_set($key, $response) {
		$cache_dir = $this->_cache_dir($key);
		if (!file_exists($cache_dir)) {
			mkdir($cache_dir, 0700, true);
			// file_put_contents($cache_dir . "body.cache", $response->body);
			// file_put_contents($cache_dir . "headers.cache", serialize($response->headers));
		}
		file_put_contents($cache_dir . "body.cache", $response->body);
		file_put_contents($cache_dir . "headers.cache", serialize($response->headers));
	}

	private function cache_get($key) {
		$cache_dir = $this->_cache_dir($key);
		if (file_exists($cache_dir)) {
			$body = file_get_contents($cache_dir . "/body.cache");
			$headers = file_get_contents($cache_dir . "/headers.cache");

			$body = "<!-- from cache -->\n" . $body;
			$headers = unserialize($headers);
			return new DymmyResponse($headers, $body);
		} else {
			return null;
		}
	}

	public function display(...$path) {
		$request = $this->request;
		$data = $request->getQuery('data');
		$url = $request->getQuery('url');
		if (strlen($url) == 0) {
			return $this->back();
		}

		$scheme = strtolower(parse_url($url, PHP_URL_SCHEME));
		if (strlen($scheme) == 0 || !in_array($scheme, ['http', 'https'])) {
			return $this->back();
		}

		$method = strtolower($request->getMethod());
		if (!in_array($method, ['get', 'post', 'put', 'delete', 'patch'])) {
			return $this->back();
		}

		$headers = [];
		// var_dump($request->getHeaders());
		foreach ($request->getHeaders() as $key => $value) {
			if (in_array(strtolower($key), ['host', 'connection', 'expect', 'content-length'])) {
				continue;
			}
			if (count($value) == 0) {
				continue;
			}
			$headers[$key] = $value[0];
		}
		// var_dump($url);
		$key = md5($url);
		if ($method == 'get') {
			$response = $this->cache_get($key);
			// var_dump($response->headers);
			if (!$response) {
				$response = $this->httpclient($method, $url, $headers, null);
				$this->cache_set($key, $response);
			}
			$response = $this->httpclient($method, $url, $headers, null);
			$this->cache_set($key, $response);
		} else {
			$response = $this->httpclient($method, $url, $headers, $data);
		}

		foreach ($response->headers as $key => $value) {
			if (strtolower($key) == 'content-type') {
				$this->response->type(array('type' => $value));
				$this->response->type('type');
				continue;
			}
			// var_dump($key);
			// var_dump($value);
			$this->response->withHeader($key, $value);
		}

		$this->response->body($response->body);
		var_dump($response->headers);
		return $this->response;
	}
}
