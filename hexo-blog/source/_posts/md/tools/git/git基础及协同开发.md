---
title: 'git基础及协同开发'
date: 2022-8-9 09:03:02
cover: false
tags:
- git
categories: git
---





教程来源：https://www.bilibili.com/video/BV1tz411i7t1?p=1

# 2.使用git

## 2.1.初始化

进入需要被管理的文件夹，右键点击`Git Bash Here`

- `git init`

  ```git
  
  Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev
  $ git init
  Initialized empty Git repository in D:/hh/workspace/git/code_dev/.git/
  
  ```

  - 出现了.git的文件夹，表示git已经开始管理当前文件夹了
    - 所有的配置、版本信息，都会存储在.git文件夹中

- `git status`

  - 检测当前文件夹下，文件的状态

    ```git
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
    $ git status
    On branch master
    
    No commits yet
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            git.md
            index.txt1
    
    nothing added to commit but untracked files present (use "git add" to track)
    
    ```

  - 如果又新增了一个文件，再执行`git status`，也是可以检测到的

## 2.2.管理文件

- `git add `

  - 管理文件

  - `git add git.md`

    - 表示管理`git.md`这个文件，其他的不管

      ```git
      Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
      $ git add git.md
      
      Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
      $ git status
      On branch master
      
      No commits yet
      
      Changes to be committed:
        (use "git rm --cached <file>..." to unstage)
              new file:   git.md
      
      Untracked files:
        (use "git add <file>..." to include in what will be committed)
              index.txt1
      
      ```

      再执行`git status`，只提示`index.txt1`未被管理（已管理的文件，绿色显示；未被管理的文件，红色显示）

- `git add .`

  - 管理当前文件夹下的所有文件

## 2.3.生成版本

- `git commit -m 'version1'`

  ```git
  Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
  $ git commit -m 'version1'
  [master (root-commit) 3b08830] version1
   2 files changed, 79 insertions(+)
   create mode 100644 git.md
   create mode 100644 index.txt1
  ```

  - 再执行`git status`

    ```git
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
    $ git status
    On branch master
    nothing to commit, working tree clean
    ```

- `git log`

  - 查看版本控制记录

    ```git
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
    $ git log
    commit b29cdcd1e80198c462e866f2ccbf218a2598a64b (HEAD -> master)
    Author: 666 <1314520@qq.com>
    Date:   Tue Oct 19 14:40:53 2021 +0800
    
        v2
    
    commit 0dbd95e75cbb238f270f6a271a0329c39195f53d
    Author: 666 <1314520@qq.com>
    Date:   Tue Oct 19 14:38:36 2021 +0800
    
        version1
    
    commit 3b08830cbfe98f1e382841f13ce2f2ba294bd43e
    Author: 666 <1314520@qq.com>
    Date:   Tue Oct 19 14:36:45 2021 +0800
    
        version1
    
    ```

## 2.4.命令总结

- `git init`
- `git status`
- `git add`
- `git commit`
- `git log`

- 三种状态的变化
  - 红色：新增的文件/修改的文件  --> `git add .`
  - 绿色：git已经管理起来  -->  `git commit -m '描述信息'`
  - 生成版本

## 2.5.使用注意点

**配置个人信息**

生成版本前，如果是第一次使用git的时候，会报错

按照提示，输入用户名和邮箱即可

```
git config --global user.email "test@email.com"
git config --global user.name "testName"
```

# 3.git三大区域

- 工作区
  - 正在工作的文件夹
  - 有两种文件状态
    - 已管理
    - 新的文件/修改的文件
  - git自动检测文件状态
- 暂存区
  - 通过`git add .`将文件提交到暂存区
  - 如果不要了，这一步操作是可以回滚的
- 版本库

**图示：**

![在这里插入图片描述](https://img-blog.csdnimg.cn/65f46c51b6b243aca89870c18d0cbf62.png)

## 3.1.回滚

**git reset**

```git
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
$ git log
commit 08e2cdaa95ca317d89413ed577b93fca99f076e6 (HEAD -> master)
Author: 666 <1314520@qq.com>
Date:   Tue Oct 19 15:29:26 2021 +0800

    yuefan

commit 2b4df9b308a682d52aa27204f145ab721523ff17
Author: 666 <1314520@qq.com>
Date:   Tue Oct 19 15:27:27 2021 +0800

    shipin

commit b29cdcd1e80198c462e866f2ccbf218a2598a64b
Author: 666 <1314520@qq.com>
Date:   Tue Oct 19 14:40:53 2021 +0800

    v2

commit 0dbd95e75cbb238f270f6a271a0329c39195f53d
Author: 666 <1314520@qq.com>
Date:   Tue Oct 19 14:38:36 2021 +0800

    version1

```

`git reset --hard 版本号`

```git
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
$ git reset --hard 2b4df9b308a682d52aa27204f145ab721523ff17
HEAD is now at 2b4df9b shipin

```

查看文件夹，yuefan功能创建的文件，已经没有了，文件夹版本回滚了shipin功能刚提交时的版本

此时`git log`只有到shipin的版本记录

```git
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
$ git log
commit 2b4df9b308a682d52aa27204f145ab721523ff17 (HEAD -> master)
Author: 666 <1314520@qq.com>
Date:   Tue Oct 19 15:27:27 2021 +0800

    shipin

commit b29cdcd1e80198c462e866f2ccbf218a2598a64b
Author: 666 <1314520@qq.com>
Date:   Tue Oct 19 14:40:53 2021 +0800

    v2

commit 0dbd95e75cbb238f270f6a271a0329c39195f53d
Author: 666 <1314520@qq.com>
Date:   Tue Oct 19 14:38:36 2021 +0800

    version1

commit 3b08830cbfe98f1e382841f13ce2f2ba294bd43e
Author: 666 <1314520@qq.com>
Date:   Tue Oct 19 14:36:45 2021 +0800

    version1

```

这个时候，如果又想回滚到yuefan功能的版本，`git log`无法解决问题

需要使用如下命令：

`git reflog`

```git
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
$ git reflog
2b4df9b (HEAD -> master) HEAD@{0}: reset: moving to 2b4df9b308a682d52aa27204f145ab721523ff17
08e2cda HEAD@{1}: commit: yuefan
2b4df9b (HEAD -> master) HEAD@{2}: commit: shipin
b29cdcd HEAD@{3}: commit: v2
0dbd95e HEAD@{4}: commit: version1
3b08830 HEAD@{5}: commit (initial): version1

```

上述的`08e2cda HEAD@{1}: commit: yuefan`

最前面，就是yuefan功能的版本号

回滚到yuefan功能

```git
git reset --hard 08e2cda
```

```git
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
$ git reset --hard 08e2cda
HEAD is now at 08e2cda yuefan
```

`git log`查看，回到了当初`yuefan`功能的版本

```git
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
$ git log
commit 08e2cdaa95ca317d89413ed577b93fca99f076e6 (HEAD -> master)
Author: 666 <1314520@qq.com>
Date:   Tue Oct 19 15:29:26 2021 +0800

    yuefan

commit 2b4df9b308a682d52aa27204f145ab721523ff17
Author: 666 <1314520@qq.com>
Date:   Tue Oct 19 15:27:27 2021 +0800

    shipin

commit b29cdcd1e80198c462e866f2ccbf218a2598a64b
Author: 666 <1314520@qq.com>
Date:   Tue Oct 19 14:40:53 2021 +0800

    v2

commit 0dbd95e75cbb238f270f6a271a0329c39195f53d
Author: 666 <1314520@qq.com>
Date:   Tue Oct 19 14:38:36 2021 +0800

    version1

commit 3b08830cbfe98f1e382841f13ce2f2ba294bd43e
Author: 666 <1314520@qq.com>
Date:   Tue Oct 19 14:36:45 2021 +0800

    version1

```

## 3.2.命令及作用总结



![在这里插入图片描述](https://img-blog.csdnimg.cn/30c2798e33f544dab1ccade70ef0757c.png)

# 4.初识分支

## 4.1.紧急修复线上bug思路

会创建一个新的分支，修复后合并到master里面

## 4.2.基于分支修复线上bug具体过程

- `git branch`
  - 查看当前所处的分支

    ```git
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
    $ git branch
    * master
    ```

  - 当前是处在master分支上

- `git branch dev`

  - 创建`dev`分支
    - 这个dev分支，是基于当前的master分支的
    - 功能更新到了yuefan
    - 现在在新的分支上，开发商城功能

- `git checkout dev`

  - 从`master分支`切换到`dev`分支

  - 相当于切换了一个新的环境，在`dev`分支上写代码，是不影响`master`分支的

    ```git
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
    $ git checkout dev
    Switched to branch 'dev'
    
    ```

  - 切换之后，新增文件，并用`git status`查看状态

    ```git
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (dev)
    $ git status
    On branch dev
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            tmall.txt1
    
    nothing added to commit but untracked files present (use "git add" to track)
    
    ```

  - 这个时候再提交到暂存区，都是在`dev`分支进行操作的

- master出现了bug

  - 切换回master分支

    ```git
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (dev)
    $ git checkout master
    Switched to branch 'master'
    
    ```

  - 此时文件夹里，包含商城功能的`tmall.txt1`，已经没有了，因为当前分支是`master`，商城功能是在`dev`分支上开发的

  - 可以再切换到`dev`分支验证下，文件又回到商城功能的版本了（分支和分支之间，做了代码隔离）

- `git branch bug`

  - 在`master`分支上，创建名称为`bug`的分支

  - 跳转到bug分支：`git checkout bug`，在yuefan功能上修改

    ```git
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
    $ git checkout bug
    Switched to branch 'bug'
    
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (bug)
    $ git add .
    
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (bug)
    $ git commit -m 'bug_modify_c5'
    [bug aa7250e] bug_modify_c5
     2 files changed, 2 insertions(+), 1 deletion(-)
     delete mode 100644 yuefan.txt1
     create mode 100644 yuefan_modify_bug.txt1
    
    ```

  - bug修复完毕，但此时是在`bug`分支上修复的bug，`master`分支上还没有修复

    - 一般线上运行的分支，都是`master`分支
    - 子分支上修复完bug之后，需要合并到`master`上

- `git merge 分支名称`

  - 切换回`master`分支

  - `git merge bug`

    ```git
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (bug)
    $ git checkout master
    Switched to branch 'master'
    
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
    $ git merge bug
    Updating 08e2cda..aa7250e
    Fast-forward
     yuefan.txt1            | 1 -
     yuefan_modify_bug.txt1 | 2 ++
     2 files changed, 2 insertions(+), 1 deletion(-)
     delete mode 100644 yuefan.txt1
     create mode 100644 yuefan_modify_bug.txt1
    
    ```

- `git branch -d bug`

  - 删除`bug`分支

  - 修复完bug后，`bug`分支已经没用了

    ```git
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
    $ git branch -d bug
    Deleted branch bug (was aa7250e).
    
    ```

- bug修复完之后，可以切换到`dev`分支，继续开发商城功能了

  - `dev`分支，是从一开始的master上分下来的，bug还没有修复呢

    - 这个暂时不用管

  - 就专注于新功能的开发

    ```git
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (master)
    $ git checkout dev
    Switched to branch 'dev'
    
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (dev)
    $ git status
    On branch dev
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   tmall.txt1
    
    no changes added to commit (use "git add" and/or "git commit -a")
    
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (dev)
    $ git add .
    
    Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_dev (dev)
    $ git commit -m "mall_version_complete"
    [dev caf51f0] mall_version_complete
     1 file changed, 2 insertions(+), 1 deletion(-)
    
    ```

  - 新功能开发完毕后，进入`master`分支，合并`dev`分支

    - sd

    - 此时会报冲突：

      ```git
      Merge branch 'dev'
      # Please enter a commit message to explain why this merge is necessary,
      # especially if it merges an updated upstream into a topic branch.
      #
      # Lines starting with '#' will be ignored, and an empty message aborts
      # the commit.
      ~
      
      ```


## 4.3.分支命令总结

- 查看分支

  ```
  git branch
  ```

- 创建分支

  ```
  git branch 分支名称
  ```

- 切换分支

  ```
  git checkout 分支名称
  ```

- 分支合并（可能产生冲突）

  ```
  git merge 要合并的分支
  
  注意：切换分支再合并
  ```

- 删除分支

  ```
  git branch -d 分支名称
  ```

## 4.4.git开发工作流

写代码，都在`dev`分支上写

# 5.github/gitee做代码托管

## 5.1.创建仓库

以gitee为例，新建仓库后，会有以下提示：

**简易的命令行入门教程:**

Git 全局设置:

```
git config --global user.name "莫回首"
git config --global user.email "2495620791@qq.com"
```

创建 git 仓库:

```
mkdir code_sai
cd code_sai
git init
touch README.md
git add README.md
git commit -m "first commit"
git remote add origin https://gitee.com/mindcons/code_sai.git
git push -u origin master
```

已有仓库?

```
cd existing_git_repo
git remote add origin https://gitee.com/mindcons/code_sai.git
git push -u origin master
```

## 5.2.推送代码

在windows按照上述流程并推送

```
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai
$ git init
Initialized empty Git repository in D:/hh/workspace/git/code_sai/.git/

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (master)
$ touch README.md

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (master)
$ git add README.md

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (master)
$ git commit -m 'first commit'
[master (root-commit) 74b14f4] first commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (master)
$ git remote add origin https://gitee.com/mindcons/code_sai.git

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (master)
$ git push -u origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 202 bytes | 202.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote: Powered by GITEE.COM [GNK-6.1]
To https://gitee.com/mindcons/code_sai.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.

```

此时打开：https://gitee.com/mindcons/code_sai

可以看到刚刚推送的文件了

## 5.3.推送分支

此时只有master分支，我们推送一下dev分支

```
// 切换到master分支
git checkout master
// 推送dev分支
git push -u origin dev
// 如果dev分支上已经commit了，可以在网页的dev分支上，看到专属于dev分支的文件
```

## 5.4.克隆代码

此时到了另外一个地方了，需要接着写代码，第一次需要把代码克隆下来

此时我们在code_sai意外的另外的地方，新建一个文件夹，模拟在其他地方（家里）

```
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/new_place
$ git clone https://gitee.com/mindcons/code_sai.git
Cloning into 'code_sai'...
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (5/5), done.

```

克隆下来之后，进入到code_sai，就可以进行任何想做的操作了

比如说，我们可以看到之前的提交记录：

```
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/new_place/code_sai (master)
$ git log
commit 74b14f41ae13432f28afdef724caa8c44b658ac5 (HEAD -> master, origin/master, origin/HEAD)
Author: sai <2495620791@qq.com>
Date:   Sat Oct 23 10:28:02 2021 +0800

    first commit

```

另外，这里默认显示的是master分支，我们用`git branch`虽然只看到了master分支

但dev分支也是都克隆下来的，可以直接进行切换

```
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/new_place/code_sai (master)
$ git branch
* master

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/new_place/code_sai (master)
$ git checkout dev
Switched to a new branch 'dev'
Branch 'dev' set up to track remote branch 'dev' from 'origin'.

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/new_place/code_sai (dev)
$

```

## 5.5.代码托管命令总结

- 给远程仓库起别名

  ```
  git remore add origin(别名) 仓库地址
  // 别名只用添加一遍
  ```

- 向远程推送代码

  ```
  git push -u origin 分支
  ```

- 克隆远程仓库

  ```
  git clone 远程仓库地址（内部已经实现 git remote add origin 远程仓库地址）
  ```

- 克隆之后可以切换分支

  ```
  git checkout 分支
  ```

# 6.两地开发

## 6.1.master分支合并到dev

我们给master加一个c7.txt1表示更新到版本7，修复了bug，此时dev是一个在版本6分出去的，要继续开发的话，需要在dev分支上，合并master

```
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (master)
$ git branch
  dev
* master

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (master)
$ git checkout dev
Switched to branch 'dev'
Your branch is up to date with 'origin/dev'.

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev)
$ git merge master
Merge made by the 'recursive' strategy.
 C7.html | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 C7.html

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev)
$ git log
commit 2c33bf83387d72c144061f4c98cbefb9a547a190 (HEAD -> dev)
Merge: 193819f eacc6df
Author: sai <2495620791@qq.com>
Date:   Sat Oct 23 11:00:11 2021 +0800

    Merge branch 'master' into dev
    the commit.

commit eacc6df7732e144a2537c4305108881ebcea3e6f (origin/master, master)
Author: sai <2495620791@qq.com>
Date:   Sat Oct 23 10:57:02 2021 +0800

    c7

commit 193819f504ecbf66bd8095c8c273c7041edbe088 (origin/dev)
Author: sai <2495620791@qq.com>
Date:   Sat Oct 23 10:35:03 2021 +0800

    dev

commit 74b14f41ae13432f28afdef724caa8c44b658ac5
Author: sai <2495620791@qq.com>
Date:   Sat Oct 23 10:28:02 2021 +0800
:

```

merge的时候，会让你输入个备注，输入必要信息，保存退出即可，先按一下`esc`，然后输入`:wq`，回车

这是一个vim编辑器



我们通过`git log`，可以看到在`dev`分支中，也是有c7的版本提交记录的

我们在`dev`分支上，开发了一个新功能，假设是`a1.py`

然后快下班了，下班之前，要把dev分支提交

```
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev)
$ git add .

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev)
$ git commit -m '公司开发的第一天'
[dev 6d93e2a] 公司开发的第一天
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a1.py

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev)
$ git push origin dev
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 489 bytes | 489.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Powered by GITEE.COM [GNK-6.1]
To https://gitee.com/mindcons/code_sai.git
   193819f..6d93e2a  dev -> dev

```

## 6.2.回家拉代码，写完后提交

这个时候回家，2小时后，到家后继续敲代码

我们之前克隆过了

第一步，先把家里面的代码更新一下，不用做`git clone`，只要更新

`git pull origin dev`

切换到`dev`分支后，从远程拉代码下来

```
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/new_place/code_sai (dev)
$ git pull origin dev
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 6 (delta 2), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (6/6), 620 bytes | 1024 bytes/s, done.
From https://gitee.com/mindcons/code_sai
 * branch            dev        -> FETCH_HEAD
   193819f..6d93e2a  dev        -> origin/dev
Updating 193819f..6d93e2a
Fast-forward
 C7.html | 0
 a1.py   | 0
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 C7.html
 create mode 100644 a1.py

```

写到两点，在家里写了`a2.py`，然后推送到仓库

```
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/new_place/code_sai (dev)
$ git add .

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/new_place/code_sai (dev)
$ git commit -m '家里加班写了a2的功能'
[dev 751e26e] 家里加班写了a2的功能
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a2.py

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/new_place/code_sai (dev)
$ git push origin dev
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 255 bytes | 255.00 KiB/s, done.
Total 2 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Powered by GITEE.COM [GNK-6.1]
To https://gitee.com/mindcons/code_sai.git
   6d93e2a..751e26e  dev -> dev

```

## 6.3.到公司后拉代码，写完后提交

同理，第二天上班到公司后，第一件事不是写代码，而是把远程仓库的代码拉下来：

重复上面的即可

## 6.4.开发完毕

如果要上线，需要把dev分支，合并到master分支即可

此时dev开发了最后的功能，即将上线

```
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev)
$ git add .

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev)
$ git commit -m 'a3功能开发完毕，即将上线'
[dev 6e21f86] a3功能开发完毕，即将上线
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a3.py

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev)
$ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.

```

在master分支合并dev

```
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (master)
$ git merge dev
Updating eacc6df..6e21f86
Fast-forward
 a1.py    | 0
 a3.py    | 0
 dev.html | 0
 3 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a1.py
 create mode 100644 a3.py
 create mode 100644 dev.html

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (master)
$ git push origin master
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 2 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 901 bytes | 450.00 KiB/s, done.
Total 8 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Powered by GITEE.COM [GNK-6.1]
To https://gitee.com/mindcons/code_sai.git
   eacc6df..6e21f86  master -> master

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (master)
$
```

最后也可以把master分支合并到dev，并推送，让两者的代码保持一致

```
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (master)
$ git checkout dev
Switched to branch 'dev'
Your branch is up to date with 'origin/dev'.

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev)
$ git merge master
Updating d5b6ad2..c030879
Fast-forward
 a3.py | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 a3.py

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev)
$ git push origin dev
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote: Powered by GITEE.COM [GNK-6.1]
To https://gitee.com/mindcons/code_sai.git
   d5b6ad2..c030879  dev -> dev

```

## 6.5.忘推送代码了

在公司写了功能，commit了但是忘记push了

回到家写了另外的功能，然后push

第二天在公司pull的时候，会提示有冲突：

```
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev)
$ git pull origin dev
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 304 bytes | 0 bytes/s, done.
From https://gitee.com/mindcons/code_sai
 * branch            dev        -> FETCH_HEAD
   c030879..d9b6b9e  dev        -> origin/dev
Auto-merging a1.py
CONFLICT (content): Merge conflict in a1.py
Automatic merge failed; fix conflicts and then commit the result.

```

![在这里插入图片描述](https://img-blog.csdnimg.cn/0f23fbb8057345ce8a765734c01abca9.png)

查看产生冲突的文件，这个时候需要我们手动解决冲突（该保留的保留，该删的删）

![在这里插入图片描述](https://img-blog.csdnimg.cn/0e8397c9e26e44faa273ab9f4f04fb98.png)

然后继续开发，开发完后提交代码：

```
Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev|MERGING)
$ git add .

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev|MERGING)
$ git commit -m '解决冲突后，继续开发至完成'
[dev 61d8565] 解决冲突后，继续开发至完成

Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev)
$ git push origin dev
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 2 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (8/8), 943 bytes | 471.00 KiB/s, done.
Total 8 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Powered by GITEE.COM [GNK-6.1]
To https://gitee.com/mindcons/code_sai.git
   d9b6b9e..61d8565  dev -> dev

```

## 6.6.命令补充

- `git pull origin dev`等同于
  - `git fetch origin dev`
  - `git merge origin/dev`

图示：16集18:00

# 7.rebase应用场景

目的：让代码提交记录变得简洁

## 7.1.应用场景一

### 7.1.1.提交记录合并

假设总共提交了4次版本，可以用`git log`查看

- `git rebase -i `版本号 

  - 合并当前版本至目的版本之前的所有版本号

- `git rebase -i HEAD~3`

  - 合并当前版本，距离最近的3条记录

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/fc6d7a01eaa144f89262d1904bb20ecf.png)

  把第二行和第三行的`pick`修改为`s`，表示希望当前的版本，合并到上一个版本上去

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/9997a894e10c4238972600f183376f19.png)

  保存退出，进入提交信息修改界面，保存退出

### 7.1.2.备注

  已经push到仓库的，不建议合并，否则会很麻烦

## 7.2.应用场景二

开发过程中的dev分叉，也是可以合并的

- `git log --graph`

  以分支的形式显示

- `git log --graph --pretty=format:"%h %s"`

  更加简洁的显示

  ```
  Administrator@IT-20191111ZDGI MINGW64 /d/hh/workspace/git/code_sai (dev|REBASE 3/3)
  $ git log --graph --pretty=format:"%h %s"
  * fbb73dc dev_rebase
  * 8b5dd1e # This is a combination of 2 commits. # This is the 1st commit message:
  *   c030879 Merge branch 'dev'
  |\
  | * d5b6ad2 a4
  | *   a33a827 Merge branch 'dev' of https://gitee.com/mindcons/code_sai into dev
  | |\
  | | * 751e26e 家里加班写了a2的功能
  * | | 0b34eb4 up
  |/ /
  * / 6e21f86 a3功能开发完毕，即将上线
  |/
  * 6d93e2a 公司开发的第一天
  *   2c33bf8 Merge branch 'master' into dev the commit.
  |\
  | * eacc6df c7
  * | 193819f dev
  |/
  * 74b14f4 first commit
  
  ```


- 现在`dev`中开发，commit
- 然后在`dev`中，执行`git rebase master`
- 接着切换到`master`，再执行`git merge dev`
- 最后显示`git log --graph --pretty=format:"%h %s"`的时候，就没有分叉了



## 7.3.应用场景三

之前忘记提交代码的案例中，v1和v2的合并，会产生分叉

不要直接`git pull`

- `git pull`
  - `git fetch`
  - `git merge`

直接`git pull`，拉到本地后，回执行`git merge`的操作，

我们直接`git fetch origin dev`，再执行`git rebase origin/dev`

这样子合并的话，提交记录就不会产生分叉。

`git rebase`的时候，上述都是默认没有冲突的。

出现冲突后，按照提示解决冲突后，最后可以执行`git rebase --continue`

## 7.4.beyond compare快速解决冲突

- 安装软件

- 在git中配置，`--local`表示只在当前项目有效

  ```
  git config --local merge.tool bc3
  git config --local mergetool.path '/usr/local/bin/bcomp'
  git config --local mergetool.keepBackup false
  ```

- 应用`beyond compare`解决冲突

  ```
  git mergetool
  ```

## 7.5.命令总结



# 8.git flow工作流

![在这里插入图片描述](https://img-blog.csdnimg.cn/69a33cb6a4214f38b719036e1c88c04a.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/9205c94363db4687a6990905f29d7ba0.png)







协同开发：

- 邀请成员
- 创建组织

## 8.1.git tag

多次`commit`之后，可以

```
git tag -a v1 -m '第一版'
git push origin --tag
```

在git远程，就可以看到tag的版本了：

![在这里插入图片描述](https://img-blog.csdnimg.cn/50d9096b658c4c4db2fddb2426ceb93c.png)

## 8.2.邀请成员

邀请成员进入组织

再邀请成员进入仓库

然后成员创建分支，进行开发

`git checkout -b dev`

创建，并切换分支

邀请，并设置开发权限

小弟操作：

```
// 先从主分支拆分
git checkout dev

// 功能点实际开发时，再拆分
git checkout -b '功能点1'
```

## 8.3.代码review

成员开发完后，需要做代码review

可以用`pull request`实现，在此之前，需要做一下branch的配置：

git中设置：

![在这里插入图片描述](https://img-blog.csdnimg.cn/7f6d8ebb75724251869e3f941418edf6.png)



![在这里插入图片描述](https://img-blog.csdnimg.cn/2429209b638d4429a7a18b2e25ab337f.png)

成员创建`pull request`

![在这里插入图片描述](https://img-blog.csdnimg.cn/ba98c67cbdd14f0e95c5712fe6c330e8.png)

提交后

![在这里插入图片描述](https://img-blog.csdnimg.cn/db5546ed2af94478a849c2df8f7f681a.png)

管理人员：



![在这里插入图片描述](https://img-blog.csdnimg.cn/7fad3616b4c749c59f2fff5993372779.png)



![在这里插入图片描述](https://img-blog.csdnimg.cn/f1802e7c72414a569f283a60d74e7da1.png)

## 8.4.测试上线

从dev分支，切除release版本

```
git checkout -b release 
git push origin release
```

测试完成，把`release`版本`pull request`到`master`中

还要将`release`合并到`dev`，也可以直接`merge`（代码review的时候，不能直接merge）

最后删除`release`

然后把代码拉下来，打tag标识版本，并推送

最后上线的，可以上线tag的v2版本

```
git branch -d release
git checkout master
git pull origin master
git tag -a v2 -m '第二版'
git push origin --tags
```



# 9.给开源项目贡献代码

- 将别人的源代码，拷贝到自己的仓库

- 在自己的仓库修改
- 给源代码的作者，提交修复bug的申请（pull reqeust）
  - 把自己的`master`，申请合并到对方的`master`

# 10.补充

## 10.1.配置文件存放的三个位置

- 项目配置文件：`.git/config`

  ```
  git config --local user.name 'aaa'
  git config --local user.email 'aaa@aa.com'
  ```

- 全局配置文件：`~/.gitconfig`

  ```
  git config --global user.name 'aaa'
  git config --global user.email 'aaa@aa.com'
  ```

- 系统配置文件：`/etc/.gitconfig`

  ```
  git config --system user.name 'aaa'
  git config --system user.email 'aaa@aa.com'
  
  需要有root权限
  ```

优先级：现在项目找，再在全局找，最后在系统找

应用场景：

```
git config --local user.name 'aaa'
git config --local user.email 'aaa@aa.com'

git config --local merge.tool bc3
git config --local mergetool.path '/usr/local/bin/bcomp'
git config --local mergetool.keepBackup false

git remote add origin 地址 // 默认添加在本地配置文件中（--local）
```

## 10.2.git免密登陆

- url中体现

  ```
  原来的地址：https://gitee.com/mindcons/code_total.git
  修改的地址：https://用户名:密码@gitee.com/mindcons/code_total.git
  
  
  git remote add https://用户名:密码@gitee.com/mindcons/code_total.git
  git push origin master
  ```

- ssh实现

  ```
  1.生成公钥和私钥
  git 终端：
  ssh-keygen
  2.存储位置
  默认放在(~/.ssh)
  id_isa.pub 公钥
  id_isa 私钥
  3.拷贝公钥的内容，并设置到github中
  4.在git本地配置ssh地址
  	git remote add origin git@gitee.com:mindcons-g/python.git
  5.以后使用
  	git push origin master
  ```

- git自动管理凭证

## 10.3.git忽略文件

创建`.gitignore`文件

让git不再管理当前目录下的某些文件

```
*.h
!a.h
files/
*.py[c|a|d]
```

## 10.4.任务管理相关

- issues

- wiki
  - 记录文档
