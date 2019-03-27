
var pp = require("png-img"),
    fs = require("fs"),
    flag = "5L2g5LiN5Lya5Lul5Li66L+Z5piv562U5qGI5ZCnPw==";
function encode(flag, path, keySrc, dest, dest2) {
    for (var used = [], relPosition = [], jpegData = fs.readFileSync(path), ks = fs.readFileSync(keySrc), pngtool = new pp(jpegData), key = new pp(ks), picSize = pngtool.size(), pixelNum = picSize.width * picSize.height, i = (new Buffer(4 * pixelNum), 0); i < flag.length; i++) for (temp = Math.floor(pixelNum * Math.random());;) {
        if (!used.includes(temp)) {
            used.push(temp), relPosition.push(i);
            break
        }
        temp = (temp + 1) % Math.floor(pixelNum)
    }
    for (i = 0; i < picSize.height; i++) for (var j = 0; j < picSize.width; j++) {
        var addrIndex = used.findIndex(function(item) {
            return item === i * picSize.width + j
        }),
            flagIndex = relPosition[addrIndex];
        if (-1 !== addrIndex) {
            var temp = pngtool.get(j, i);
            100 * Math.random() > 50 && !used.includes(j * picSize.width + i) ? (pngtool.set(j, i, {
                r: 255 - temp.r,
                g: 255 - temp.g,
                b: 255 - temp.b,
                a: temp.a
            }), key.set(i, j, {
                r: temp.r,
                g: flagIndex,
                b: flag.charCodeAt(flagIndex)
            })) : (pngtool.set(j, i, {
                r: temp.r,
                g: flagIndex,
                b: 255 - temp.b,
                a: temp.a
            }), key.set(j, i, {
                r: temp.r,
                g: flag.charCodeAt(flagIndex),
                b: temp.b,
                a: temp.a
            }))
        }
    }
    pngtool.save(dest, function(e) {
        console.log(e)
    }), key.save(dest2, function(e) {
        console.log(e)
    })
}
encode(flag, "1.png", "ks.png", "dest.png", "key.png");
//如果你找到了这个文件，恭喜你，就真的成送分题了

// woyaogaoshiqing.gaoshiqing
// encode(flag, "1.png", "ks.png", "dest.png", "key.png");
