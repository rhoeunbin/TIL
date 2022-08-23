while True:
    sen = input().upper()
    if sen == "#":
        break
    cnt = 0
    for i in sen:
        if i in 'AEIOU':
            cnt += 1
    print(cnt)

# sys쓰면 출력초과 남 => 개행을 안 넣어서!!