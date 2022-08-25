def solution(absolutes, signs): #함수 선언
    total = 0 #합

    for i in range(len(absolutes)): #absolutes의 길이만큼
        if signs[i] == True: #signs[i]가 True이면 +이므로
            total += absolutes

        else: #signs[i]가 False이면 -이므로
            total -= absolutes

    return total #total 값 반환