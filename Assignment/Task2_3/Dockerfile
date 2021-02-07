FROM centos
RUN yum install nginx -y
EXPOSE 80
ADD ./index.html /usr/share/nginx/html/
ADD ./webpage /etc/nginx/sites-available/webpage
RUN mkdir  /etc/nginx/sites-enabled/
RUN ln -s /etc/nginx/sites-available/webpage /etc/nginx/sites-enabled/webpage
WORKDIR /etc/nginx
CMD [ "nginx" ]



