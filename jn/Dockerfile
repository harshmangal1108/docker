from ubuntu
run apt update
RUN apt install python3-pip -y
run pip3 install jupyter
cmd ["jupyter","notebook","--port=8888","--no-browser","--ip=0.0.0.0","--allow-root"]
