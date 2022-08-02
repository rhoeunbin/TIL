## 힙(Heap)&셋(Set)

우선순위 큐(Priority Queue) : 우선순위를 기준으로 가장 우선순위가 높은 데이터가 가장 먼저 나가는 방식

1. 가중치가 있는 데이터
2. 작업 스케줄링
3. 내트워크



- dequeue - 큐의 맨 앞 데이터를 가져오기
- enqueue - 큐의 맨 뒤에 데이터를 삽입



#### 우선순위 큐를구현하는 방법

1. 배열(Array)
2. 연결 리스트
3. 힙(Heap) = 등호 관계가 아닌 힙은 우선순위 큐를 활용할 수 있다고 봄



#### 힙 시간복잡도

|        연산 종류        |   Enqueue   |   Dequeue   |
| :---------------------: | :---------: | :---------: |
|       배열(Array)       |    O(1)     |    O(N)     |
|       정렬된 배열       |    O(N)     |    O(1)     |
| 연결리스트(Linked List) |    O(1)     |    O(N)     |
|    정렬된 연결리스트    |    O(N)     |    O(1)     |
|      **힙(Heap)**       | **O(logN)** | **O(logN)** |

***O(logN)** 시간복잡도가 빠르다*

*heap으로 하면 넣을 때도 뺄 때도 효율적*



#### 힙의 특징

- **최대값 최소값을 빠르게 **찾아내도록 만들어진 데이터 구조

- **느슨한 정렬 상태를 지속적으로 유지**(1 2 3 4 5 가 아닌 -> 1 3 2 5 4 인 애매한 형태)

- 중복 값 허용



#### 힙은 언제 사용?

1. 데이터가 지속적으로 정렬되어야 할 때
2. 데이터에 삽입/삭제가 빈번할 때



#### 파이썬의 heqpq 모듈

- Minheap(최소 힙)으로 구현(가장 작은 값이 먼저 옴) ↔ Maxheap
- 삽입, 삭제, 수정, 조회 **연산의 속도가 리스트보다 빠름**



`heapq.heapify`

`heapq.heappop(heap) `

`heapq.heappush(heap, item)`



```python
import heapq

numbers = [5, 3, 2, 4, 1]

heapq.heapify(numbers)  #heap으로 만들겠다 numbers를 distructive로 만듦

print(result)  #None -> =numbers.sort()와 같은 distructive method이기 때문
print(numbers)  #1 3 2 4 5


import heapq

numbers = [5, 3, 2, 4, 1]
heapq.heapify(numbers) #1 3 2 4 5

heapq.heappop(numbers) 
print(numbers) #2 3 5 4

heapq.heappop(numbers)
print(numbers) # 3 4 5

heapq.heappush(numbers. 10) # 3 4 5 10
heapq.heappush(numbers. 0) # 0 3 5 10 4
```

---

### 셋(Set)

> 수학에서의 '집합'을 나타내는 데이터 구조

1. .add()
2. .remove()
3. 합집합 +
4. 차집합 -
5. 교집합 &
6. 대칭차 ^



#### Set은 언제 사용? 

1. 데이터의 중복이 없어야 할 때
2. 정수가 아닌 데이터의 삽입/삭제/탐색이 빈번할 때



#### Set의 시간복잡도

탐색, 제거 - O(1)

합집합, 교집합, 차집합, 대칭 차집합 - O(N)



