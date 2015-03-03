# Version: 0.0.1
FROM sanpingz/centos:base
MAINTAINER Calvin Zhang "sanping.zhang@alcatel-lucent.com"

RUN yum -y install redis; yum clean all
WORKDIR /etc
EXPOSE 6379

CMD ["redis-server", "redis.conf"]
