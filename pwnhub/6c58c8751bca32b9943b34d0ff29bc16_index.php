<!DOCTYPE html>
<html>
<head>
    <title>你在里面发现了什么? </title>
</head>
<body>

<form action="index.php" method="post" enctype="multipart/form-data">
<input name="upload" type="file" /><br/>
<input type="submit" value="上传" />
<p>注意：只支持tar!!</p>
<?php
//设置编码为UTF-8，以避免中文乱码
header('Content-Type:text/html;charset=utf-8');
# 没文件上传就退出

$file = $_FILES['upload'];
# 文件名不可预测性
$salt = base64_encode('8gss7sd09129ajcjai2283u821hcsass').mt_rand(80,65535);
$name = (md5(md5($file['name'] . $salt) . $salt).'.tar');
if (!isset($_FILES['upload']) or !is_uploaded_file($file['tmp_name'])) {
    exit;
}
# 移动文件到相应的文件夹
if (move_uploaded_file($file['tmp_name'], "/tmp/pwnhub/$name")) {
    $cfgName = trim(shell_exec('python /usr/local/nginx/html/6c58c8751bca32b9943b34d0ff29bc16/untar.py /tmp/pwnhub/'.$name));
    $cfgName = trim($cfgName);
    echo "<p>更新配置成功，内容如下</p>";
    // echo '<br/>';
    echo '<textarea cols="30" rows="15">';
    readfile("/tmp/pwnhub/$cfgName");
    echo '</textarea>';
} else {
    echo("Failed!");
}


?>
</form>
</body>
</html>
