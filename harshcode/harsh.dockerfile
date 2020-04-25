from centos
maintainer harsh mangal
env x=web1 
## environment variable or keyword 
run dnf install httpd -y
copy web1 /var/www/html/
expose 80
entrypoint httpd -DFOREGROUND
