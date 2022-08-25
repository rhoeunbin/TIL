LJESNJAK = ['c=','c-','dz=','d-','lj','nj','s=','z='] #크로아티아 리스트

cro = input() #단어 input 받기
for i in LJESNJAK: #변수 i가 크로아티아 리스트에 있으면
    cro = cro.replace(i, 'a') # 그 데이터를 a 로 변경하고

print(len(cro)) # 길이를 구한다