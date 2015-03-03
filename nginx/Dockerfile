# Version: 0.0.1
FROM sanpingz/centos:base
MAINTAINER Calvin Zhang "sanping.zhang@alcatel-lucent.com"

RUN printf "[nginx]\nname=nginx repo\nbaseurl=http://nginx.org/packages/centos/\$releasever/\$basearch/\ngpgcheck=0\nenabled=1\n" > /etc/yum.repos.d/nginx.repo
RUN yum -y install nginx; yum clean all
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
