def self_number(x):
    answer.append(x + sum(map(int,str(x))))

answer = [] #생성자가 있는 숫자가 answer 리스트로 들어감
for i in range(1,10001): #분해합이 만들어지고 리스트에 들어감
    self_number(i)
    if i not in answer: #본인보다 큰 숫자는 이미 없으니깐 출력됨
        print(i)