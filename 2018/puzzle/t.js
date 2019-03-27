function safeKeyword(keyword) {
	console.log(keyword);
	if (!keyword.match(/(union|select|;|\-\-)/is)) {
		return keyword
	}

	return undefined
}

let username = safeKeyword('12345')
let password = safeKeyword("' unιon sεlect flag from flag where '")

if (username && password) {
	console.log(`SELECT * FROM "users" WHERE "username" = '${username.toUpperCase()}' AND "password" = '${password.toUpperCase()}'`)
} else {
	console.log("error");
}