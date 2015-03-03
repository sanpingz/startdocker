# Version: 0.0.1
FROM sanpingz/centos:base
MAINTAINER Calvin Zhang "sanping.zhang@alcatel-lucent.com"

RUN yum -y install gcc python-pip python-devel; yum clean all
ENV APP_ROOT /webapp
WORKDIR $APP_ROOT
ADD . $APP_ROOT
RUN pip install -r requirements.txt
# VOLUME ["webapp:$APP_ROOT:ro"]
EXPOSE 5000

CMD ["python", "app.py"]
