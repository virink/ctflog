FROM ubuntu:18.04


COPY flag /flag

RUN apt-get update
RUN apt-get -y install tzdata
RUN apt-get -y install php
RUN apt-get -y install apache2
RUN apt-get -y install libapache2-mod-php

RUN rm /var/www/html/index.html
# RUN mv /flag `cat /flag`

RUN sed -i "s/;session.upload_progress.enabled = On/session.upload_progress.enabled = Off/g" /etc/php/7.2/apache2/php.ini
RUN sed -i "s/;session.upload_progress.enabled = On/session.upload_progress.enabled = Off/g" /etc/php/7.2/cli/php.ini

RUN echo 'PD9waHAKICAoJF89QCRfR0VUWydvcmFuZ2UnXSkgJiYgQHN1YnN0cihmaWxlKCRfKVswXSwwLDYpID09PSAnQDw/cGhwJyA/IGluY2x1ZGUoJF8pIDogaGlnaGxpZ2h0X2ZpbGUoX19GSUxFX18pOw==' | base64 -d > /var/www/html/index.php
RUN chmod -R 755 /var/www/html

CMD service apache2 start & tail -F /var/log/apache2/access.log

