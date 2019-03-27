<?php
class MainController extends BaseController
{
    function actionIndex()
    {
        print_r($_SESSION);
        if (isset($_SESSION['user_id']) && intval($_SESSION['user_id']) > 0) {
            $user = new User();
            $data = $user->query("SELECT * FROM `{$user->table_name}` WHERE `id` = {$_SESSION['user_id']}");

            $this->username = $data[0]['username'];
            $this->email = $data[0]['email'];
        } else {
            $this->jump('/main/login');
        }
    }

    function actionLogin()
    {
        if ($_POST) {
            $username = arg('username');
            $password = md5(arg('password', ''));

            if (empty($username) || empty($password)) {
                $this->error('Username or password is empty.');
            }

            $user = new User();
            $data = $user->query("SELECT * FROM `{$user->table_name}` WHERE `username` = '{$username}' AND `password` = '{$password}'");
            if (empty($data) or $data[0]['password'] !== $password) {
                $this->error('Username or password is error.');
            }

            $_SESSION['user_id'] = $data[0]['id'];
            $this->jump('/');
        }
    }

    function actionRegister()
    {
        $this->layoyt ="";
        var_dump($_SERVER['HTTP_HOST']);
        if ($_POST) {
            $username = arg('username');
            $password = arg('password', '');

            if (empty($username) || empty($password)) {
                $this->error('Username or password is empty.');
            }

            $email = arg('email');
            if (empty($email)) {
                // 感觉可以注入
                $email = $username . '@' . arg('HTTP_HOST');
                var_dump($email);
            }

            // 过不了emmmmmm
            if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
                $this->error('Email error.');
            }
            // exit;

            $user = new User();
            $data = $user->query("SELECT * FROM `{$user->table_name}` WHERE `username` = '{$username}'");
            if ($data) {
                $this->error('This username is exists.');
            }
            $r = [
                'username' => $username,
                'password' => md5($password),
                'email' => $email
            ];
            $ret = $user->create($r);
            if ($ret) {
                $_SESSION['user_id'] = $user->lastInsertId();
            } else {
                $this->error('Unknown error.');
            }
            print_r($r);
            exit;
        }
    }
}
