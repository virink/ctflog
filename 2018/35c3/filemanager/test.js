const a = "Please solve a proof-of work with difficulty 22 and prefix 3b99 using https://www.npmjs.com/package/proof-of-work";

var r = a.match(/difficulty (\d+) and prefix (\w+) using/);

console.log(r[1]);