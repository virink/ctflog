#!/usr/bin/env sh

function b64d(){
    echo "$1" | base64 -d
}

xx="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm/+"

for i in `seq ${#xx}`
do   
    echo ${str:$i-1;1} `b64d "eyJ0eXAiOiJKV1QiLCJhbGciOiJzaGEyNTYiLCJraWQiOiIyNTEzIn0KeyJuYW1lIjoidmRtaW4ifQK${str:$i-1;1}"`
done 