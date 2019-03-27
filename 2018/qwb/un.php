<?php 
error_reporting(0); 
class example 
{ 
    var $var='123'; 

    function __destruct(){ 
        $fb = fopen('./php.php','w'); 
        fwrite($fb, $this->var); 
        fclose($fb); 
    } 
} 

if(empty($_GET['code'])) {
    show_source(__FILE__); 

    $a = new example();
    $a->var = "<?php phpinfo();";
    echo serialize($a); 
} else {
    $class = $_GET['code']; 
    $class_unser = unserialize($class); 
    unset($class_unser);
}

// O:7:"example":1:{s:3:"var";s:16:"<?php phpinfo();";}

?>