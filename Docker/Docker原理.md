# Docker原理

Docker是一个Client-Server结构的系统，Docker的守护进程运行在宿主机上，通过Socket从DockerClient访问，DockerServer接收到指令，就会执行该指令。

![Docker通信原理](docker%E5%8E%9F%E7%90%86/20201111111901922.png)

## Docker为什么比 VM 快

1. docker有着比虚拟机更少的抽象层。由于docker不需要Hypervisor实现硬件资源虚拟化，运行在docker容器上的程序直接使用的都是实际物理机的硬件资源。因此在CPU、内存利用率上docker将会在效率上有明显优势。
2. docker利用的是宿主机的内核，而不需要Guest OS。

![20201111112236733](docker%E5%8E%9F%E7%90%86/20201111112236733.png)

因此,当新建一个 容器时，docker不需要和虚拟机一样重新加载一个操作系统内核。避免引导、加载操作系统内核返个比较费时费资源的过程,当新建一个虚拟机时,虚拟机软件需要加载GuestOS，返个新建过程是分钟级别的。而docker由于直接利用宿主机的操作系统，则省略了这个复杂的过程,因此新建一个docker容器只需要几秒钟。

