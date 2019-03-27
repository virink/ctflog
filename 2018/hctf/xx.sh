#!/bin/sh
# for i in `seq 10000000 100000000`
function hashmd5(){
	arg="$1"
	echo "Running... $arg"
	i=10000000
	while True;
	# for i in `seq 10000000 100000000`
	do
		printf "\r%s" $i
		res=$(md5 -s "$i" | grep -o -E '[a-f0-9]{32}')
		if [[ "$arg" = "${res:0:${#arg}}" ]];then
		    printf '\r%s\n' $i 
		    break
		fi
		let i=i+1
	done
}

hashmd5 950f