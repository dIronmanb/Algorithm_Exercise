# 알고리즘 예제 풀이
알고리즘을 배운 후 직접 익히기 위해 만들었습니다.  
문제들은 백준에서 가져왔으며 먼저 풀고 남들은 어떻게 풀었는지를 분석할 예정입니다.

<br/>
<br/>

# 그전에...
현재 나는 우분투 내에서 알고리즘 문제를 풀고 있다. 다음과 같은 명령어를 치면 파이썬 버전을 알 수 있다. 저자는 파이썬 버전 2.7.17를 사용한다.
```
 $ python -V
```

윈도우에서는 파이썬 3.x 버전을 사용하고 있어서 알고리즘을 푸는데 있어서 문제가 발생하지는 않는다. 다만, 우분투에서는 2.x 버전을 3.x으로 변경해줄 필요가 있다. 다음 두 가지를 알아보도록 하자.
## 1. 파이썬 버전 2.x에서 3.x로 바꾸는 방법
파이썬이 설치되는 경로를 알아보자.
```
 $ whereis python
``` 
저자의 경우 다음과 같이 다양한 파이썬 파일들을 확인할 수 있었다.
```
 $ python: /usr/bin/python3.6-config /usr/bin/python3.6 /usr/bin/python /usr/bin/python3.6m /usr/bin/python3.6m-config /usr/bin/python2.7-config /usr/bin/python2.7 /usr/lib/x86_64-linux-gnu/python2.7 /usr/lib/python3.7 /usr/lib/python3.8 /usr/lib/python3.6 /usr/lib/python2.7 /etc/python3.6 /etc/python /etc/python2.7 /usr/local/lib/python3.6 /usr/local/lib/python2.7 /usr/include/python3.6 /usr/include/python3.6m /usr/include/python2.7 /usr/include/python2.7_d /usr/share/python /usr/share/man/man1/python.1.gz
```
터미널 창에서 `python`만 치면 우분투의 기본으로 깔려 있는 파이썬이 실행된다.
```
$ python
Python 2.7.17 (default, Feb 27 2021, 15:10:58) 
[GCC 7.5.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
현재 버전이 2.7.17인 파이썬이 실행됨을 알 수 있다.

현재 python 버전 3.x.x이 설치 되어 있지 않았으면 설치하도록 하자.

```
 $ sudo apt update
 $ sudo apt install python3.6
```
다음 명령어를 통해 실행될 때 사용되는 파이썬 버전을 선택할 수 있다.
```
 $ sudo update-alternatives --config python
 ```
 저자의 경우 다음과 같이 두 개의 버전을 확인할 수 있다. 0번에는 auto mode으로 되어 있다.
 ```
  선택       경로              우선순� 상태
 ------------------------------------------------------------
 * 0            /usr/bin/python3.6   2         자동 모드
   1            /usr/bin/python2.7   1         수동 모드
   2            /usr/bin/python3.6   2         수동 모드

Press <enter> to keep the current choice[*], or type selection number: 
 ```

 2를 선택하면 파이썬 3.x버전으로 사용할 수 있게 된다.
 
 <br/>
 <br/>

 

## 2. 파이썬 버전 3.x에서 2.x로 바꾸는 방법
 파이썬 버전 3.x에서 2.x로 바꾸는 방법을 왜 다시 돌아가게 하는가에 대해 의문이 생길 수도 있는데, 추후 터미널을 켤 때 안켜지는 문제가 발생한다. (특히 terminator를 설치한 분들이라면 더욱...)이를 해결하기 위해서는 파이썬 버전을 2.x로 다시 맞추어야 한다. terminator가 파이썬 2.x을 기반으로 돌아가기 때문이다.

<br/>

위에서 사용했던 명령어를 다시 사용해보자.
```
$ sudo update-alternatives --config python
```

다음과 같은 창이 뜰 것이다.

```
  선택       경로              우선순� 상태
------------------------------------------------------------
* 0            /usr/bin/python3.6   2         자동 모드
  1            /usr/bin/python2.7   1         수동 모드
  2            /usr/bin/python3.6   2         수동 모드
```
여기서 1를 선택하여 버전이 2.x가 되도록 하자. 
Ctrl + Alt + T를 누르면 터미널 창이 따시 뜰 것이다.