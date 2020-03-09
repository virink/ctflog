<?php
error_reporting(E_ALL);

$filename = isset($argv[1]) ? $argv[1] : 'Upload.php';
if (!file_exists($filename)) {
	echo "$filename is not exists";
	exit;
}
// $filename = 'Upload.php';
$fdata = file_get_contents($filename);
// rename($filename, "$filename.bak");

$fdata = str_replace("<?php", "", $fdata);
$fdata = str_replace("?>", "", $fdata);
$fdata = str_replace("GLOBALS", "G", $fdata);

// unserialize
preg_match_all('/\$G.*?=unserialize.*?;/', $fdata, $matches);
$global_var_code = $matches[0][0];
eval($global_var_code);
$global_var_name = array_keys($G)[0];
unset($G);
$fdata = str_replace($global_var_name, "gvn", $fdata);
$global_var_code = str_replace($global_var_name, "gvn", $global_var_code);
eval($global_var_code);
// print_r($G);

$fdata = str_replace($global_var_code, "", $fdata);

preg_match_all('/\$([\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)/', $fdata, $matches);
$random_var_name = $matches[1];
$random_var_name = array_unique($random_var_name);
$i = 1;
foreach ($random_var_name as $var_name) {
	$fdata = str_replace($var_name, "var_name_$i", $fdata);
	$i += 1;
}

$funcs = get_defined_functions()['internal'];
$G['gvn'][0] = 'ggvn';
for ($i = 0; $i < 2000; $i++) {
	if (isset($G['gvn'][$i])) {
		$tmp = $G['gvn'][$i];
		if (is_numeric($tmp)) {
		} else if (in_array($tmp, $funcs)) {
		} else {
			$tmp = "'$tmp'";
		}
		$fdata = str_replace("\$G['gvn'][$i]", $tmp, $fdata);
	}
}

preg_match_all('/\$G.*?=unserialize.*?;/', $fdata, $matches);
$gglobal_var_code = $matches[0][0];
eval($gglobal_var_code);

$fdata = str_replace($gglobal_var_code, "", $fdata);
// print_r($fdata);

// $G['ggvn'][37+(88-67)]
preg_match_all('/\$G\[\'ggvn\'\]\[([\d\+\-\(\)]+)\]/', $fdata, $matches);
// echo $var_name_1;
$random_ggvn_vars = $matches[0];
foreach ($random_ggvn_vars as $value) {
	eval('$tmp=' . $value . ';');
	// if (is_numeric($tmp)) {
	// } else if (in_array($tmp, $funcs)) {
	// } else {
	// 	$tmp = "'$tmp'";
	// }
	if (!in_array($tmp, $funcs)) {
		$tmp = "'$tmp'";
	}
	$fdata = str_replace($value, $tmp, $fdata);
}
// print_r($fdata);

// chr(59+(85-23)
preg_match_all('/chr\([\'\d\+\-\(\)]+\)/', $fdata, $matches);
$random_ggvn_vars = $matches[0];
foreach ($random_ggvn_vars as $value) {
	eval('$tmp=' . $value . ';');
	// if (!is_numeric($tmp)) {
	//  $tmp = "'$tmp'";
	// }
	$tmp = "'$tmp'";
	$fdata = str_replace($value, $tmp, $fdata);
}

// print_r($fdata);
// ('xx'.'yy')
$fdata = str_replace(".''", "", $fdata);
for ($j = 0; $j < 30; $j++) {
	preg_match_all('/\(\'([\w\'\(\)\>\<\!\/\?]+?)\'\.\'([\?\/\w\'\(\)\>\<\!]+?)\'\)/', $fdata, $matches);
	for ($i = 0; $i < count($matches[0]); $i++) {
		$tmp = $matches[1][$i] . $matches[2][$i];
		$fdata = str_replace($matches[0][$i], "'$tmp'", $fdata);
	}
	preg_match_all('/\(\'([\/\w\'\(\)\>\<\!\?]+?)\'\)/', $fdata, $matches);
	for ($i = 0; $i < count($matches[0]); $i++) {
		$tmp = $matches[1][$i];
		$fdata = str_replace($matches[0][$i], "'$tmp'", $fdata);
	}
}

// fix str_rot13'xxx'
preg_match_all('/str_rot13\'([\w\>\<\?\/]+?)\'/', $fdata, $matches);
for ($i = 0; $i < count($matches[0]); $i++) {
	$tmp = str_rot13($matches[1][$i]);
	if (in_array($tmp, $funcs)) {
		$fdata = str_replace($matches[0][$i], "$tmp", $fdata);
	} else {
		$fdata = str_replace($matches[0][$i], "'$tmp'", $fdata);
	}
}
//  str_rot13('xxx')
preg_match_all('/str_rot13\(\'([\w\>\<\?\/]+?)\'\)/', $fdata, $matches);
for ($i = 0; $i < count($matches[0]); $i++) {
	$tmp = str_rot13($matches[1][$i]);
	if (in_array($tmp, $funcs)) {
		$fdata = str_replace($matches[0][$i], "$tmp", $fdata);
	} else {
		$fdata = str_replace($matches[0][$i], "'$tmp'", $fdata);
	}
}
// print_r($fdata);
file_put_contents($filename . 'new.php', "<?php \n" . $fdata);