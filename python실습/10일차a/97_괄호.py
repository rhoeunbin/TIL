dic = {'{':'}', '[':']', '(':')','<':'>'}

for tc in range(10):
    len_ = int(input())


# from collections import deque
# exp = {'[':']', '{':'}', '(':')', '<':'>'}

# for tc in range(1, 11):
#     answer = 1
#     _ = int(input())
#     q = deque()
#     gwal = input()
#     for g in gwal:
#         if g in exp.keys():
#             q.append(g)
#         else :
#             if exp[q[-1]] == g :
#                 q.pop()
#             else:
#                 answer = 0
#                 break

#     print('#{} {}'.format(tc, answer))


for num in range(1, 11):
    g = {'(' : ')', 
         '[' : ']', 
         '{' : '}', 
         '<' : '>'}
    
    n = int(input())
    ghwalho = input()
    ans = 1

    left_g = []
    for i in ghwalho:
        if i in g.keys():
            left_g.append(i)
        else:
            if g[left_g[-1]] == i:
                left_g.pop()
            else:
                ans = 0
                break
    
    if not left_g:
        print(f'#{num}', ans)
    else:
        print(f'#{num}', ans)

