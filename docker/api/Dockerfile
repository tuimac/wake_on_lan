FROM centos:7

ARG url=https://github.com/tuimac/wake_on_lan.git
ENV LANG C.UTF-8

EXPOSE 8080
WORKDIR /root

ADD env/vimrc /root/.vimrc
ADD env/bashrc /root/.bashrc
ADD env/login_screen /root/.login_screen
ADD env/centos/vim.sh /etc/profile.d/vim.sh
ADD env/tmux.conf /root/.tmux.conf
ADD requirements.txt /root/requirements.txt

RUN yum update -y && \
    yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum remove -y vi && \
    yum install -y nython36u python36u-libs python36u-devel python36u-pip \
                    vim* iproute curl iputils-ping net-tools unzip git nmap \
                    nmap-ncat.x86_64 tcpdump && \
    pip3 install -r requirements.txt && \
    git clone $url && \
    mkdir -p ~/.vim/backup && \
    mkdir -p ~/.vim/undo && \
    mkdir -p ~/.vim/swap
ADD env/add_remote_repo /root/wake_on_lan/add_remote_repo
