# Algorithm_Study
Study of Algorithm & Practice for Coding-test

1주 당 코딩테스트 5문항 풀이 후 Tistory에 업로드(기록), 매주 study를 통해 스터디원들의 색다른 풀이를 경험

개인 블로그 : 
1. 이현 https://pred0771.tistory.com/category/Algorithm
2. 정유라 https://declare0703.tistory.com  
3. 박민서 https://minseocoding.tistory.com/
4. 김세온 https://kso323.tistory.com/
5. 김가을 https://velog.io/@kimgaeul02


| ![](https://github.com/LEE-Hyeon0771.png) | ![](https://github.com/yura0703.png) | ![](https://github.com/KSO012.png) | ![](https://github.com/2021247011parkminseo.png) | ![](https://github.com/kimgaeul02.png) |
| :--------------------------------------: | :--------------------------------------: | :--------------------------------------: | :-----------------------------------: | :------------------------------------: |
|             **이현<br>(Developer)<br>연세대학교 미래캠퍼스**              |             **정유라<br>(Developer)<br>연세대학교 미래캠퍼스**              |             **김세온<br>(Developer)<br>연세대학교 미래캠퍼스**              |            **박민서<br>(Developer)<br>연세대학교 미래캠퍼스**            |            **김가을<br>(Developer)<br>연세대학교 미래캠퍼스**             |

## 주 개발 언어
<img src = https://camo.githubusercontent.com/372dfe5550512c1b2e7e3649ea92a5cbadeec44a51c3b2bf822fe2a7a22c13d7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a6176612d3030373339363f7374796c653d666c61742d737175617265266c6f676f3d4a617661266c6f676f436f6c6f723d7768697465>

<img src = 
https://camo.githubusercontent.com/dd7559df3804c36eeeb5da15bb3445ea66682b8ffc736e2dc737e1975056cbf4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3337363641423f7374796c653d666c61742d737175617265266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465>

## 참고 사이트
1. Baekjoon <https://www.acmicpc.net/>
2. Programmers <https://programmers.co.kr/>
3. https://solved.ac/problems/level
4. https://github.com/LEE-hyeon0771/baekjoon



## Algorithm 유형정리(프로그래머스 고득점 kit 사용)
### 1. Stack & Queue
- 일반적으로 순서를 찾는 문제 유형이 대다수이다. 배열 속에서 Stack과 Queue, deque를 사용하여 선입선출, 후입선출, 양쪽으로 조절 할 수 있도록 만들고 순서 배열을 요구하는 유형을 가진다.

- [같은 숫자는 싫어](https://pred0771.tistory.com/96)
- [올바른 괄호](https://pred0771.tistory.com/97)
- [기능개발](https://pred0771.tistory.com/98)
- [프린터](https://pred0771.tistory.com/99)
- [다리를 지나는 트럭](https://pred0771.tistory.com/101)
- [주식가격](https://pred0771.tistory.com/102)

### 2. Sort
- 정렬 답게 정렬 하는 문제가 대다수이다. 또는 몇번째 수인지, 해당 index가 어디인지, 가장 큰 수, 가장 작은 수가 무엇인지 이런식으로 정렬이 필요한 문제 유형을 가진다.

- [K번째 수](https://pred0771.tistory.com/109)
- 가장 큰 수 
- [H-index](https://pred0771.tistory.com/108)

### 3. Hash
- set도 사용하기는 하지만, 주로 Map을 이용하는 문제가 많다. Python은 Map과 동일한 형태를 가진 dictionary를 제공하기 때문에 해시 테이블을 어떤식으로 구성할지만 설계되면 dictionary와 list를 적절히 잘 사용하는 방식의 유형으로 변하게 된다.

- [폰켓몬](https://pred0771.tistory.com/117)
- [완주하지 못한 선수](https://pred0771.tistory.com/118)
- [전화번호 목록](https://pred0771.tistory.com/120)
- [위장](https://pred0771.tistory.com/121)
- [베스트앨범](https://pred0771.tistory.com/123)

### 4. Brute Force
- for문으로 전체를 조사해야 하는 유형들이다. 하지만, 단순히 for문 만을 사용하게 만든다면 쉬운 문제이고, 난이도가 있는 문제에서는 조금 색다른 메서드들을 사용하여 문제 풀이가 진행되는 경우들이 많다. 메서드들을 기억해두지 않으면 처음부터 구현을 해야하여 많이 복잡해질 수 있기 때문에, Python의 장점인 메서드들을 많이 기억해두는 것이 좋다. 

- [최소직사각형](https://pred0771.tistory.com/125)
- [모의고사](https://pred0771.tistory.com/126)
- [소수찾기](https://pred0771.tistory.com/127)
- [카펫](https://pred0771.tistory.com/129)
- [피로도](https://pred0771.tistory.com/128)
- [모음사전](https://pred0771.tistory.com/131)
- [DNA(백준 1969)](https://pred0771.tistory.com/146)
- [치킨치킨치킨(백준 16439)](https://pred0771.tistory.com/147)

### 5. Greedy
- 탐욕법 알고리즘으로 순간 순간 마다 최적의 경우의 수를 선택하여 최적화하는 알고리즘. 최적화를 보장해주지는 않지만, 일반적으로 코딩테스트에서는 최적화가 가능하도록 설계되어 있으므로 이론적인 최적의 경우의 수를 택할 것.

- [체육복](https://pred0771.tistory.com/135)
