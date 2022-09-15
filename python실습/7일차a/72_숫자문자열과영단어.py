def solution(s): #매개변수 s
    word = s #input
    num = {'0':"zero", '1':'one','2':'two','3':'three','4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    #숫자랑 문자를 넣은 딕셔너리
    for k, v in num.items(): #key, value를 뽑아 사용
        word = word.replace(v, k) #바뀌게 될 문자열: v, 바꿀 문자열: k
    
    return int(word) # 정수 형태로 출력

