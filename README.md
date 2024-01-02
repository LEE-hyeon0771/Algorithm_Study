# Algorithm_Study
Study of Algorithm & Practice for Coding-test

Rule : 유형정리 이후 백준 1 day 1 sol

개인 블로그 : 
이현 https://pred0771.tistory.com/category/Algorithm



| ![](https://github.com/LEE-Hyeon0771.png) |
| :--------------------------------------: | 
|             **이현<br>(Developer)<br>연세대학교 미래캠퍼스**              |  

## 주 개발 언어
<img src="https://img.shields.io/badge/Java-007396?style=flat&logo=Java&logoColor=white" /> <img src="https://img.shields.io/badge/Python-1572B6?style=flat&logo=Python&logoColor=white" />

## 참고 사이트
1. Baekjoon <https://www.acmicpc.net/>
2. Programmers <https://programmers.co.kr/>
3. https://solved.ac/problems/level
4. https://github.com/LEE-hyeon0771/baekjoon



## Algorithm 유형정리(프로그래머스 고득점 kit, 백준 사용)
### 1. Stack & Queue
- 일반적으로 순서를 찾는 문제 유형이 대다수이다. 배열 속에서 Stack과 Queue, deque를 사용하여 선입선출, 후입선출, 양쪽으로 조절 할 수 있도록 만들고 순서 배열을 요구하는 유형을 가진다.

- [같은 숫자는 싫어](https://pred0771.tistory.com/96)
- [올바른 괄호](https://pred0771.tistory.com/97)
- [기능개발](https://pred0771.tistory.com/98)
- [프린터](https://pred0771.tistory.com/99)
- [다리를 지나는 트럭](https://pred0771.tistory.com/101)
- [주식가격](https://pred0771.tistory.com/102)
- [카드2](https://pred0771.tistory.com/162)
- [후위표기식2](https://pred0771.tistory.com/163)
- [프린터 큐](https://pred0771.tistory.com/164)
- [쇠막대기](https://pred0771.tistory.com/165)
- [괄호의 값](https://pred0771.tistory.com/166)
- [괄호제거](https://pred0771.tistory.com/167)
- [탑](https://pred0771.tistory.com/168)

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
- [Four Squares(백준 17626)](https://pred0771.tistory.com/148)
- [퇴사(백준 14501)](https://pred0771.tistory.com/149)
- [큰 수 구성하기(백준 18511)](https://pred0771.tistory.com/151)
- [카드놓기(백준 5568)](https://pred0771.tistory.com/152)
- [숫자야구(백준 2503)](https://pred0771.tistory.com/153)
- [도영이가 만든 맛있는 음식(백준 2961)](https://pred0771.tistory.com/155)

### 5. Greedy
- 탐욕법 알고리즘으로 순간 순간 마다 최적의 경우의 수를 선택하여 최적화하는 알고리즘. 최적화를 보장해주지는 않지만, 일반적으로 코딩테스트에서는 최적화가 가능하도록 설계되어 있으므로 이론적인 최적의 경우의 수를 택할 것.

- [체육복](https://pred0771.tistory.com/135)
- [주유소(백준 13305)](https://pred0771.tistory.com/177)
- [서강근육맨(백준 20300)](https://pred0771.tistory.com/178)

### 6. Binary Search
- 완전탐색(Brute Force)와 결국 유사한 알고리즘을 가지고 있는 방식이지만, 줄일 수 있다면 절반부터 업다운 느낌으로 조금이라도 검색할 자료를 줄여 시간복잡도를 좋게 만들어 주는 알고리즘 방식이다. 뭔가 값을 찾아내야 하지만 손이나 머리로 풀 때 한 번에 잘 보이지 않는 경우 이분탐색 알고리즘을 떠올려 보면 좋다.

- [수 들의 합(백준 1789)](https://pred0771.tistory.com/156)
- [숫자카드(백준 10815)](https://pred0771.tistory.com/157)
- [정수 제곱근(백준 2417)](https://pred0771.tistory.com/158)
- [IF문 좀 대신 써줘(백준 19637)](https://pred0771.tistory.com/159)
- [나무자르기(백준 2805)](https://pred0771.tistory.com/160)

### 7. Priority Queue
- 일반적인 Queue와는 다르게 Heap의 개념을 사용한다. python에서는 heapq를 import하여 쉽게 사용할 수 있어 heapq와 빈 리스트를 사용하면 간편하게 사용할 수 있는 방식이다.

- [문자열 집합(백준 14425)](https://pred0771.tistory.com/169)
- [최대 힙(백준 11279)](https://pred0771.tistory.com/170)
- [N번째 큰 수(백준 2075)](https://pred0771.tistory.com/171)
- [생태학(백준 4358)](https://pred0771.tistory.com/173)
- [절댓값 힙(백준 11286)](https://pred0771.tistory.com/174)

### 8. Tree
- 트리 문제는 트리를 직접 손으로 그려서 시각화 한 후 DFS, BFS 알고리즘을 사용하여 문제를 해결하는 것이 바람직한 접근 방법이다.

- [트리의 부모찾기(백준 11725)](https://pred0771.tistory.com/176)

### 9. Math

- [소수&팰린드롬(백준 1747)](https://pred0771.tistory.com/179)
