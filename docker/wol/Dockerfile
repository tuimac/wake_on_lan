FROM centos:7

ARG url=https://github.com/tuimac/wake_on_lan.git
ARG pjtname=wakeonlan

EXPOSE 8000
WORKDIR /root

ADD env/vimrc /etc/vimrc
ADD env/bashrc /root/.bashrc
ADD env/login_screen /root/.login_screen
ADD env/centos/vim.sh /etc/profile.d/vim.sh
ADD requirements.txt /root/requirements.txt
ADD entrypoint.sh /root/entrypoint.sh

RUN yum update -y && \
    yum install -y epel-release && \
    yum install -y python-pip python3 vim* iproute curl iputils-ping net-tools unzip git && \
    pip3 install -r requirements.txt && \
    git clone $url && \
    mkdir -p /etc/vim/undo && \
    mkdir -p /etc/vim/backup && \
    django-admin startproject wakeonlan

ADD settings.py /root/$pjtname/$pjtname/settings.py

ENTRYPOINT []
