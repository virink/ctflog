<?php
session_start();
require_once('header.php');
check_user();

if(isset($_REQUEST['url'])){
    $url = $_REQUEST['url'];
}else{
    $url = 'http://'.$_COOKIE['HOST'].'/cat.jpg';
    header("Location: /market.php?url=".$url);
    die();
}
if(is_cat($url)){
    ;
}else{
    die("Do you want to cheat me?<br>");
}
$image = "data:image/jpg;base64," . base64_encode(@curl($url));
?>
<div class="col-md-8 col-md-offset-2">
    <div class="page-header"><h2><p>Animal Market/Deep Web</p></h2></div>
    <div>
        <p><h4>Welcome to deep web, <?php $username=isset($_SESSION['username'])?$_SESSION['username']:'guest';echo $username;?></h4></p>
    </div>
    <div class="well">
	<p>Do you want to buy a cat?</p>
	<br><br><br>
	<img style="width:50%" src="<?php echo $image; ?>" />
    </div>
</div>

<?php
require_once('footer.php');
?>
