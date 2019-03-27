<?php
/**
 * Created by PhpStorm.
 * User: xyz
 * Date: 2017/7/4
 * Time: 9:29
 */
class session
{

    function __construct(&$db, $session_id='', $session_table = 'session', $session_name='SESSID')
    {
        $this->dbConn  = $db;
        $this->session_name = $session_name;
        $this->session_table = $session_table;
        $this->_ip = $this->real_ip();

        output("\$this->_ip=".$this->_ip);
        output("\$session_id={$session_id}");
        output("\$_COOKIE[\$this->session_name]=".$_COOKIE[$this->session_name]);

        if ($session_id == '' && !empty($_COOKIE[$this->session_name]))
        {
            $this->session_id = $_COOKIE[$this->session_name];
        }
        else
        {
            $this->session_id = $session_id;
            // 
        }

        if ($this->session_id)
        {
            $tmp_session_id = substr($this->session_id, 0, 32);
            output("\$this->gen_session_key($tmp_session_id)=".$this->gen_session_key($tmp_session_id));
            output("substr($this->session_id, 32)=".substr($this->session_id, 32));
            if ($this->gen_session_key($tmp_session_id) == substr($this->session_id, 32)) // d07c9c1e
            {
                $this->session_id = $tmp_session_id;
            }
            else
            {
                $this->session_id = '';
            }
        }
        if ($this->session_id)
        {
            $this->load_session();
        }
        else
        {
            $this->gen_session_id();
            setcookie($this->session_name, $this->session_id . $this->gen_session_key($this->session_id));
        }

    }

    function insert_session()
    {
        $sql = 'INSERT INTO ' . $this->session_table . " (session_id, ip, data) VALUES ('" . $this->session_id ."', '". $this->_ip ."', 'a:2:{s:4:\"name\";s:5:\"guest\";s:5:\"score\";s:1:\"0\";}')";
        $res = $this->dbConn->query($sql);
        // printf("Errormessage: %s\n", $this->dbConn->error);
        return $res;
    }

    function load_session()
    {
        $sql = 'SELECT data FROM ' . $this->session_table . " WHERE session_id = '" . $this->session_id . "' and ip = '" . $this->_ip . "'";
        output($sql);
        $res = $this->dbConn->query($sql);
        // printf("Errormessage: %s\n", $this->dbConn->error);
        $session = $res->fetch_array();
        if (empty($session))
        {
            $this->insert_session();
        }
        else
        {
            output("\$session=");
            output($session);
            $GLOBALS['_SESSION']  = unserialize($session['data']);
        }
    }

    function update_session()
    {
        $data = serialize($GLOBALS['_SESSION']);

        $data = addslashes($data);
        $sql='UPDATE ' . $this->session_table . " SET ip = '" . $this->_ip . "',  data = '$data' WHERE session_id = '" . $this->session_id . "'";
        output($sql);
        $res = $this->dbConn->query($sql);
        printf("Errormessage: %s\n", $this->dbConn->error);
        return $res;
    }

    function gen_session_id()
    {
        $this->session_id = md5(uniqid(mt_rand(), true));

        return $this->insert_session();
    }

    function gen_session_key($session_id)
    {
        static $ip = '';

        if ($ip == '')
        {
            $ip = substr($this->_ip, 0, strrpos($this->_ip, '.'));
        }

        $res= sprintf('%08x', crc32($ip . $session_id));
        // output("gen_session_key=".$res);
        return $res;
    }

    // XFF
    function real_ip()
    {
        static $realip = NULL;

        if ($realip !== NULL)
        {
            return $realip;
        }

        if (isset($_SERVER))
        {
            if (isset($_SERVER['HTTP_X_FORWARDED_FOR']))
            {
                $realip = $_SERVER['HTTP_X_FORWARDED_FOR'];
            }
            elseif (isset($_SERVER['HTTP_CLIENT_IP']))
            {
                $realip = $_SERVER['HTTP_CLIENT_IP'];
            }
            else
            {
                if (isset($_SERVER['REMOTE_ADDR']))
                {
                    $realip = $_SERVER['REMOTE_ADDR'];
                }
                else
                {
                    $realip = '0.0.0.0';
                }
            }
        }
        else
        {
            $realip = '0.0.0.0';
        }
        return $realip;
    }

}
