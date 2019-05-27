이름 등록

Woong@DESKTOP-NIDPCHU MINGW64 ~
$ git config --global user.name Jin-Woong

Woong@DESKTOP-NIDPCHU MINGW64 ~
$ git config user.name
Jin-Woong



이메일 등록

Woong@DESKTOP-NIDPCHU MINGW64 ~
$ git config --global user.email kjw7236@gmail.com

Woong@DESKTOP-NIDPCHU MINGW64 ~
$ git config user.email
kjw7236@gmail.com



git setting list

Woong@DESKTOP-NIDPCHU MINGW64 ~
$ git config --list
core.symlinks=false
core.autocrlf=true
core.fscache=true
color.diff=auto
color.status=auto
color.branch=auto
color.interactive=true
help.format=html
rebase.autosquash=true
http.sslbackend=openssl
http.sslcainfo=C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
credential.helper=manager
user.name=Jin-Woong
user.email=kjw7236@gmail.com



Pycharm에서 터미널을 cmd 대신 git bash로 설정하기

 Ctrl+Alt+s  > Pycharm 설정창

![1558661338757](C:\Users\Woong\AppData\Roaming\Typora\typora-user-images\1558661338757.png)





가상환경에서 파이썬 모듈 등이  포함된 파일을 전부 커밋하면 용량이 커지므로 커밋하지 않을 파일들을 설정

![1558661564264](C:\Users\Woong\AppData\Roaming\Typora\typora-user-images\1558661564264.png)



<https://gitignore.io/>로 접속

![1558661154688](C:\Users\Woong\AppData\Roaming\Typora\typora-user-images\1558661154688.png)



![1558661207758](C:\Users\Woong\AppData\Roaming\Typora\typora-user-images\1558661207758.png)

....



텍스트 내용 전체 복사하여

.gitignore 파일에 붙여넣기

![1558661258907](C:\Users\Woong\AppData\Roaming\Typora\typora-user-images\1558661258907.png)



이전에 생성한 markdown.md 파일을 Pycharm 프로젝트로 옮기고

터미널에서 markdown.md,   .gitignore 파일 git add



Woong@DESKTOP-NIDPCHU MINGW64 /c/Users/Woong/PycharmProjects/0524-python (master)
$ git add markdown.md

Woong@DESKTOP-NIDPCHU MINGW64 /c/Users/Woong/PycharmProjects/0524-python (master)
$ git add .gitignore

Woong@DESKTOP-NIDPCHU MINGW64 /c/Users/Woong/PycharmProjects/0524-python (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   .gitignore
        new file:   markdown.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        .idea/



Woong@DESKTOP-NIDPCHU MINGW64 /c/Users/Woong/PycharmProjects/0524-python (master)
$ git commit -m "마크다운 사용법"
[master (root-commit) b85ab99] 마크다운 사용법

 2 files changed, 288 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 markdown.md



Woong@DESKTOP-NIDPCHU MINGW64 /c/Users/Woong/PycharmProjects/0524-python (master)
git log
commit b85ab993841d3b31b73b4e59693a68e5ab887afc (HEAD -> master)
Author: Jin-Woong <kjw7236@gmail.com>
Date:   Fri May 24 10:38:04 2019 +0900

    <EB><A7><88><ED><81><AC><EB><8B><A4><EC><9A><B4> <EC><82><AC><C3><AC><C2><9A> <EC><82><AC><EC><9A><A9><EB><B2><95>



$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        .idea/

nothing added to commit but untracked files present (use "git add" to track)



.idea 파일을 git 하지 않기위해 .gitignore 파일에 .idea 파일추가



Woong@DESKTOP-NIDPCHU MINGW64 /c/Users/Woong/PycharmProjects/0524-python (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   .gitignore

no changes added to commit (use "git add" and/or "git commit -a")



현재 폴더의 모든 파일 git add

Woong@DESKTOP-NIDPCHU MINGW64 /c/Users/Woong/PycharmProjects/0524-python (master)
$ git add .



커밋 메세지와 함께 커밋

Woong@DESKTOP-NIDPCHU MINGW64 /c/Users/Woong/PycharmProjects/0524-python (master)
$ git commit -m "Modify .gitignore"
[master 959a097] Modify .gitignore
 1 file changed, 3 insertions(+), 1 deletion(-)



Woong@DESKTOP-NIDPCHU MINGW64 /c/Users/Woong/PycharmProjects/0524-python (master)
$ git status
On branch master
nothing to commit, working tree clean



push할 github 경로 등록

Woong@DESKTOP-NIDPCHU MINGW64 /c/Users/Woong/PycharmProjects/0524-python (master)
$ git remote add origin https://github.com/Jin-Woong/hackerthon-python.git

Woong@DESKTOP-NIDPCHU MINGW64 /c/Users/Woong/PycharmProjects/0524-python (master)
$ git remote --v
origin  https://github.com/Jin-Woong/hackerthon-python.git (fetch)
origin  https://github.com/Jin-Woong/hackerthon-python.git (push)



위에서 등록한 origin경로로 push

Woong@DESKTOP-NIDPCHU MINGW64 /c/Users/Woong/PycharmProjects/0524-python (master)
$ git push origin master
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 4 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (10/10), 3.87 KiB | 990.00 KiB/s, done.
Total 10 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/Jin-Woong/hackerthon-python.git

 * [new branch]      master -> master



github에서 커밋한 파일들 내려받기

![1558672456317](C:\Users\Woong\AppData\Roaming\Typora\typora-user-images\1558672456317.png)

Woong@DESKTOP-NIDPCHU MINGW64 /c/Users/Woong/PycharmProjects/test
$ git clone https://github.com/Jin-Woong/hackerthon-python.git
Cloning into 'hackerthon-python'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 10 (delta 2), reused 10 (delta 2), pack-reused 0
Unpacking objects: 100% (10/10), done.



Woong@DESKTOP-NIDPCHU MINGW64 /c/Users/Woong/PycharmProjects/test
$ ls -al
total 8
drwxr-xr-x 1 Woong 197121 0 5월  24 13:32 ./
drwxr-xr-x 1 Woong 197121 0 5월  24 13:30 ../
drwxr-xr-x 1 Woong 197121 0 5월  24 13:32 hackerthon-python/





