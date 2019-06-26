<?php
require_once("function.php");
session_start();
session_unset();
session_destroy();
check_user();

?>
