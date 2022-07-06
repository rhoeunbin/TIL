# GitHub (원격저장소)

> Git(GitHub)는 버전(커밋)을 관리한다.

---

##### 📢연습해보기

- *원격저장소 만들고 로컬저장소의 커밋 push하기*
  1. github에서 New Repository 만들기
  2. 저장소 설정하기
  3. github url 확인하기
  4. `$ git remote add origin 주소`

---

#### 원격저장소 정보 확인

`$ git remote -v`  :  원격 저장소의 정보 확인



 ✍`shift + insert` : 붙여넣기 단축키(cntl + c 아님)

---

#### Push(원격 저장소로 로컬 저장소 커밋을 올림)

`git push <원격저장소이름> <브랜치이름>` : (git push origin master)

🙄*push 할 때는 인증 정보 필수, 저장소의 버전(커밋)이 올라감*

---

#### Pull(원격 저장소 업데이트 커밋 가져오기)

`$ git pull <원격저장소이름> <브랜치이름>` 

wq로 끄기 or esc (작업 전에 항상)



---

#### Clone(원격저장소 복제)

> 모든 버전을 가져온다

`$ git clone <원격저장소주소(url)>` 

---

#### 💡한 번 더 정리

`git clone <url>`  원격 저장소 복제 

`git remote –v` 원격저장소 정보 확인 

`git remote add <원격저장소>`  원격저장소 추가 (일반적으로 origin) 

`git remote rm <원격저장소>` 원격저장소 삭제 

`git push <원격저장소> <브랜치>` 원격저장소에 push 

`git pull <원격저장소> <브랜치>` 원격저장소로부터 pull



##### 설정 변경하기 

`$ git config --global user.name "id"`

`$ git config --global user.email "email" `

##### 확인하기

` $ git config --global --list `



🙄*저장소(레퍼지토리) 이름 변경 시 로컬 설정 변경 필수*

🧨*저장소 삭제 : settings →  general → 하단부 danger zone*

🧨*저장소 접근 관리 : settings → collaborators (push 권한은 collaborator 에만 있음)*

---

### Push 실패

1. 원격저장소의 커밋을 원격저장소로 가져와서 (pull) 

2. 로컬에서 두 커밋을 병합 (추가 커밋 발생) 

   ​	동시에 같은 파일이 수정된 경우 merge conflict가 발생

3.  다시 GitHub으로 push



💡 **Tip**

*잘못 눌렀을 때는 cntl+c로 지우기*

*(END)가 나오면 q 쓰기*

*`$ git commit`만 적은 경우 길게 커밋 메세지 작성 후 cntl+s 누르고 닫으면 된다*



- 파일로 할 수 있는 것

 생성, 수정 .삭제, (조회)

---

### .gitignore

> 버전 관리랑 상관 없는 파일

git에서 추적하지 않는 파일 모아놓는다



`$ touch secret.csv`

$ touch .gitignore 미리 설정하면 secret이나 *.exe(exe로 쓰여진 파일 안 보이게) 등 실행할 수 있다 

- 특정 파일 : a.txt (모든 a.txt), test/a.txt (테스트 폴더의 a.txt)
- 특정 디렉토리 : /my_secret 
- 특정 확장자 : *.exe 
- 예외 처리 : !b.exe

커밋하기 전에 ignore 해야 됨 (이미 커밋된 파일은 반드시 삭제해야함)

🙄*프로젝트 시작 전에 미리 설정하기*

개발 언어나 개발 환경에 따라서 다 다름

[.gitignore 사이트](http://ignore.io)

