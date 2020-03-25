Git is a version control system.
Git is free software.

初始化一个Git仓库，使用‘git init’命令。
添加文件到Git仓库，分两步：
1.使用‘git add <file>’命令,将文件修改添加到暂存区。注意，可反复多次使用，添加多个文件；
2.使用命令‘git commit -m <messages>’，将暂存区的所有内容提交到master分支。

随时掌握工作区的状态，使用‘git status’命令。
如果‘git status’告诉你有文件被修改过，用‘git diff’可以查看修改内容。

使用‘cat’命令查看文件内容。
使用‘git log’命令显示从最近到最远的提交日志，如果嫌输出信息太多，加上‘--pretty=oneline’参数。
HEAD指向的版本就是当前版本，因此，Git允许在版本的历史之间穿梭，使用命令‘git reset --hard commit_id’。
重新回到最近版本，用‘git reflog’命令查看历史，以便确定回到最近的哪个版本。

git跟踪并管理的是修改，并非文件。
每次修改需要用‘git add’命令将修改放入暂存区，最后统一用‘git commit’命令加入master。