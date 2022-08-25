# alpha = []

# for i in range(5):
#     alpha.append(input())

#     for j in range(len(alpha)):





matrix = [] 
mx = 0
for i in range(5):
    k = input()
    matrix.append(k)
    mx = max(mx, len(k))
print(mx)

    # a = input()
    #   k = 15 - len(a)
    #   a += k * " "