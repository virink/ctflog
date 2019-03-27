<?php
if (!isset($lemon_flag)) {
    die('No!');
}
?>
<h1> Admin Login </h1>
<form action="" method="POST">
<input type="text" name="name" value="">
<input type="text" name="pass" value="">
<input type="submit" value="submit">
</form>

<?php
if (isset($_POST['name']) && isset($_POST['pass'])) {
    if ($_POST['name'] === 'admin' && $_POST['pass'] === 'sctf2018_h656cDBkU2') {
        $_SESSION['admin'] = 1;
    } else {
        die('<script>alert(/Login Error!/)</script>');
    }
}

//admin view

if (@$_SESSION['admin'] === 1) {
    ?>
<form action="./?f=upload_sctf2018_C9f7y48M75.php" method="POST" enctype="multipart/form-data">
    <input type="file" value="" name="upload">
    <input type="submit" value="submit" name="submit">
</form>

<?php
}
?>
