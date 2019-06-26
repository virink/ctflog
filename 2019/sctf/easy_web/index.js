const koa = require("koa");
const AWS = require("aws-sdk");
const bodyparser = require('koa-bodyparser');
const Router = require('koa-router');
const async = require("async");
const archiver = require('archiver');
const fs = require("fs");
const cp = require("child_process");
const mount = require("koa-mount");
const cfg = {
    "Bucket":"static.l0ca1.xyz",
    "host":"static.l0ca1.xyz",
}

function getRandomStr(len) {
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    for (var i = 0; i < len; i++)
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    return text;
};
function zip(archive, output, nodeModules) {
    const field_name = getRandomStr(20);
    fs.mkdirSync(`/tmp/${field_name}`);
    archive.pipe(output);
    return new Promise((res, rej) => {
        async.mapLimit(nodeModules, 10, (i, c) => {
            process.chdir(`/tmp/${field_name}`);
            console.log(`npm --userconfig='/tmp' --cache='/tmp' install ${i}`);
            cp.exec(`npm --userconfig='/tmp' --cache='/tmp' install ${i}`, (error, stdout, stderr) => {
                if (error) {
                    c(null, error);
                } else {
                    c(null, stdout);
                }
            });
        }, (error, results) => {
            archive.directory(`/tmp/${field_name}/`, false);
            archive.finalize();
        });
        output.on('close', function () {
            cp.exec(`rm -rf /tmp/${field_name}`, () => {
                res("");
            });
        });
        archive.on("error", (e) => {
            cp.exec(`rm -rf /tmp/${field_name}`, () => {
                rej(e);
            });
        });
    });
}

const s3Parme = {
    // accessKeyId:"xxxxxxxxxxxxxxxx",
    // secretAccessKey:"xxxxxxxxxxxxxxxxxxx",
}
var s3 = new AWS.S3(s3Parme);
const app = new koa();
const router = new Router();
app.use(bodyparser());
app.use(mount('/static',require('koa-static')(require('path').join(__dirname,'./static'))));
router.get("/", async (ctx) => {
    return new Promise((resolve, reject) => {
        fs.readFile(require('path').join(__dirname, './static/index.html'), (err, data) => {
            if (err) {
                ctx.throw("系统发生错误,请重试");
                return;
            };
            ctx.type = 'text/html';
            ctx.body = data.toString();
            resolve();
        });
    });
})
.post("/login",async(ctx)=>{
    if(!ctx.request.body.email || !ctx.request.body.password){
        ctx.throw(400,"参数错误");
        return;
    }
    ctx.body = {isUser:false,message:"用户名或密码错误"};
    return;
})
.post("/upload", async (ctx) => {
    const parme = ctx.request.body;
    const nodeModules = parme.npm;
    const key = parme.key;
    if(typeof key == "undefined" || key!="abcdefghiklmn123"){
        ctx.throw(403,"请求失败");
        return;
    }
    if (typeof nodeModules == "undefined") {
        ctx.throw(400, "JSON 格式错误");
        return;
    }
    const zipFileName = `${getRandomStr(20)}.zip`;
    var output = fs.createWriteStream(`/tmp/${zipFileName}`, { flags: "w" });
    var archive = archiver('zip', {
        zlib: { level: 9 },
    });
    try {
        await zip(archive, output, nodeModules);
    } catch (e) {
        console.log(e);
        ctx.throw(400,"系统发生错误,请重试");
        return;
    }
    const zipBuffer = fs.readFileSync(`/tmp/${zipFileName}`);
    const data = await s3.upload({ Bucket: cfg.Bucket, Key: `node_modules/${zipFileName}`, Body: zipBuffer ,ACL:"public-read"}).promise().catch(e=>{
        console.log(e);
        ctx.throw(400,"系统发生错误,请重试");
        return;
    });
    ctx.body = {url:`http://${cfg.host}/node_modules/${zipFileName}`};
    cp.execSync(`rm -f /tmp/${zipFileName}`);
    return;
})
app.use(router.routes());

if (process.env && process.env.AWS_REGION) {
    require("dns").setServers(['8.8.8.8','8.8.4.4']);
    const serverless = require('serverless-http');
    module.exports.handler = serverless(app, {
        binary: ['image/*', 'image/png', 'image/jpeg']
    });
}else{
    app.listen(3000,()=>{
        console.log(`listening 3000......`);
    });
}