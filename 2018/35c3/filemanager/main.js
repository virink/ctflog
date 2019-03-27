// 1 引入模块
const net = require('net');
const readline = require('readline');
const pow = require('proof-of-work');
const solver = new pow.Solver();

const ip = "35.246.157.192";
const port = 1;

function proof(num, prefix) {
	console.log(`[+] num: ${num} prefix: ${prefix}`);
	// Buffer.from(prefix, 'hex')
	return solver.solve(num, prefix).toString();
}
// 2 创建套接字和输入输出命令行
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
})

let client = new net.Socket();
client.connect(port, ip);

client.setEncoding('utf8');

client.on('data', (chunk) => {
	console.log(`[+] chunk ${chunk}`);
	if (chunk.indexOf('Please solve a proof-of') > -1) {
		var res = chunk.match(/difficulty (\d+) and prefix (\w+) using/);
		res = proof(res[1], res[2]);
		console.log(`[+] Proof ${res}`);
		res && client.write(res + '\n');
	}
})

client.on('error', (e) => {
	console.log("[+] Error: " + e.message);
	client.close()
})
// 绑定输io流事件,获取输入输出字符
rl.on('line', (mes) => {
	client.write(mes);
})