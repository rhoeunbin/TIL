n = int(input())
nums = list(map(int,input().split())) #오르막길 숫자들 리스트로 input

cnt = 0 #오르막길 count
height = [] #오르막길 길이

for i in range (len(nums) - 1):  #0~4
    if nums[i] < nums[i+1] :  #i값이 i+1보다 작다면
        cnt += nums[i+1] - nums[i]  #i+1값 - i값을 cnt에 더함(오르막길임)

    if nums[i] >= nums[i+1] : #i값이 i+1보다 크다면 => 오르막길 아님
        cnt = 0       # cnt = 0 출력
        height.append(cnt)  #오르막길 길이에 cnt = 0 추가
    height.append(cnt)  #오르막길 길이에 cnt 값 추가

print(max(height))   #가장 큰 값 출력

