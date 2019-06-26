<?php
include("header.php");
?>

<script src="js/signin.js"></script>
<div class="col-md-8 col-md-offset-2">
    <div class="col-md-4 col-md-offset-4">
        <form action="checklogin.php" method="post" id="signin">
            <div class="form-group">
                <label for="username">Username</label>
                <input autofocus="autofocus" class="form-control" id="username" name="username" type="text" />
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input autocomplete="off" class="form-control" id="password" name="password" type="password" />
            </div>
            <div><input class="btn btn-primary" id="submit" name="submit" type="submit" value="Login"></div>
        </form>
        <div id="message"></div>
    </div>
</div>

<?php
    require_once('footer.php')
?>



