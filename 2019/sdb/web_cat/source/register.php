<?php
include("header.php");
?>

<script src="js/signup.js"></script>
<div class="col-md-8 col-md-offset-2">
    <div class="col-md-4 col-md-offset-4">
        <form action="checkregister.php" method="post" id="signin">
            <div class="form-group">
                <label for="username">Username</label>
                <input autofocus="autofocus" class="form-control" id="username" name="username" type="text" />
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input autocomplete="off" class="form-control" id="password" name="password" type="password" />
            </div>
            <div class="form-group">
                <label for="code">Code</label>
                <input autofocus="autofocus" class="form-control" id="code" name="code" type="text" />
            </div>
            <div><input class="btn btn-primary" id="submit" name="submit" type="submit" value="Register"></div>
        </form>
        <div id="message"></div>
    </div>
</div>

<?php
    require_once('footer.php')
?>



