n = int(input()) # n은 정수
nums = list(map(int, input(). split())) #숫자들을 리스트로 받음
print(min(nums), max(nums)) #내장함수 써서 풀었ㄷ,,,

#알고리즘 식으로 고민해보기

n = int(input()) # n은 정수
nums = list(map(int, input(). split())) 

nums.sort(reverse = True)
print(nums[n-1], nums[0])