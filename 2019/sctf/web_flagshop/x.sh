#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2019/06/23, 12:54

function fuck(){
    local name=$1
    # curl -s -k -q \
    curl -vv \
    --cookie "auth=eyJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiI0OTVhZWMwYy1iYjVkLTRlMDYtYWVhZS1kZTExN2QxMzgyZjMiLCJqa2wiOjEwMDAwMH0.54OUE6a_Ame4cRTMXXOoP1BWB2kDPl5LmrouldeZwSw" \
    "http://47.110.15.101/api/info" \
    --output -
}

fuck