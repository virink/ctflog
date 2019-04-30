FROM ubuntu:18.04

# COPY echohub.php /var/www/html/index.php
# COPY sandbox.php /var/www/html/sandbox.php
COPY ./run.sh /run.sh

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.ustc.edu.cn/g" /etc/apt/sources.list && \
    sed -i '/security.ubuntu.com/d' /etc/apt/sources.list && \
    apt-get update && \
    apt-get -y install software-properties-common
RUN add-apt-repository -y ppa:ondrej/php && \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install tzdata && \
    apt-get -y install vim && \
    apt-get -y install apache2
RUN apt-cache search "php" | grep "php7.3"| awk '{print $1}'| xargs apt-get -y install && \
    # 这个有毒。。。不知道官方证明跑起来的
    # service --status-all | awk '{print $4}'| xargs -i service {} stop && \
    rm /var/www/html/index.html && \
    chmod 755 -R /var/www/html/ && \
    chmod 700 /run.sh

# COPY ./php.ini /etc/php/7.3/apache2/php.ini
# RUN 

CMD ["/run.sh"]
