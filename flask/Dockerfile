# Version: 0.0.1
FROM centos:7
MAINTAINER Calvin Zhang "sanping.zhang@alcatel-lucent.com"

RUN printf "\nproxy=http://135.2.77.29:8895\nproxy_username=sanpingz\nproxy_password=alu\!1022\n" >> /etc/yum.conf
ENV REFRESHED_AT 2015-02-04
RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install python-pip; yum clean all

ENV APP_ROOT /webapp
WORKDIR $APP_ROOT
ADD . $APP_ROOT
ENV http_proxy http://sanpingz:alu\!1022@135.2.77.29:8895
ENV https_proxy https://sanpingz:alu\!1022@135.2.77.29:8895
RUN pip install -r requirements.txt
#VOLUME ["webapp:$APP_ROOT:ro"]
EXPOSE 5000

CMD ["python", "app.py"]
