<?php
session_start();
require_once('header.php');
if(isset($_GET['lang'])){
    $lang = $_GET['lang'];
}else{
    $lang = 'en';
}

if(strstr($lang,'en')!==false){
    require_once('en.php');
    $lang='cn';
}else{
    require_once('cn.php');
    $lang='en';
}

?>
<div class="col-md-8 col-md-offset-2">
    <div class="page-header"><h2><p><?php echo $title;?></p></h2></div>
    <div>
        <p><h4>Hello, <?php $username=isset($_SESSION['username'])?$_SESSION['username']:'guest';echo $username;?></h4></p>
    </div>
    <div class="well">
	    <p><?php echo $content_1;?></p>
	    <p><?php echo $content_2;?></p>
	    <p><?php echo $content_3;?></p><br><br><br><br><br><br><br><?php echo "<a href='redirect.php?u=index.php?lang=$lang'>change lang</a>"; ?>

    </div>
</div>

<?php
require_once('footer.php');
?>
