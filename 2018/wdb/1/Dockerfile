FROM nimmis/alpine-apache-php5

COPY fakebook/ /web/html/

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    apk update && \
    apk add curl php5 php5-mysqli php5-curl mariadb && \
    mkdir /run/openrc && \
    mkdir /run/mysqld && \
    touch /run/openrc/softlevel && \
    /etc/init.d/mariadb setup && \
    touch /run/openrc/softlevel && \
    # sed -i '/AddType application\/x-gzip .gz .tgz/a\    AddType application\/x-httpd-php .php' /usr/local/apache2/conf/httpd.conf && \
    # sed -i '/# LoadModule foo_module/a\LoadModule php5_module libphp5.so' /usr/local/apache2/conf/httpd.conf && \
    # sed -i 's/LoadModule php5_module libphp5.so/LoadModule php5_module modules\/libphp5.so/' /usr/local/apache2/conf/httpd.conf