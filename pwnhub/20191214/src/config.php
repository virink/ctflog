<?php
$con = "mysql:host=localhost;port=3306;dbname=test";
$conn = new PDO($con, 'root', '123456');
$conn->query('set names utf8');

?>
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>key</title>
</head>
<body>
<form action='index.php' method='POST'>
<select name='v'>
  <option value ="anime">anime</option>
  <option value ="character">character</option><br>
</select>
<input type='text' name='i' placeholder='id'>
<input type='submit' value='query'>
</form>
</body>
</html>