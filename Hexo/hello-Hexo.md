---
title: Hello Hexo
date: 2021-10-09 
tags: 
- Hexo
- 网页
categories: 
- Blog
---

## What is Hexo？

[Hexo](https://hexo.io/zh-cn/)是一个快速、简洁且高效的博客框架。Hexo 使用 [Markdown](http://daringfireball.net/projects/markdown/)（或其他渲染引擎）解析文章，在几秒内，即可利用靓丽的主题生成静态网页。

<!--more-->

## What is Github Pages？

GitHub Pages是用户自己编写并托管在GitHub上的静态网页。使用GitHub Pages托管可以提供免费的服务器，不用自己再搭建服务器和数据库，也可以绑定自己的域名。

## Quick Start

### Install

#### Requirements

- [Git](http://git-scm.com/)
- [Node.js](http://nodejs.org/) (Should be at least Node.js 10.13, recommends 12.0 or higher)

Mac直接使用HomeBrew安装即可。

安装完成之后在终端输入一下命令查看是否安装成功：

```bash
git --version
node -v
nlp -v
```

#### Install Hexo

在安装之前最好新建一个Blog的文件夹，然后在该文件下执行一下命令开始安装

```bash
npm install -g hexo-cli
```

这里直接安装最新版本即可。

##### Install Git page deployer

部署到GitHub Pages需要安装对应的deployer

```bash
npm install hexo-deployer-git --save
```

到这里就安装Hexo就安装成功了。接下来是Hexo的初始化以及一下简单配置。

### Init

在刚才新建的文件夹Blog下面新建一个存放Hexo相关配置的文件夹，这里假设为Hexo。在该目录下进行Hexo初始化。

```bash
hexo init
```

初始化完成之后可以看到该文件夹下的目录结构如下：

```bash
.
├── _config.yml
├── package.json
├── scaffolds
├── source
|   ├── _drafts
|   └── _posts
└── themes
```

#### _config.yml

网站的[配置](https://hexo.io/zh-cn/docs/configuration)信息，可以在此配置大部分的参数。

#### package.json

应用程序的信息。[EJS](https://ejs.co/), [Stylus](http://learnboost.github.io/stylus/) 和 [Markdown](http://daringfireball.net/projects/markdown/) renderer 已默认安装，可以自由移除。

#### scaffolds

[模版](https://hexo.io/zh-cn/docs/writing) 文件夹。当新建文章时，Hexo 会根据 scaffold 来建立文件。

Hexo的模板是指在新建的文章文件中默认填充的内容。如果修改scaffold/post.md中的Front-matter内容，那么每次新建一篇文章时都会包含这个修改。

#### Source

资源文件夹是存放用户资源的地方。除 `_posts` 文件夹之外，开头命名为 `_` (下划线)的文件 / 文件夹和隐藏的文件将会被忽略。Markdown 和 HTML 文件会被解析并放到 `public` 文件夹，而其他文件会被拷贝过去。

#### themes

[主题](https://hexo.io/zh-cn/docs/themes) 文件夹。Hexo 会根据主题来生成静态页面

### 本地查看渲染效果

```bash
hexo generate	# 生成静态文件
hexo server		# 启动服务器。默认情况下，访问网址为： http://localhost:4000/
```

输入以上命令之后终端返回一下信息证明操作成功：

```bash
INFO  Validating config
INFO  Start processing
INFO  Hexo is running at http://localhost:4000 . Press Ctrl+C to stop.
```

此时点击该网址即可查看渲染效果。

### 将Hexo部署到GitHub Pages

将博客部署到GitHub Pages上的目的是为了方便别人访问我们的博客☺️。

1. 需要注册一个[GitHub](https://github.com/)账号。

2. 为博客新建一个仓库：点击 New repository 开始创建。此处需要注意仓库名的命名规则，前缀和用户名一致，后缀为github.io

   ![Demo](hello-world/image-20211010141415767.png)

3. 、配置 SSH 密钥：只有配置好 SSH 密钥后，我们才可以通过 git 操作实现本地代码库与 Github 代码库同步

   ```bash
   ssh-keygen -t rsa -C "your email@example.com"
   ```

   之后会出现：

   ```bash
   Generating public/private rsa key pair.
   Enter file in which to save the key (/地址/.ssh/id_rsa):
   # 到这里可以直接回车将密钥按默认文件地址进行存储
   ```

   然后会出现：

   ```bash
   Enter passphrase (empty for no passphrase):
   # 这里是要你输入密码，只需要输入简单的回车即可
   Enter same passphrase again:
   # 同样
   ```

   接下来屏幕会显示：

   ```bash
   Your identification has been saved in /地址/.ssh/id_rsa.
   Your public key has been saved in /地址/.ssh/id_rsa.pub.
   The key fingerprint is:
   # 这里是各种字母数字组成的字符串，结尾是你的邮箱
   The key's randomart image is:
   # 这里也是各种字母数字符号组成的字符串
   ```

   运行以下命令，将公钥的内容复制到系统粘贴板上

   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```

   4. 在 GitHub 账户中添加你的公钥
      1. 登陆 GitHub，进入 Settings：
      2. 点击 SSH and GPG Keys：
      3. 选择 New SSH key：
         ![New SSH Key](hello-world/13.jpg)
      4. 粘贴密钥：
         ![Add Key](hello-world/14.jpg)

   5. 测试是否成功：

      ```bash
      ssh -T git@github.com                                                                                   ─╯
      Hi Huffman-cotdom! You've successfully authenticated, but GitHub does not provide shell access.
      ```

      此时显示配置成功。

   6. 配置Git个人信息：

      Git 会根据用户的名字和邮箱来记录提交，GitHub 也是用这些信息来做权限的处理，输入以下命令进行个人信息的设置，把名称和邮箱替换成你自己的，名字可以不是 GitHub 的昵称，但为了方便记忆，建议与 GitHub 一致

      ```bash
      git config --global user.name "此处填你的用户名"
      git config --global user.email "此处填你的邮箱"
      ```

      到此为止 SSH Key 配置成功，本机已成功连接到 Github。

### 将本地的Hexo文件同步到GitHub仓库中

1. copy刚刚新建的仓库ssh地址

2. 打开_config.yml文件并做如下修改并保存：

   ```bash
   # Deployment
   ## Docs: https://hexo.io/docs/one-command-deployment
   deploy:
     type: git
     repository: git@github.com:Huffman-cotdom/Huffman_cotdom.github.io.git
     branch: main
   ```

   注意：冒号之后有一个空格…

3. 在Hexo文件夹下执行一下命名

   ```bash
   hexo g
   hexo d	
   ```

   或者

   ```bash
   hexo g -d
   ```

   执行完之后会让你输入你的 Github 的账号和密码，如果此时报以下错误，说明你的 deployer 没有安装成功

   ```bash
   ERROR Deployer not found: git
   ```

   需要重新安装一次依赖

   ```bash
   npm install hexo-deployer-git --save
   ```

   此时应该就能正常访问博客了。博客地址为：https://你的用户名.github.io，比如我的是：[https://huffman-cotdom.github.io/](https://huffman-cotdom.github.io/) ，现在每个人都可以通过此链接访问你的博客了。

   注意：这里是不区分大小写的

### 发布博客

1. 在Hexo路径下执行以下命令即可在 \Hexo\source\_posts 中生成 文章标题.md 文件，文章标题根据需要命名

   ```bash
   hexo n "文章标题"
   ```

   也可以直接在 \Hexo\source\_posts 目录下新建md文档

2. 发布

   写完文档之后可以先在本地查看网页内容

   ```bash
   hexo s
   ```

   没有问题之后便可推送到服务器上

   ```bash
   hexo g -d
   ```
   
   

## 总结

Hexo博客从安装到简单配置大致流程就这些，但是其丰富的配置远不止于此，等待后续的研究，将继续更新相关的博客~





