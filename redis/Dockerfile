# Version: 0.0.1
FROM centos:7
MAINTAINER Calvin Zhang "sanping.zhang@alcatel-lucent.com"
RUN printf "\nproxy=http://135.2.77.29:8895\nproxy_username=sanpingz\nproxy_password=alu\!1022\n" >> /etc/yum.conf
ENV REFRESHED_AT 2015-02-04
RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install redis; yum clean all
WORKDIR /etc
EXPOSE 6379

CMD ["redis-server", "redis.conf"]
