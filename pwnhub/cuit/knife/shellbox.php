<?php
include 'db_conn.php';

if(isset($_GET['shell']) && $_GET['shell']!=''){
    $shell = addslashes($_GET['shell']);

    if(preg_match('/script|object|link|on\w*?\s*\\=\s*[\\x00-\\x7f]+?$|srcdoc\s*\\=\s*[\\x00-\\x7f]+?$/i',$shell)){

