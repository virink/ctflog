<?php
/**
 * Created by PhpStorm.
 * User: phithon
 * Date: 15/10/14
 * Time: 下午9:39
 */

require_once "common.inc.php";
define('ROOT',dirname(__FILE__).'/'); 

if(isset($req['oldname']) && isset($req['newname'])) {
    $result = $db->query("select * from `file` where `filename`='{$req['oldname']}'");
    if ($result->num_rows>0) {
        $result = $result->fetch_assoc();
    }else{
        exit("old file doesn't exists!");
    }
    
    if($result) {
        
        $req['newname'] = basename($req['newname']);
        $re = $db->query("update `file` set `filename`='{$req['newname']}', `oldname`='{$result['filename']}' where `fid`={$result['fid']}");
        if(!$re) {
            print_r($db->errorInfo());
            exit;
        }
        $oldname = ROOT.UPLOAD_DIR . $result["filename"].$result["extension"];
        $newname = ROOT.UPLOAD_DIR . $req["newname"].$result["extension"];
        if(file_exists($oldname)) {
            rename($oldname, $newname);
            $url = "/" . $newname;
            echo "Your file is rename, url:
                <a href=\"{$url}\" target='_blank'>{$url}</a><br/>
                <a href=\"/\">go back</a>";
        }
        else{echo $oldname." not exists.";}
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="">
<meta name="author" content="">
<link rel="icon" href="assets/img/favicon.ico">
    <title>file manage</title>
    <base href="./">
    <meta charset="utf-8" />
    <!-- Bootstrap core CSS -->
<link href="assets/css/bootstrap.css" rel="stylesheet">

<!-- Custom styles for this template -->
<link href="assets/css/custom-animations.css" rel="stylesheet">
<link href="assets/css/style.css" rel="stylesheet">


<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
<script src="assets/js/ie10-viewport-bug-workaround.js"></script>

<!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
<!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
<![endif]-->
</head>
<body>
<! -- ********** HEADER ********** -->
<div id="h">
	<div class="container">
<h1>Rename file</h1>
<h3>You can Rename What you had uploaded file<h3>
</div>
</div>
<! -- ********** FOOTER ********** -->
<div id="f">
	<div class="container">
		<div class="row">
			<div class="col-md-8 col-md-offset-2 centered">
<form method="post">
    <p>
        <h3>old filename(exclude extension)：</h3>
        <input type="text" class="subscribe-input" name="oldname">
    </p>
    <p>
        <h3>new filename(exclude extension)：</h3>
        <input type="text" class="subscribe-input" name="newname">
    </p>
    <p>
        <input type="submit" class="subscribe-submit" value="rename">
    </p>
</form>
</div>

		</div><! --/row -->
	</div><! --/container -->
</div><! --/F -->

</body>
</html>
