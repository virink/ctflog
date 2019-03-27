<?php if(!class_exists("View", false)) exit("no direct access allowed");?><div class="register-photo">
    <div class="form-container">
        <form method="post">Hello, <?php echo htmlspecialchars($username, ENT_QUOTES, "UTF-8"); ?>, your email is <?php echo htmlspecialchars($email, ENT_QUOTES, "UTF-8"); ?></form>
    </div>
</div>
