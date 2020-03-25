Git is a version control system.
Git is free software.


初始化一个Git仓库，使用‘git init’命令。
添加文件到Git仓库，分两步：
1.使用‘git add <file>’命令,将文件修改添加到暂存区。注意，可反复多次使用，添加多个文件；
2.使用命令‘git commit -m <messages>’，将暂存区的所有内容提交到master分支版本库。


随时掌握工作区的状态，使用‘git status’命令。
如果‘git status’告诉你有文件被修改过，用‘git diff’可以查看修改内容。


使用‘cat’命令查看文件内容。
使用‘git log’命令显示从最近到最远的提交日志，如果嫌输出信息太多，加上‘--pretty=oneline’参数。
HEAD指向的版本就是当前版本，因此，Git允许在版本的历史之间穿梭，使用命令‘git reset --hard commit_id’。
重新回到最近版本，用‘git reflog’命令查看历史，以便确定回到最近的哪个版本。


git跟踪并管理的是修改，并非文件。
每次修改需要用‘git add’命令将修改放入暂存区，最后统一用‘git commit’命令加入版本库。


场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令‘git checkout -- <file>’。
场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步：
1.用‘git restore --staged <fi1e>‘，回到了场景1；
2.按场景1操作。


场景1：将版本库中的文件删除，用命令’git rm‘和’git commit‘。
场景2：仅删除工作区中文件，用命令’rm‘；恢复删除文件到最新版本：’git checkout -- <file>‘。注意：从来没有被添加到版本库就被删除的文件，是无法恢复的。


关联远程库，使用命令‘git remote add origin git@server-name:path/repo-name.git’。
关联后，使用命令‘git push -u origin master’第一次推送master分支的所有内容。
此后，每次本地提交后，只要有必要，就可以使用命令‘git push origin master’推送最新修改。


克隆远程库，首先必须知道仓库的地址，然后使用命令‘git clone’克隆。
git支持多种协议，默认的‘git://’使用ssh，但也可以使用‘https://’等其他协议。
使用‘https://’除了速度慢，还有最大的麻烦是每次推送都必须输入口令，但是在某些只开放http端口的公司内部就无法使用ssh协议而只能用https。


查看分支：‘git branch’
创建分支：‘git branch <name>’
切换分支：‘git switch <name>’（推荐）或‘git checkout <name>’
创建+切换分支：‘git switch -c <name>’（推荐）或‘git checkout -b <name>’
合并某分支到当前分支：‘git merge <name>’
删除分支：‘git branch -d <name>’