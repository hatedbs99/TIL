# GIT Command

#### git config

git 설치 후 username과 email 등록

```shell
git config --global user.name "Juho"
git config --global user.email "hatedbs99@gmail.com"
```



#### git init

기존 디렉토리를 Git저장소로 만듬

```shell
git init
```



#### git add

파일을 새로 추적

```shell
git add . # 모든 파일과 폴더
git add <file> # 파일
```



#### git commit

수정사항을 commit하여 Staging Area에 저장

```shell
git commit -m "commit message"
```



#### git remote

remote repository 세팅

```shell
git remote add origin https://github.com/hatedbs99/til.git
```



#### git push

원격 저장소에 파일을 적용

```shell
git push -u origin master
```



