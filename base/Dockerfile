# Version: 0.0.1
FROM centos:7
MAINTAINER Calvin Zhang "sanping.zhang@alcatel-lucent.com"

ENV PROXY_HOST 135.2.77.29:8895
ENV PROXY_USERNAME sanpingz
ENV PROXY_PASSWORD alu\!1022
ENV http_proxy http://${PROXY_USERNAME}:${PROXY_PASSWORD}@${PROXY_HOST}
ENV https_proxy https://${PROXY_USERNAME}:${PROXY_PASSWORD}@${PROXY_HOST}
RUN printf "\nproxy=http://${PROXY_HOST}\nproxy_username=${PROXY_USERNAME}\nproxy_password=${PROXY_PASSWORD}\n" >> /etc/yum.conf

ENV REFRESHED_AT 2015-03-03
RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all

CMD ["bash"]
