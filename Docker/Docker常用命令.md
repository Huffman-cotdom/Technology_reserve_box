# Docker常用命令

![docker](Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI1MzEwNjY5,size_16,color_FFFFFF,t_70.png)

```tex
  attach      Attach local standard input, output, and error streams to a running container
  #当前shell下 attach连接指定运行的镜像
  build       Build an image from a Dockerfile # 通过Dockerfile定制镜像
  commit      Create a new image from a container's changes #提交当前容器为新的镜像
  cp          Copy files/folders between a container and the local filesystem #拷贝文件
  create      Create a new container #创建一个新的容器
  diff        Inspect changes to files or directories on a container's filesystem #查看docker容器的变化
  events      Get real time events from the server # 从服务获取容器实时时间
  exec        Run a command in a running container # 在运行中的容器上运行命令
  export      Export a container's filesystem as a tar archive #导出容器文件系统作为一个tar归档文件[对应import]
  history     Show the history of an image # 展示一个镜像形成历史
  images      List images #列出系统当前的镜像
  import      Import the contents from a tarball to create a filesystem image # 从 tar包中导入内容创建一个文件系统镜像，对应[export]
  info        Display system-wide information # 显示全系统信息
  inspect     Return low-level information on Docker objects # 查看容器详细信息
  kill        Kill one or more running containers # kill指定docker容器
  load        Load an image from a tar archive or STDIN # 从一个tar包或标准输入中加载一个镜像[对应save]
  login       Log in to a Docker registry # 注册或者登陆一个docker源服务器
  logout      Log out from a Docker registry # 从当前的docker registry 退出
  logs        Fetch the logs of a container # 输出当前容器的日志信息
  pause       Pause all processes within one or more containers # 暂停容器
  port        List port mappings or a specific mapping for the container # 查看映射端口对应容器的源端口
  ps          List containers # 列出容器列表
  pull        Pull an image or a repository from a registry # 拉取指定镜像或者库镜像
  push        Push an image or a repository to a registry # 推送指定镜像或者库镜像 
  rename      Rename a container # 重命名容器
  restart     Restart one or more containers # 重启动容器
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default) # 保存镜像为一个tar包，对应[load]
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE # 给源中镜像打标签
  top         Display the running processes of a container 	# 查看进程信息
  unpause     Unpause all processes within one or more containers # 取消暂停
  update      Update configuration of one or more containers	
  version     Show the Docker version information	# 版本
  wait        Block until one or more containers stop, then print their exit codes # 截取容器停止时的推出状态值
```



## 帮助命令

```
docker version		# 显示docker版本信息
docker info 		# 显示docker的系统信息，包括镜像和容器数量
docker --help -h 	# 
```

## 镜像命令

`docker images`查看本地主机的所有镜像

```shell
➜  ~ docker images
REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
mysql                 5.7                 e73346bdf465        24 hours ago        448MB

# 解释
#REPOSITORY			# 镜像的仓库源
#TAG				# 镜像的标签
#IMAGE ID			# 镜像的id
#CREATED			# 镜像的创建时间
#SIZE				# 镜像的大小
# 可选项
Options:
  -a, --all             Show all images (default hides intermediate images) # 列出所有镜像
  -q, --quiet           Only show numeric IDs # 只显示镜像的id
  
➜  ~ docker images -aq ＃显示所有镜像的id
e73346bdf465
d03312117bb0
d03312117bb0
602e111c06b6
2869fc110bf7
470671670cac
bf756fb1ae65
5acf0e8da90b
```

`docker search`搜索镜像

```shell
➜  ~ docker search mysql
NAME                              DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
mysql                             MySQL is a widely used, open-source relation…   9500                [OK]                
mariadb                           MariaDB is a community-developed fork of MyS…   3444                [OK]  
# --filter=STARS=3000 # 搜索出来的镜像就是STARS大于3000的
Options:
  -f, --filter filter   Filter output based on conditions provided
      --format string   Pretty-print search using a Go template
      --limit int       Max number of search results (default 25)
      --no-trunc        Don't truncate output
      
➜  ~ docker search mysql --filter=STARS=3000
NAME                DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
mysql               MySQL is a widely used, open-source relation…   9500                [OK]             
mariadb             MariaDB is a community-developed fork of MyS…   3444                [OK]
```

`docker pull`下载镜像

```shell
# 下载镜像 docker pull 镜像名[:tag]
➜  ~ docker pull tomcat:8
8: Pulling from library/tomcat # 如果不写tag，默认就是latest最新版
90fe46dd8199: Already exists   # 分层下载： docker image 的核心 联合文件系统
35a4f1977689: Already exists 
bbc37f14aded: Already exists 
74e27dc593d4: Already exists 
93a01fbfad7f: Already exists 	# 如果本地之前版本已经存在的层则不用下载
1478df405869: Pull complete 	# 如果更改过的层则重新下载
64f0dd11682b: Pull complete 
68ff4e050d11: Pull complete 
f576086003cf: Pull complete 
3b72593ce10e: Pull complete 
Digest: sha256:0c6234e7ec9d10ab32c06423ab829b32e3183ba5bf2620ee66de866df640a027  # 签名 防伪
Status: Downloaded newer image for tomcat:8
docker.io/library/tomcat:8 # 真实地址

# 等价于
docker pull tomcat:8
# 或者
docker pull docker.io/library/tomcat:8
```

`docker rmi`删除镜像

```shell
➜  ~ docker rmi -f 镜像id 						# 删除指定的镜像
➜  ~ docker rmi -f 镜像id 镜像id 镜像id 镜像id		# 删除指定的镜像
➜  ~ docker rmi -f $(docker images -aq) 	     # 删除全部的镜像
```

## 容器命令

```shell
docker run 镜像id 		   # 新建容器并启动
docker ps 					# 列出所有运行的容器 docker container list
docker rm 容器id 删除指定容器
docker start 容器id #启动容器
docker restart 容器id #重启容器
docker stop 容器id #停止当前正在运行的容器
docker kill 容器id #强制停止当前容器
```

```shell
docker run [可选参数] image | docker container run [可选参数] image 
# 参数说明
--name="Name"		容器名字 tomcat01 tomcat02 用来区分容器
-d					后台方式运行
-it 				使用交互方式运行，并进入容器
-p					指定容器的端口 -p 8080(宿主机):8080(容器)
		-p ip:主机端口:容器端口
		-p 主机端口:容器端口(常用)	# 主机端口映射到容器端口
		-p 容器端口
		容器端口
-P(大写) 				随机指定端口

# 测试、启动并进入容器
➜  ~ docker run -it centos /bin/bash
Unable to find image 'centos:latest' locally
latest: Pulling from library/centos
8a29a15cefae: Already exists 
Digest: sha256:fe8d824220415eed5477b63addf40fb06c3b049404242b31982106ac204f6700
Status: Downloaded newer image for centos:latest
[root@95039813da8d /]# ls    	# 主机名就是镜像id
bin  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
[root@95039813da8d /]# exit 	# 从容器退回主机
exit
```

`docker ps`列出正在运行的容器

```shell
#docker ps命令 			 # 列出当前正在运行的容器
  -a, --all               # 展示所有容器，不管是不是在运行
  -n, --last int          # 展示最近n个创建的容器
  -q, --quiet             # 只显示容器编号
  
  ➜  ~ docker ps   
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                    NAMES
68729e9654d4        portainer/portainer   "/portainer"             14 hours ago        Up About a minute   0.0.0.0:8088->9000/tcp   funny_curie
d506a017e951        nginx                 "nginx -g 'daemon of…"   15 hours ago        Up 15 hours         0.0.0.0:3344->80/tcp     nginx01

➜  ~ docker ps -a
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS                       PORTS                    NAMES
95039813da8d        centos                "/bin/bash"              3 minutes ago       Exited (0) 2 minutes ago                              condescending_pike
1e46a426a5ba        tomcat                "catalina.sh run"        11 minutes ago      Exited (130) 9 minutes ago                            sweet_gould
14bc9334d1b2        bf756fb1ae65          "/hello"                 3 hours ago         Exited (0) 3 hours ago                                amazing_stonebraker
f10d60f473f5        bf756fb1ae65          "/hello"                 3 hours ago         Exited (0) 3 hours ago                                dreamy_germain
68729e9654d4        portainer/portainer   "/portainer"             14 hours ago        Up About a minute            0.0.0.0:8088->9000/tcp   funny_curie
677cde5e4f1d        elasticsearch         "/docker-entrypoint.…"   15 hours ago        Exited (143) 8 minutes ago                            elasticsearch

➜  ~ docker ps -aq
95039813da8d
1e46a426a5ba
14bc9334d1b2
f10d60f473f5
68729e9654d4
677cde5e4f1d
```

退出容器

```shell
exit 		# 容器停止并退出
ctrl P Q 	# 容器不停止退出
```

删除容器

```shell
docker rm 容器id   # 删除指定的容器，不能删除正在运行的容器，如果要强制删除 rm -f
docker rm -f $(docker ps -aq)  		# 删除所有的容器
docker ps -a -q|xargs docker rm  	# 删除所有的容器
```

启动和停止容器

```shell
docker start 容器id	# 启动容器
docker restart 容器id	# 重启容器
docker stop 容器id	# 停止当前正在运行的容器
docker kill 容器id	# 强制停止当前容器
```

## 其他命令

后台启动命令

```shell
# 命令 docker run -d 镜像名
➜  ~ docker run -d centos
a8f922c255859622ac45ce3a535b7a0e8253329be4756ed6e32265d2dd2fac6c
➜  ~ docker ps           
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
# 问题：运行docker ps查看正在运行的容器. 发现centos 停止了
# 常见的坑，docker容器使用后台运行，就必须要有要一个前台进程，docker发现没有应用，就会自动停止
# nginx，容器启动后，发现自己没有提供服务，就会立刻停止，就是没有程序了
# 以centos为例，交互模式启动之后ctrl+p+q 不停止退出，这个容器就还在启动状态
```

`docker logs`查看日志

```shell
docker logs --help
Options:
      --details        Show extra details provided to logs 
*  -f, --follow         Follow log output
      --since string   Show logs since timestamp (e.g. 2013-01-02T13:23:37) or relative (e.g. 42m for 42 minutes)
*      --tail string    Number of lines to show from the end of the logs (default "all")
*  -t, --timestamps     Show timestamps
      --until string   Show logs before a timestamp (e.g. 2013-01-02T13:23:37) or relative (e.g. 42m for 42 minutes)
      
➜  ~ docker run -d centos /bin/sh -c "while true;do echo 6666;sleep 1;done" #模拟日志      
#显示日志
-tf		# 显示日志信息（一直更新）
--tail number 
# 例子
docker logs -t --tail n 容器id 	# 查看最新的n条log	
docker logs -tf 容器id 			# 持续打印log	
```

`docker top`查看容器内的进程信息

```shell
# docker top 容器id
docker top a137fecf48a0                                                                                        ─╯
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                2353                2327                0                   17:04               ?                   00:00:00            /bin/sh -c while true;do echo 6666;sleep 1;done
root                2740                2353                0                   17:10               ?                   00:00:00            /usr/bin/coreutils --coreutils-prog-shebang=sleep /usr/bin/sleep 1
```

`docker inspect`查看容器的元数据

```shell
# 命令
docker inspect 容器id

➜  ~ docker inspect a137fecf48a0
[
    {
        "Id": "a137fecf48a078fec112e2e3f8d1991f2950ac53dbc9818b88933ab9bebf2706",
        "Created": "2021-12-23T17:04:34.662694965Z",
        "Path": "/bin/sh",
        "Args": [
            "-c",
            "while true;do echo 6666;sleep 1;done"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 2353,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2021-12-23T17:04:34.842278549Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:e6a0117ec169eda93dc5ca978c6ac87580e36765a66097a6bfb6639a3bd4038a",
        "ResolvConfPath": "/var/lib/docker/containers/a137fecf48a078fec112e2e3f8d1991f2950ac53dbc9818b88933ab9bebf2706/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/a137fecf48a078fec112e2e3f8d1991f2950ac53dbc9818b88933ab9bebf2706/hostname",
        "HostsPath": "/var/lib/docker/containers/a137fecf48a078fec112e2e3f8d1991f2950ac53dbc9818b88933ab9bebf2706/hosts",
        "LogPath": "/var/lib/docker/containers/a137fecf48a078fec112e2e3f8d1991f2950ac53dbc9818b88933ab9bebf2706/a137fecf48a078fec112e2e3f8d1991f2950ac53dbc9818b88933ab9bebf2706-json.log",
        "Name": "/compassionate_volhard",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/b84dd4616d3ca64b2532a7a6fbeec54fa7cceffd7143ad01057f4f54dfcc7506-init/diff:/var/lib/docker/overlay2/9305ee5b56f8cef9debeb900e1462d44ab176aac042a4efd18a05ac1208a20ce/diff",
                "MergedDir": "/var/lib/docker/overlay2/b84dd4616d3ca64b2532a7a6fbeec54fa7cceffd7143ad01057f4f54dfcc7506/merged",
                "UpperDir": "/var/lib/docker/overlay2/b84dd4616d3ca64b2532a7a6fbeec54fa7cceffd7143ad01057f4f54dfcc7506/diff",
                "WorkDir": "/var/lib/docker/overlay2/b84dd4616d3ca64b2532a7a6fbeec54fa7cceffd7143ad01057f4f54dfcc7506/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "a137fecf48a0",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "while true;do echo 6666;sleep 1;done"
            ],
            "Image": "centos",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {
                "org.label-schema.build-date": "20210915",
                "org.label-schema.license": "GPLv2",
                "org.label-schema.name": "CentOS Base Image",
                "org.label-schema.schema-version": "1.0",
                "org.label-schema.vendor": "CentOS"
            }
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "d7a3338387f8c9a9ddc4e2925a10c3cbee398b61ad0e422fdc76c2071197fab3",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/d7a3338387f8",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "a47504dc8515e6f2e22e7f672a58cf977507897f20a7b1846b7ee04e525c8ed0",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.3",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:03",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "b65ef02cb1dea068b9b350130bc94f5b09b6ffc60b9ab47b9ba6d3adf5cf83e5",
                    "EndpointID": "a47504dc8515e6f2e22e7f672a58cf977507897f20a7b1846b7ee04e525c8ed0",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.3",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:03",
                    "DriverOpts": null
                }
            }
        }
    }
]
```

进行当前正在运行的容器

方式1：`docker exec -it`进入当前容器后开启一个新的终端，可以在里面操作。（常用）

```shell
# 我们通常容器都是使用后台方式运行的，需要进入容器，修改一些配置

# 命令 
docker exec -it 容器id /bin/bash

# Demo
docker exec -it a137fecf48a0 /bin/bash
```

方式2：`docker attach`进入容器正在执行的终端，进入的是正在运行的命令行

```
docker attach a137fecf48a0
```

`docker cp` 容器id:容器路径 主机目标路径

`docker cp` 主机路径 容器id:容器目标路径，也可以使用 -v 挂载卷的方式自动同步目录

