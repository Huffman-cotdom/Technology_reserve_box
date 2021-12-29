 

# Docker for centos7安装

官方文档：https://docs.docker.com/engine/install/centos/

## 卸载旧版本

```shell
sudo yum remove docker \
                docker-client \
                docker-client-latest \
                docker-common \
                docker-latest \
                docker-latest-logrotate \
                docker-logrotate \
                docker-engine
```

## 安装

> 安装依赖包

```shell
yum install -y yum-utils
```

> 设置镜像仓库

```shell
 sudo yum-config-manager \
   --add-repo \
   https://download.docker.com/linux/centos/docker-ce.repo
```

> 安装docker

```shell
# 安装最新版的docker
sudo yum install docker-ce docker-ce-cli containerd.io

# 安装指定版本的docker
# 列出并排序存储库中可用的版本
yum list docker-ce --showduplicates | sort -r

# 安装指定版本的docker
sudo yum install docker-ce-<VERSION_STRING> docker-ce-cli-<VERSION_STRING> containerd.io
```

> 启动docker

```shell
sudo systemctl start docker
```

> 检查是否安装成功

```shell
docker version
```

> hello-world

```shell
docker run hello-world

Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
b8dfde127a29: Pull complete
Digest: sha256:308866a43596e83578c7dfa15e27a73011bdd402185a84c5cd7f32a88b501a24
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

说明安装成功！

docker run 流程图

![docker run](Docker%E5%AE%89%E8%A3%85/20201111103606187.png)

> 查看本地镜像

```shell
docker image ls
或者
docker images
```

### docker卸载

```shell
# 1. 卸载依赖
yum remove docker-ce docker-ce-cli containerd.io

# 2. 删除资源
rm -rf /var/lib/docker	# docker的默认工作路径
```

