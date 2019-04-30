<?php
$banner = <<<EOF
<!--/?source=1-->
<pre>
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || |     ______   | || |  ____  ____  | || |     ____     | || |  ____  ____  | || | _____  _____ | || |   ______     | |
| | |_   ___  |  | || |   .' ___  |  | || | |_   ||   _| | || |   .'    `.   | || | |_   ||   _| | || ||_   _||_   _|| || |  |_   _ \    | |
| |   | |_  \_|  | || |  / .'   \_|  | || |   | |__| |   | || |  /  .--.  \  | || |   | |__| |   | || |  | |    | |  | || |    | |_) |   | |
| |   |  _|  _   | || |  | |         | || |   |  __  |   | || |  | |    | |  | || |   |  __  |   | || |  | '    ' |  | || |    |  __'.   | |
| |  _| |___/ |  | || |  \ `.___.'\  | || |  _| |  | |_  | || |  \  `--'  /  | || |  _| |  | |_  | || |   \ `--' /   | || |   _| |__) |  | |
| | |_________|  | || |   `._____.'  | || | |____||____| | || |   `.____.'   | || | |____||____| | || |    `.__.'    | || |  |_______/   | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'

 Welcome to random stack ! Try to execute `/readflag` :P

 </pre>

 <form action="/" method="post">root > <input name="data" placeholder="input some data"></form>
EOF;
echo $banner;
if (isset($_GET['source'])) {
	$file = fopen("index.php", "r");
	$contents = fread($file, filesize("index.php"));
	echo "---------------sourcecode---------------";
	echo base64_encode($contents);
	echo "----------------------------------------";
	fclose($file);
	//Dockerfile here
	echo "RlJPTSB1YnVudHU6MTguMDQKClJVTiBzZWQgLWkgInMvaHR0cDpcL1wvYXJjaGl2ZS51YnVudHUuY29tL2h0dHA6XC9cL21pcnJvcnMudXN0Yy5lZHUuY24vZyIgL2V0Yy9hcHQvc291cmNlcy5saXN0ClJVTiBhcHQtZ2V0IHVwZGF0ZQpSVU4gYXB0LWdldCAteSBpbnN0YWxsIHNvZnR3YXJlLXByb3BlcnRpZXMtY29tbW9uClJVTiBhZGQtYXB0LXJlcG9zaXRvcnkgLXkgcHBhOm9uZHJlai9waHAKUlVOIGFwdC1nZXQgdXBkYXRlClJVTiBhcHQtZ2V0IC15IHVwZ3JhZGUKUlVOIGFwdC1nZXQgLXkgaW5zdGFsbCB0emRhdGEKUlVOIGFwdC1nZXQgLXkgaW5zdGFsbCB2aW0KUlVOIGFwdC1nZXQgLXkgaW5zdGFsbCBhcGFjaGUyClJVTiBhcHQtY2FjaGUgc2VhcmNoICJwaHAiIHwgZ3JlcCAicGhwNy4zInwgYXdrICd7cHJpbnQgJDF9J3wgeGFyZ3MgYXB0LWdldCAteSBpbnN0YWxsClJVTiBzZXJ2aWNlIC0tc3RhdHVzLWFsbCB8IGF3ayAne3ByaW50ICQ0fSd8IHhhcmdzIC1pIHNlcnZpY2Uge30gc3RvcAoKUlVOIHJtIC92YXIvd3d3L2h0bWwvaW5kZXguaHRtbApDT1BZIHJhbmRvbXN0YWNrLnBocCAvdmFyL3d3dy9odG1sL2luZGV4LnBocApDT1BZIHNhbmRib3gucGhwIC92YXIvd3d3L2h0bWwvc2FuZGJveC5waHAKUlVOIGNobW9kIDc1NSAtUiAvdmFyL3d3dy9odG1sLwpDT1BZIGZsYWcgL2ZsYWcKQ09QWSByZWFkZmxhZyAvcmVhZGZsYWcKUlVOIGNobW9kIDU1NSAvcmVhZGZsYWcKUlVOIGNobW9kIHUrcyAvcmVhZGZsYWcKUlVOIGNobW9kIDUwMCAvZmxhZwpDT1BZIC4vcnVuLnNoIC9ydW4uc2gKQ09QWSAuL3BocC5pbmkgL2V0Yy9waHAvNy4zL2FwYWNoZTIvcGhwLmluaQpSVU4gY2htb2QgNzAwIC9ydW4uc2gKCkNNRCBbIi9ydW4uc2giXQ==";
	highlight_file(__FILE__);

}
$disable_functions = ini_get("disable_functions");
$loadext = get_loaded_extensions();
foreach ($loadext as $ext) {
	if (in_array($ext, array("Core", "date", "libxml", "pcre", "zlib", "filter", "hash", "sqlite3", "zip"))) {
		continue;
	} else {
		if (count(get_extension_funcs($ext) ? get_extension_funcs($ext) : array()) >= 1) {
			$dfunc = join(',', get_extension_funcs($ext));
		} else {
			continue;
		}

		$disable_functions = $disable_functions . $dfunc . ",";

	}
}
$func = get_defined_functions()["internal"];
foreach ($func as $f) {
	if (stripos($f, "file") !== false || stripos($f, "open") !== false || stripos($f, "read") !== false || stripos($f, "write") !== false) {
		$disable_functions = $disable_functions . $f . ",";
	}
}
// echo "\r\n";
// print_r($disable_functions);
// echo "\r\n";
ini_set("disable_functions", $disable_functions);
ini_set("open_basedir", "/var/www/html/:/tmp/" . md5($_SERVER['REMOTE_ADDR']) . "/");
