<?php
class User{
    public $username;
    function __construct($username)
    {
        $this->username = $username;
    }
    function show(){
        return "username: $this->username\n";
    }
}