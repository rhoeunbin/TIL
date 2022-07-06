# CLI(Command Line Interface)

### 프롬포트 기본 인터페이스(명령 기반의 인터페이스)

- 컴퓨터 정보
- 디렉토리
- $



mac OS : terminal

Windows : cmd



# 디렉토리 관리

- `pwd`(print working directory) : 현재 디렉토리(폴터/파일) 출력

- `cd` (change directory) : 디렉토리 이동

  ex) `cd .git` : git으로 이동

  `cd .. ` : 위의 폴더로 이동(띄어쓰기 주의)

  `.`  : 현재 디렉토리

- `ls` (list) : 목록

- `mkdir` (make directory) : 디렉토리 생성

  l하고 tab 누르면 경로를 만들어줌

- `touch` : 파일 생성

- `rm` (remove) : 파일 삭제

- `rm -r 폴더이름` : 폴더 지우기삭제

  

✍`cntl+l`  : 지우기

---



#### 오류

띄어쓰기, (1, ㅣ,L, ㅣ, l)

폴더 만들 때 띄어쓰기 보다는 _사용이 편함



✍`cntl+shift+s ` :  캡처



# Git

### 버전 관리

 버전 : 컴퓨터 소프트웨어의 특정 상태 

ex) 구글 docx, git

---

#### 💡저장소 처음 만들 때

`$ git init`  : 버전을 기록할 때  →`(master)` 가 뜨면 됨
`$ git add .`  : (U 면 아직add 안 된 상태 > A: add O)
`$ git commit -m `  : '커밋메시지'

상태 확인할 때
`$ git status`  : 1통, 2통
`$ git log`  : 커밋 확인

---

#### git add  

: 중간 공간(별도로 버전 지정이 가능하기 때문에)

*일종의 임시공간* (물리적인 것을 바꾸는 건 아니다!)

 `git add 파일이름` 으로 따로 가능

​	`git add .`  : 전체 파일



❔만약 다른 버전을 넣고 싶다면

a, b, c 가 있을 때

a는 이미지 b,c 는 글 자료 라면

b, c 따로 add 후 commit

a add 후 commit

---

#### commit: 버전 기록

- `git commit -m` : staged 상태의 파일들 커밋메세지 기록

*내가 무슨 작업을 했는지 기록한 행위이기 때문에 중요*



git- 스냅샷으로 관리, 매우 크기 작음

파일이 달라지지 않으면 성능을 위해 파일을 새로 저장 x

---

#### 파일 라이프사이클

- Tracked : 이전부터 버전으로 관리되는 파일

​		modified : 파일이 수정된 상태 (add를 통해)

​		staged :  수정한 파일 곧 커밋할 것이라고 표시 상태

​		commited  : 커밋 완료

- Untracked : 버전으로 관리된 적 없는 파일(새로 만든 파일)



untracked> staged>commit-unmodified>modified

---

#### git log : 현재 저장소에 기록된 커밋 조회

git log-1 : 최근 이전의 것

git log --oneline : 최근 것을 한줄로

git log-2 --oneline : 최근 2개를 한줄로 보여줌

---

#### Config

- 사용자 정보 입력

` $git config —global user.name “username”`

`$git config —global user.email “my@email.com”`

- 설정 확인

  git config -l 	

  git config —global -l 

  git config user.name

---

#### 디렉토리

`cd .` : 현재 디렉토리 확인 가능

`cd ..` : 상위 디렉토리 확인 가능
