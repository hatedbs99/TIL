# 웹 브라우저에 URL을 입력하면 일어나는 일

브라우저는 웹서버를 통해 리소스(image, js, html + css)를 가져온다.

UI는 항상 Data structure에 의존한다.

![브라우저 구성 요소](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20220608013010703.png)

​																			 브라우저 구성 요소

렌더링 엔진은 통신으로부터 요청한 문서의 내용을 얻는 것으로 시작하는데 문서의 내용은 보통 8KE

다음은 렌더링 엔진의 기본적인 동작 과정이다.

DOM 트리 구축을 위한 HTML 파싱 -> 렌더 트리 구축 -> 렌더 트리 배치 -> 렌더 트리 그리기



![image-20220608013421374](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20220608013421374.png)

TCP/IP 연결 후 HTTP 통신이 이루어지기 시작하면 HTML을 제일 먼저 가져온다. 이후, HTML 구문 분석을 통해 DOM 트리를 만들 수 있다. 다음으로 스타일시트가 넘어오게 되고 스타일시트를 파싱하고 렌더트리가 완성되어 화면에 렌더링이 이루어진다.



Tree => 비선형 자료구조

TCP통신은 끊기고 HTTP통신은 이루어짐.