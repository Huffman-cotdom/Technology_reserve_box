---
title: Hexo文件管理
date: 2021-11-10 18:06:47
tags:
- Hexo
categories:
- Blog
---
当Blog逐渐增多时，发现`_post`文件夹下显得杂乱不堪~
<!-- more -->

```shell
hexo n post -p Hexo/Hexo文件管理 "Hexo文件管理"
or
hexo new post -p Hexo/Hexo文件管理 "Hexo文件管理"
```

新建Blog文件时使用这条命令，就会在`_post`文件夹下新建一个`Hexo`子文件夹，并在其中新建一个`Hexo文件管理.md`的文件，`"Hexo文件管理"`是title的名称。

```shell
Hexo
├── Hexo文件管理
└── Hexo文件管理.md
```

