FROM centos:7

ARG url=https://github.com/tuimac/wakeonlan.git
ARG pjtname=wakeonlan

EXPOSE 8000
WORKDIR /root

ADD env/vimrc /etc/vimrc
ADD env/bashrc /root/.bashrc
ADD env/login_screen /root/.login_screen
ADD env/centos/vim.sh /etc/profile.d/vim.sh
ADD requirements.txt /root/requirements.txt

RUN yum update -y && \
    yum install -y epel-release && \
    yum install -y python-pip python3 vim* iproute curl iputils-ping net-tools unzip git tree && \
    pip3 install -r /root/requirements.txt && \
    git clone $url && \
    mkdir -p /etc/vim/undo && \
    mkdir -p /etc/vim/backup
    #django-admin startproject $pjtname

#WORKDIR /root/$pjtname/$pjtname/$pjtname
#COPY settings.py settings.py
ADD add_remote_repo /root/$pjtname/add_remote_repo
WORKDIR /root/$pjtname/$pjtname
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
