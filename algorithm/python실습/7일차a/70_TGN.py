import sys
input = sys.stdin.readline

for i in range(int(input())):  #input 만큼 반복
    r, e, c = map(int,input().split())
    # r은 광고를 하지 않았을 때 수익, e는 광고를 했을 때의 수익, c는 광고 비용

    if r + c < e : #광고 X + 광고비용이 광고 했을 때보다 적으면
        print('advertise')
    elif r + c == e: #광고 X + 광고비용이 광고 했을 때와 같으면
        print('does not matter')
    else : #둘 다 아니면
        print('do not advertise')