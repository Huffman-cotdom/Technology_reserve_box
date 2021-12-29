```shell
git branch -r | grep -v '\->' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done	# 在本地新建与远程所有相同的分支并追踪
git fetch --all	# 将远程主机的最新内容拉到本地
git pull --all
```