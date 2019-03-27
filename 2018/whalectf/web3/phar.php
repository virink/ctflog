<?php
/**
 * Created by yunke.
 * User: yunke
 * Date: 2017/2/10
 * Time: 9:36
 */
 
//产生一个yunke.phar文件
$phar = new Phar('chamd5.phar', 0, 'chamd5.phar');
// 添加project里面的所有文件到yunke.phar归档文件
$phar->buildFromDirectory(dirname(__FILE__) . '/x');
//设置执行时的入口文件，第一个用于命令行，第二个用于浏览器访问，这里都设置为index.php
$phar->setDefaultStub('x.php', 'x.php');
