#!/bin/sh

docker run -p 8080:8080 -p 80:443 -v `pwd`:/var/www/html  -ti icq_web5 /bin/bash 
