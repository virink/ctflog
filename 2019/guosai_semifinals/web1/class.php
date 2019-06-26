<?php
error_reporting(E_ALL);

class Test {
	public function __construct() {
		file_put_contents("php://stdout", "__construct");
		$a = file_get_contents($this->filename);
		file_put_contents("php://stdout", $a);
	}
	public function __destruct() {
		file_put_contents("php://stdout", "__destruct");
		$a = file_get_contents($this->filename);
		file_put_contents("php://stdout", $a);
	}
}

// $t = new Test();

// $dbaddr = "localhost";
// $dbuser = "root";
// $dbpass = "";
// $dbname = "dropbox";
// $db = new mysqli($dbaddr, $dbuser, $dbpass, $dbname);

// class User {
// 	public $db;

// 	public function __construct() {
// 		global $db;
// 		$this->db = $db;
// 	}

// 	public function userExist($username) {
// 		$stmt = $this->db->prepare("SELECT `username` FROM `users` WHERE `username` = ? LIMIT 1;");
// 		$stmt->bind_param("s", $username);
// 		$stmt->execute();
// 		$stmt->store_result();
// 		$count = $stmt->num_rows;
// 		if ($count === 0) {
// 			return false;
// 		}
// 		return true;
// 	}

// 	public function addUser($username, $password) {
// 		if ($this->userExist($username)) {
// 			return false;
// 		}
// 		$password = sha1($password . "SiAchGHmFx");
// 		$stmt = $this->db->prepare("INSERT INTO `users` (`id`, `username`, `password`) VALUES (NULL, ?, ?);");
// 		$stmt->bind_param("ss", $username, $password);
// 		$stmt->execute();
// 		return true;
// 	}

// 	public function verifyUser($username, $password) {
// 		if (!$this->userExist($username)) {
// 			return false;
// 		}
// 		$password = sha1($password . "SiAchGHmFx");
// 		$stmt = $this->db->prepare("SELECT `password` FROM `users` WHERE `username` = ?;");
// 		$stmt->bind_param("s", $username);
// 		$stmt->execute();
// 		$stmt->bind_result($expect);
// 		$stmt->fetch();
// 		if (isset($expect) && $expect === $password) {
// 			return true;
// 		}
// 		return false;
// 	}

// 	public function __destruct() {
// 		$this->db->close();
// 	}
// }

class FileList {
	private $files;
	private $results;
	private $funcs;

	public function __construct($path) {
		$this->files = array();
		$this->results = array();
		$this->funcs = array();
		$filenames = scandir($path);

		$key = array_search(".", $filenames);
		unset($filenames[$key]);
		$key = array_search("..", $filenames);
		unset($filenames[$key]);

		foreach ($filenames as $filename) {
			$file = new File();
			$file->open($path . $filename);
			array_push($this->files, $file);
			$this->results[$file->name()] = array();
		}
	}

	public function __call($func, $args) {
		file_put_contents("php://stdout", "FileList_" . "__call");
		array_push($this->funcs, $func);
		foreach ($this->files as $file) {
			$this->results[$file->name()][$func] = $file->$func();
		}
	}

	public function __destruct() {
		file_put_contents("php://stdout", "FileList_" . "__destruct");
		$table = '<div id="container" class="container"><div class="table-responsive"><table id="table" class="table table-bordered table-hover sm-font">';
		$table .= '<thead><tr>';
		foreach ($this->funcs as $func) {
			$table .= '<th scope="col" class="text-center">' . htmlentities($func) . '</th>';
		}
		$table .= '<th scope="col" class="text-center">Opt</th>';
		$table .= '</thead><tbody>';
		foreach ($this->results as $filename => $result) {
			$table .= '<tr>';
			foreach ($result as $func => $value) {
				$table .= '<td class="text-center">' . htmlentities($value) . '</td>';
			}
			$table .= '<td class="text-center" filename="' . htmlentities($filename) . '"><a href="download.php?filename=' . htmlentities($filename) . '" class="download">download</a> / <a href="delete.php?filename=' . htmlentities($filename) . '" class="delete">delete</a></td>';
			$table .= '</tr>';
		}
		echo $table;
	}
}

class File {
	public $filename;

	public function open($filename) {
		$this->filename = $filename;
		if (file_exists($filename) && !is_dir($filename)) {
			return true;
		} else {
			return false;
		}
	}

	public function name() {
		return basename($this->filename);
	}

	public function size() {
		$size = filesize($this->filename);
		$units = array(' B', ' KB', ' MB', ' GB', ' TB');
		for ($i = 0; $size >= 1024 && $i < 4; $i++) {
			$size /= 1024;
		}

		return round($size, 2) . $units[$i];
	}

	public function detele() {
		unlink($this->filename);
	}

	public function close() {
		return file_get_contents($this->filename);
	}
}
?>