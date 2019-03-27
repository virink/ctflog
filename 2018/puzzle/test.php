<?php

$domain = ";%s'";
// preg_replace_callback('', 'return phpinfo();');
$command = sprintf("echo %s", escapeshellarg($domain));

print_r($command);

echo "\r\n";

$output = shell_exec($command);
$output = htmlspecialchars($output, ENT_HTML401 | ENT_QUOTES);

print_r($output);