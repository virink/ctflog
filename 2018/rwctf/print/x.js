var url = 'http://ippppppppp:7799/?emmmmmm'
const axios = require('axios');
axios(url)
    .then(r => {
        console.log(r.data);
    })
    .catch((error) => {
        console.log(error);
    });;