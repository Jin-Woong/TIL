# Git
## 기본 명령어
1. git 저장소 (repository) 초기화

   ```bash
   $ git init
   ```

   - 원하는 폴더를 저장소로 만들게 되면, git bash에서는 (master)라고 표기된다.
   - 그리고 숨김폴더로 `.git/` 이 생성된다.

2. 커밋할 목록에 담기 (Staging Area)

   ```bash
   $ git add .
   ```

   - 현재 작업 공간(Working Derectory / Tree)의 변경사항을 커밋할 목록에 추가한다. (`add`)
   - `.` 리눅스에서 현재 디렉토리(폴더)를 표기하는 방법으로, 현재 내 폴더에 있는 파일의 변경사항을 전부 추가한다.
   - 단일파일만 추가할면 `git add "파일이름"`
   - 폴더를 추가하려면 `git add "폴더이름/

3. 커밋하기

   ```bash
   $ git commit -m '______'
   ```

   - 커밋을 할때에는 해당하는 버전의 이력을 의미하는 메시지를 반드시 적어준다.
   - 메세지는 지금 버전을 쉽게 이해할 수 있도록 작성한다.
   - 커밋은 현재 코드의 상태를 스냅샷 찍는 것이다.

4. 로그 확인

   ```bash
   $ git log
   
   commit 959a0978fe787e02cb1dd2b9cde9c1791d07ef7d (HEAD -> master)
   Author: Jin-Woong <kjw7236@gmail.com>
   Date:   Fri May 24 10:44:23 2019 +0900
   
       Modify .gitignore
   ```

   - 현재까지 커밋된 이력을 모두 확인할 수 있다.

5. git 상태확인하기 

   ```bash
   $ git status
   On branch master
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
   
           "Git\354\202\254\354\232\251\353\262\225.md"
   
   nothing added to commit but untracked files present (use "git add" to track)
   ```

   - CLI(Command Line Interface) 현재 상태를 알기 위해 반드시 명령어를 통해 확인한다.
   - 커밋할 목록에 담겨 있는지, untracked인지, 커밋할 내역이 있는지 등등 다양한 정보를 알려준다.


<<<<<<< HEAD


=======
>>>>>>> 681b79dee6b6c801441f50aa7014226375a2ad54
## 원격저장소 활용하기

1. 원격 저장소 (remote repository) 등록하기

   ```bash
   $ git remote add origin ____경로____
   ```

   - 원격 저장소 (`remote`)를 등록 (`add`)한다. (경로를  `origin` 이름으로 등록)
   - 최초에 한번만 등록하면 된다.
   - 아래의 명령어로 현재 등록된 원격 저장소를 확인할 수 있다.

   ```bash
   $ git remote --v
   origin  https://github.com/Jin-Woong/hackerthon-python.git (fetch)
   origin  https://github.com/Jin-Woong/hackerthon-python.git (push)
   ```

2. 원격 저장소에 올리기 (`push`)

   ```bash
   $ git push origin master
   ```

   - `git`! 올려줘(`push`) `origin`이라는 이름의 원격저장소에 `master`로!

3. 원격 저장소로부터 가져오기 (`pull`)

   ```bash
   $ git pull origin master
   ```



## 원격 저장소 복제(clone) 하기

```bash
$ git clone ____경로____
```

- 다운 받기를 원하는 폴더에서 `Git Bash`를 열고 위의 명령어를 입력한다.

- 경로는 `github`의 `repository`에서 우측의 초록색 버튼을 누르면 나타난다.

  

<<<<<<< HEAD


=======
>>>>>>> 681b79dee6b6c801441f50aa7014226375a2ad54
